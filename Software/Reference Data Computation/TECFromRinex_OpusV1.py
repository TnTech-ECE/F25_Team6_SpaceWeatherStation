# File Name: TECFromRinex_OpusV1.py
# Authors: Kenneth Creamer, Jackson Taylor
# Last Updated: May 3, 2026
# Purpose: Creates a set of vTEC and sTEC csv data from a rinex .26o file.
# Input format: A .26o rinex obeservation file.
#   Uses a .sp3 file for elevation angles preferably. Also intakes
#   a rinex .26n file for elevation angle compuation fallback.
# Output Files: a CSV of all computed data,
#   and a seperate csv of average vTEC per timestamp, which is an average
#   of all vTEC computations for all satellites at each timestamp.
#   To set rinex files to be processed, change directory
#   in lines 586, 589, and 595

import pandas as pd
import numpy as np
import sys
import os
import warnings
import matplotlib.pyplot as plt
import georinex as gr
import pymap3d as pm

# Suppress warnings from xarray/numpy for cleaner console output
warnings.filterwarnings('ignore')

# --- Constants ---
L1_FREQ = 1575.42
L5_FREQ = 1176.45
K = 1/40.3 * (L1_FREQ*1000000)**2 * (L5_FREQ*1000000)**2 / ((L5_FREQ*1000000)**2-(L1_FREQ*1000000)**2) * 10**-16

# mean height of ionospheric pierce point
H = 428800

# Effective mean Earth radius
R = 6371000 * 4 / 3

# GPS Orbital Constants (WGS84 / ICD-200)
GM = 3.986005e14  
OMEGA_E = 7.2921151467e-5  

# Broadcast ephemeris validity half-window (seconds). GPS ICD-200 specifies
# ephemerides are nominally valid for +/- 2 hours from Toe.
BRDC_VALIDITY_HALF_WINDOW_S = 2 * 3600

# Order of Lagrange interpolation polynomial for SP3 interpolation.
# 10 is the community standard for 15-minute SP3 data.
SP3_LAGRANGE_ORDER = 10


#Function that creates pandas data frame containing satellites with only L1 and L5 pseudorange measurements, and the timestamps of said measurements, and signal strength data
def get_l1_l5_pseudoranges(rinex_file, l1_code='C1', l5_code='C5', l1s_code='S1', l5s_code='S5'):
    """
    Extracts L1 and L5 pseudorange measurements from a RINEX observation file.
    Only retains epochs/satellites where BOTH signals are valid (non-NaN).
    """
    print(f"Loading RINEX OBS file: {rinex_file}...")
    try:
        obs = gr.load(rinex_file, fast= False)
    except Exception as e:
        print(f"Failed to load RINEX file. Error: {e}")
        sys.exit(1)

    available_vars = list(obs.data_vars)

    if l1_code not in available_vars or l5_code not in available_vars:
        print(f"\nError: The requested codes ('{l1_code}', '{l5_code}') are not both present in this file.")
        sys.exit(1)

    print("Filtering for simultaneous L1 and L5 measurements...")
    
    l1_data = obs[l1_code]
    l5_data = obs[l5_code]
    l1s_data = obs[l1s_code]
    l5s_data = obs[l5s_code]

    valid_mask = l1_data.notnull() & l5_data.notnull() & l5s_data.notnull() & l1s_data.notnull()

    l1_filtered = l1_data.where(valid_mask)
    l5_filtered = l5_data.where(valid_mask)
    l1s_filtered = l1s_data.where(valid_mask)
    l5s_filtered = l5s_data.where(valid_mask)

    df_l1 = l1_filtered.to_dataframe(name=l1_code).dropna().reset_index()
    df_l5 = l5_filtered.to_dataframe(name=l5_code).dropna().reset_index()
    df_l1s = l1s_filtered.to_dataframe(name=l1s_code).dropna().reset_index()
    df_l5s = l5s_filtered.to_dataframe(name=l5s_code).dropna().reset_index()

    merged_df = pd.merge(df_l1[['time', 'sv', l1_code]], 
                         df_l5[['time', 'sv', l5_code]], 
                         on=['time', 'sv'])
    
    merged_dfs = pd.merge(df_l1s[['time', 'sv', l1s_code]], 
                          df_l5s[['time', 'sv', l5s_code]], 
                          on=['time', 'sv'])
    
    merged_df = pd.merge(merged_df[['time', 'sv', l1_code, l5_code]], 
                         merged_dfs[['time', 'sv', l1s_code, l5s_code]], 
                         on=['time', 'sv'])

    merged_df = merged_df.sort_values(by=['time', 'sv']).reset_index(drop=True)

    # Extract receiver position to pass to the elevation calculator
    rx_position = obs.position if hasattr(obs, 'position') else None

    return merged_df, rx_position


# Computes slant TEC from inputted pseudorange measurements
def computeSlantTEC(L1_pseudorange, L5_pseudorange) -> float:
    tec = K * (L1_pseudorange-L5_pseudorange) 
    return tec

# Computes vertical TEC from slant TEC and satellite elevation
def computeVertTEC(sTEC: float, elevation: float):

    m = 1 / np.sqrt(1 - ((R * np.cos(np.radians(elevation))) /(R+H))**2)
    vTEC = sTEC / m

    return vTEC

#Adds slant TEC column to inputted DF
def genTECData(pseudorangeDF):
    pseudorangeDF['sTECp'] = computeSlantTEC(pseudorangeDF['C1'], pseudorangeDF['C5'])
    return pseudorangeDF

#Adds vertical TEC column to inputted DF
def genvTECData(sTECDF):
    sTECDF['vTECp'] = computeVertTEC(sTECDF['sTECp'], sTECDF['elevation'])
    return sTECDF


# --- Orbital Physics ---

#Computes satellite coordinates from a single broadcast ephemeris record
def compute_sv_ecef(ephem, t_obs):
    # Toe is stored as seconds into the GPS week (float), not a datetime
    toe_sec = float(ephem['Toe'].values)

    # Compute t_obs as GPS seconds-of-week for a consistent tk
    gps_epoch = pd.Timestamp('1980-01-06')
    t_obs_total = (pd.Timestamp(t_obs) - gps_epoch).total_seconds()
    tk = t_obs_total % 604800 - toe_sec

    # Handle week rollovers
    if tk > 302400:
        tk -= 604800
    elif tk < -302400:
        tk += 604800

    A = float(ephem['sqrtA'].values) ** 2
    n0 = np.sqrt(GM / A**3)
    n = n0 + float(ephem['DeltaN'].values)
    Mk = float(ephem['M0'].values) + n * tk

    Ek = Mk
    e = float(ephem['Eccentricity'].values)
    for _ in range(10):
        Ek = Mk + e * np.sin(Ek)

    vk = np.arctan2(np.sqrt(1 - e**2) * np.sin(Ek), np.cos(Ek) - e)
    Phik = vk + float(ephem['omega'].values)

    duk = float(ephem['Cuc'].values) * np.cos(2*Phik) + float(ephem['Cus'].values) * np.sin(2*Phik)
    drk = float(ephem['Crc'].values) * np.cos(2*Phik) + float(ephem['Crs'].values) * np.sin(2*Phik)
    dik = float(ephem['Cic'].values) * np.cos(2*Phik) + float(ephem['Cis'].values) * np.sin(2*Phik)

    uk = Phik + duk
    rk = A * (1 - e * np.cos(Ek)) + drk
    ik = float(ephem['Io'].values) + float(ephem['IDOT'].values) * tk + dik

    xkp = rk * np.cos(uk)
    ykp = rk * np.sin(uk)

    Omegak = float(ephem['Omega0'].values) + (float(ephem['OmegaDot'].values) - OMEGA_E) * tk - OMEGA_E * toe_sec

    X = xkp * np.cos(Omegak) - ykp * np.cos(ik) * np.sin(Omegak)
    Y = xkp * np.sin(Omegak) + ykp * np.cos(ik) * np.cos(Omegak)
    Z = ykp * np.sin(ik)

    return X, Y, Z


# --- SP3 Precise Ephemeris Support ---

def load_sp3(sp3_file):
    """
    Parse an SP3-c/d precise ephemeris file and return a dict:
        { sv_id : { 'times': np.ndarray[datetime64[ns]],
                    'xyz'  : np.ndarray[N, 3] in meters } }

    SP3 stores positions in kilometers; this function converts to meters.
    SP3 times are in GPS time. Position records starting with 'P' are used;
    velocity records ('V') are ignored.

    Satellite IDs are normalized to the RINEX-3 style (e.g. 'G01', 'R15',
    'E12') so they match the 'sv' values georinex produces.
    """
    print(f"Loading SP3 precise ephemeris file: {sp3_file}...")

    sats = {}
    current_time = None

    with open(sp3_file, 'r') as f:
        for line in f:
            if not line:
                continue
            tag = line[0]

            if tag == '*':
                # Epoch header: '*  YYYY MM DD HH MM SS.SSSSSSSS'
                parts = line[1:].split()
                if len(parts) < 6:
                    continue
                year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                hour, minute = int(parts[3]), int(parts[4])
                second = float(parts[5])
                sec_int = int(second)
                usec = int(round((second - sec_int) * 1e6))
                try:
                    current_time = pd.Timestamp(
                        year=year, month=month, day=day,
                        hour=hour, minute=minute, second=sec_int,
                        microsecond=usec
                    )
                except ValueError:
                    current_time = None

            elif tag == 'P' and current_time is not None:
                # Position record: 'PG01  X Y Z CLK ...' (km, km, km, microsec)
                sv_raw = line[1:4].strip()
                if len(sv_raw) < 2:
                    continue
                # Normalize: pad numeric part to 2 digits (e.g. 'G 1' -> 'G01')
                sys_char = sv_raw[0]
                num_str = sv_raw[1:].strip()
                if not num_str.isdigit():
                    continue
                sv_id = f"{sys_char}{int(num_str):02d}"

                try:
                    x_km = float(line[4:18])
                    y_km = float(line[18:32])
                    z_km = float(line[32:46])
                except ValueError:
                    continue

                # SP3 bad/missing position sentinel is 0.000000
                if x_km == 0.0 and y_km == 0.0 and z_km == 0.0:
                    continue

                rec = sats.setdefault(sv_id, {'times': [], 'xyz': []})
                rec['times'].append(np.datetime64(current_time))
                rec['xyz'].append([x_km * 1000.0, y_km * 1000.0, z_km * 1000.0])

    # Convert lists to numpy arrays, sorted by time
    for sv_id, rec in sats.items():
        times = np.array(rec['times'], dtype='datetime64[ns]')
        xyz = np.array(rec['xyz'], dtype=float)
        order = np.argsort(times)
        rec['times'] = times[order]
        rec['xyz'] = xyz[order]

    print(f"  Loaded {len(sats)} satellites from SP3.")
    return sats


def _lagrange_interp(t_nodes_s, vals, t_query_s):
    """
    Evaluate the Lagrange interpolating polynomial through (t_nodes_s, vals)
    at t_query_s. t_nodes_s is shape [N], vals is shape [N] or [N, K].
    Nodes are expected in seconds relative to a common reference.
    """
    n = len(t_nodes_s)
    result = np.zeros_like(vals[0], dtype=float) if vals.ndim > 1 else 0.0
    for i in range(n):
        # Build the i-th Lagrange basis value at t_query_s
        num = 1.0
        den = 1.0
        ti = t_nodes_s[i]
        for j in range(n):
            if j == i:
                continue
            tj = t_nodes_s[j]
            num *= (t_query_s - tj)
            den *= (ti - tj)
        Li = num / den
        result = result + Li * vals[i]
    return result


def interpolate_sp3_position(sp3_sats, sv, t_obs, order=SP3_LAGRANGE_ORDER):
    """
    Interpolate satellite ECEF position at t_obs using Lagrange interpolation
    over a window of SP3 nodes centered (as closely as possible) on t_obs.

    Returns (X, Y, Z) in meters, or None if sv not available or not enough
    surrounding nodes.
    """
    if sv not in sp3_sats:
        return None

    rec = sp3_sats[sv]
    times = rec['times']
    xyz = rec['xyz']
    n_pts = len(times)
    if n_pts == 0:
        return None

    # Use order+1 surrounding nodes (e.g. order 10 -> 11 points)
    window = order + 1
    window = min(window, n_pts)

    t_obs_np = np.datetime64(pd.Timestamp(t_obs))

    # Find insertion index, then pick a window centered on it
    idx = np.searchsorted(times, t_obs_np)
    half = window // 2
    start = idx - half
    end = start + window
    if start < 0:
        start = 0
        end = window
    if end > n_pts:
        end = n_pts
        start = end - window

    t_nodes = times[start:end]
    pts = xyz[start:end]

    # Convert times to seconds relative to the first node (avoids huge numbers
    # in the Lagrange formula, which can amplify floating-point error)
    t0 = t_nodes[0]
    t_nodes_s = (t_nodes - t0) / np.timedelta64(1, 's')
    t_query_s = (t_obs_np - t0) / np.timedelta64(1, 's')
    t_nodes_s = t_nodes_s.astype(float)
    t_query_s = float(t_query_s)

    xyz_interp = _lagrange_interp(t_nodes_s, pts, t_query_s)
    return float(xyz_interp[0]), float(xyz_interp[1]), float(xyz_interp[2])


# --- Broadcast ephemeris helpers (fallback path) ---

def _build_brdc_index(nav):
    """
    Pre-index the broadcast nav dataset into a plain dict keyed by sv.
    For each sv, store arrays of ephemeris times and the matching xarray
    indices. This avoids re-slicing the xarray Dataset on every observation.
    """
    print("Indexing broadcast ephemeris records...")
    brdc_index = {}
    for sv in nav.sv.values:
        sv_nav = nav.sel(sv=sv)
        sv_df = sv_nav.to_dataframe().dropna(how='all')
        if sv_df.empty:
            continue
        times = sv_df.index.get_level_values('time').unique().values
        times = np.sort(times)
        if len(times) == 0:
            continue
        brdc_index[sv] = times
    print(f"  Indexed {len(brdc_index)} satellites from broadcast nav.")
    return brdc_index


def _pick_brdc_ephem(nav, brdc_index, sv, t_obs):
    """
    Select the ephemeris record for sv whose Toe is closest to t_obs, but only
    if it falls within +/- BRDC_VALIDITY_HALF_WINDOW_S. Returns (ephem, dt_sec)
    where dt_sec is the absolute time offset used. Returns (None, None) if no
    record is within the validity window.

    This relaxes the old nearest-neighbor-no-matter-what behavior so we can
    tell the difference between "in-window, trustworthy" and "out-of-window,
    needs interpolation across the gap".
    """
    if sv not in brdc_index:
        return None, None

    valid_times = brdc_index[sv]
    t_np = np.datetime64(pd.Timestamp(t_obs))
    dts = np.abs(valid_times - t_np) / np.timedelta64(1, 's')
    k = int(np.argmin(dts))
    dt_sec = float(dts[k])

    if dt_sec > BRDC_VALIDITY_HALF_WINDOW_S:
        return None, dt_sec  # out of window

    ephem = nav.sel(sv=sv, time=valid_times[k])
    return ephem, dt_sec


def _bracketing_brdc_ephems(nav, brdc_index, sv, t_obs):
    """
    For observations that fall in a broadcast gap (> 2 hr from any Toe), return
    the two closest ephemeris records bracketing t_obs (one before, one after)
    so we can compute positions at each and Lagrange/linearly interpolate ECEF
    across the gap. Returns (ephem_before, t_before, ephem_after, t_after) with
    any missing side as (None, None).
    """
    if sv not in brdc_index:
        return None, None, None, None

    valid_times = brdc_index[sv]
    t_np = np.datetime64(pd.Timestamp(t_obs))

    before_mask = valid_times <= t_np
    after_mask = valid_times >= t_np

    ephem_before, t_before = None, None
    ephem_after, t_after = None, None

    if before_mask.any():
        t_before = valid_times[before_mask].max()
        ephem_before = nav.sel(sv=sv, time=t_before)
    if after_mask.any():
        t_after = valid_times[after_mask].min()
        ephem_after = nav.sel(sv=sv, time=t_after)

    return ephem_before, t_before, ephem_after, t_after


def _sat_ecef_from_brdc(nav, brdc_index, sv, t_obs):
    """
    Compute satellite ECEF at t_obs using broadcast ephemeris.

    Strategy (in order):
      1. If an ephemeris exists within +/- 2 hr of t_obs, use compute_sv_ecef
         with that ephemeris directly (this is the standard, high-accuracy
         path).
      2. Otherwise, find the bracketing ephemerides before and after t_obs,
         compute the satellite position at t_obs using each (propagating each
         ephem across the gap), and linearly interpolate between them weighted
         by time. This is a degraded-quality fallback for broadcast gaps.
      3. If no bracketing pair exists, return None.

    Returns ((X, Y, Z), quality_flag) where quality_flag is one of:
        'brdc'      - in-window broadcast ephemeris (best)
        'brdc_gap'  - interpolated across a broadcast gap (degraded)
        None        - no position available
    """
    ephem, dt = _pick_brdc_ephem(nav, brdc_index, sv, t_obs)
    if ephem is not None:
        try:
            x, y, z = compute_sv_ecef(ephem, t_obs)
            return (x, y, z), 'brdc'
        except Exception:
            pass  # fall through to gap handler

    ephem_b, t_b, ephem_a, t_a = _bracketing_brdc_ephems(
        nav, brdc_index, sv, t_obs
    )
    if ephem_b is None and ephem_a is None:
        return None, None

    # Compute each side's best estimate of sat position at t_obs
    pos_b = pos_a = None
    if ephem_b is not None:
        try:
            pos_b = np.array(compute_sv_ecef(ephem_b, t_obs))
        except Exception:
            pos_b = None
    if ephem_a is not None:
        try:
            pos_a = np.array(compute_sv_ecef(ephem_a, t_obs))
        except Exception:
            pos_a = None

    if pos_b is not None and pos_a is not None:
        # Linear blend weighted by temporal proximity of Toe on each side
        t_np = np.datetime64(pd.Timestamp(t_obs))
        dt_b = abs((t_np - t_b) / np.timedelta64(1, 's'))
        dt_a = abs((t_a - t_np) / np.timedelta64(1, 's'))
        total = dt_b + dt_a
        if total == 0:
            w_b, w_a = 0.5, 0.5
        else:
            # Closer side gets the larger weight
            w_b = dt_a / total
            w_a = dt_b / total
        pos = w_b * pos_b + w_a * pos_a
        return (float(pos[0]), float(pos[1]), float(pos[2])), 'brdc_gap'

    # Only one side available -- just use it, but mark as gap-quality
    pos = pos_b if pos_b is not None else pos_a
    return (float(pos[0]), float(pos[1]), float(pos[2])), 'brdc_gap'


# --- Main elevation routine ---

def add_elevations_to_df(df, nav_file, rx_position, sp3_file=None):
    """
    Add satellite elevation angles (degrees) to df.

    Ephemeris priority:
      1. If sp3_file is provided and valid, use Lagrange interpolation of
         precise SP3 positions. This is the recommended path for reference-
         quality comparisons (e.g. against NOAA-published data).
      2. Otherwise, use the broadcast nav file with a +/- 2 hr validity window
         and linear ECEF interpolation across any gaps longer than that.

    Also adds an 'elev_source' column so downstream code can tell which method
    produced each elevation ('sp3', 'brdc', 'brdc_gap', or 'none').
    """
    if rx_position is None:
        print("Warning: No receiver position found. Cannot compute elevations.")
        df['elevation'] = np.nan
        df['elev_source'] = 'none'
        return df

    rx_x, rx_y, rx_z = rx_position
    rx_lat, rx_lon, rx_alt = pm.ecef2geodetic(rx_x, rx_y, rx_z)

    # --- Path 1: SP3 precise ephemeris ---
    sp3_sats = None
    if sp3_file is not None and os.path.exists(sp3_file):
        try:
            sp3_sats = load_sp3(sp3_file)
        except Exception as e:
            print(f"  [WARN] Failed to load SP3 file {sp3_file}: {e}")
            sp3_sats = None
    elif sp3_file is not None:
        print(f"  [WARN] SP3 file {sp3_file} not found; falling back to broadcast.")

    # --- Path 2: Broadcast nav (always load for fallback) ---
    print(f"Loading RINEX NAV file: {nav_file}...")
    nav = gr.load(nav_file)
    brdc_index = _build_brdc_index(nav)

    print("Computing satellite elevations...")
    elevations = []
    sources = []
    counts = {'sp3': 0, 'brdc': 0, 'brdc_gap': 0, 'none': 0}

    for _, row in df.iterrows():
        t = row['time']
        sv = row['sv']
        el = np.nan
        source = 'none'
        sat_pos = None

        # Try SP3 first
        if sp3_sats is not None:
            sat_pos = interpolate_sp3_position(sp3_sats, sv, t)
            if sat_pos is not None:
                source = 'sp3'

        # Fall back to broadcast
        if sat_pos is None:
            print("Fall back")
            sat_pos, brdc_source = _sat_ecef_from_brdc(
                nav, brdc_index, sv, t
            )
            if sat_pos is not None:
                source = brdc_source  # 'brdc' or 'brdc_gap'

        # Convert ECEF to elevation if we have a position
        if sat_pos is not None:
            try:
                sat_x, sat_y, sat_z = sat_pos
                _, el, _ = pm.ecef2aer(sat_x, sat_y, sat_z, rx_lat, rx_lon, rx_alt)
            except Exception as e:
                print(f"  [ERROR] {sv} at {t}: {e}")
                el = np.nan
                source = 'none'

        elevations.append(float(el))
        sources.append(source)
        counts[source] = counts.get(source, 0) + 1

    df['elevation'] = elevations
    df['elev_source'] = sources

    total = len(elevations)
    print(f"\nElevation source summary ({total} rows):")
    for k in ('sp3', 'brdc', 'brdc_gap', 'none'):
        c = counts.get(k, 0)
        if total > 0:
            print(f"  {k:10s}: {c:6d}  ({100.0*c/total:5.1f}%)")
    return df


if __name__ == "__main__":
    # --- Configuration ---

    # Observation RINEX file
    OBS_FILE = "tn241150.26o" 

    # Navigation RINEX file (fallback source for elevations)
    NAV_FILE = "brdc1150.26n" 

    # Precise ephemeris SP3 file (optional; preferred when available).
    # Set to None to force broadcast-only mode.
    # Typical IGS filenames: igs22345.sp3 (final), igr22345.sp3 (rapid),
    # or the new long-form IGS0OPSFIN_yyyydddhhmm_01D_15M_ORB.SP3.
    SP3_FILE = "COD0OPSRAP_20261150000_01D_05M_ORB.SP3"  # e.g. "igs23100.sp3"
    
    # Code for L1, L5 pseudoranges and signal strength, current for rinex v2
    L1_OBS_CODE = 'C1' 
    L5_OBS_CODE = 'C5'
    L1_STRENGTH_CODE = 'S1'
    L5_STRENGTH_CODE = 'S5'
    
    #Generate pandas dataframe of time, satellites, and signal pseudoranges per sattelite. Also get receiver position
    df, rx_pos = get_l1_l5_pseudoranges(OBS_FILE, L1_OBS_CODE, L5_OBS_CODE, L1_STRENGTH_CODE, L5_STRENGTH_CODE)
    
    if df is not None and not df.empty:
        # Calculate Slant TEC
        df = genTECData(df)
        
        # Calculate Elevations (SP3-preferred, broadcast fallback)
        df = add_elevations_to_df(df, NAV_FILE, rx_pos, sp3_file=SP3_FILE)

        # Calculate Vertical TEC
        df = genvTECData(df)

        #Compute average vTEC at each timestamp, store to seperate pandas DF
        avg_vtec_df = df.groupby('time', as_index=False)['vTECp'].mean()
        avg_vtec_df.columns = ['time', 'avg_vTECp']
        
        print("\nSuccess! Final Dataset with TEC and Elevation:")
        print(df)
        
        # Save to CSV, all data csv and vertical TEC average across satellites csv
        df.to_csv('allReferenceData.csv', index=False)
        avg_vtec_df.to_csv('vTECAverageReferenceData.csv', index=False)

        # Plot average vTEC across satellites to time

        avg_vtec_df['time'] = pd.to_datetime(avg_vtec_df['time'])
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.scatter(avg_vtec_df['time'], avg_vtec_df['avg_vTECp'], color='purple', s=10)
        ax.set_ylabel('Average vTEC')
        ax.set_xlabel('Time')
        ax.set_title('Average vTEC Across All Satellites')
        fig.autofmt_xdate()
        plt.tight_layout()
        plt.show()

        # Plot sTEC and elevation for G28 satellite
        filtered_df = df.loc[df['sv'] == 'G28'].copy()
        filtered_df['time'] = pd.to_datetime(filtered_df['time'])

        if not filtered_df.empty:
            fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

            ax1.scatter(filtered_df['time'], filtered_df['sTECp'], color='blue', s=10)
            ax1.set_title('G28 sTEC and Elevation over Time')
            ax1.set_ylabel('sTEC (Raw)')

            ax2.scatter(filtered_df['time'], filtered_df['elevation'], color='orange', s=10)
            ax2.set_ylabel('Elevation (Degrees)')

            ax3.scatter(filtered_df['time'], filtered_df['vTECp'], color='green', s=10)
            ax3.set_ylabel('vTEC (Raw)')
            ax3.set_xlabel('Time')

            fig.autofmt_xdate()
            plt.tight_layout()
            plt.show()
        else:
            print("Satellite G28 not found in the filtered data for plotting.")

    else:
        print("\nNo overlapping L1 and L5 pseudorange data found in this file.")

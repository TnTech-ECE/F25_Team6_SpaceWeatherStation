Overview of folder:
  In this folder is the python program used to compute a set of reference TEC data we used to compare our measured data to.
  This program uses a RINEX observation file (.26o) for signal data and an emphemeris file (.sp3) for satellite elevations to compute TEC data.
  This program can also intake a RINEX navigation file (.26n) to compute satellite elevations, although .sp3 files are preferred.
  This folder outputs two .csv files. One contains all computed data. The other contains the average vTEC measurements of all satellites in the
  rinex files per timestamp.

Input files:
  RINEX observation file (.26o):
    - Contains signal data
  Emphemeris file (.sp3):
    - Contains location data for satellites
    - Used to compute elevation angle data
  RINEX navigation file (.26n):
    - Optional
    - Used to compute elevation angle data
      for satellites. Computationally dense.
      Only used if .sp3 file not complete

Program Output Files:
  allREferenceData.csv:
    - File containing all data generated from inputted files per timestamp per satellite.
      Includes signal pseudorange data, vTEC values, sTEC values, elevation angles, and signal strength values
  vTECAverageReferenceData.csv:
    - File containing average vTEC per timestamp. Average vTEC value is computed by averaging vTEC values of all
      satellites at a given timestamp.
    - Used in the compareTECDatav03.py program as the set of reference data.

Dependencies:
Make sure all relevant python libraries are installed on your device first. Required Python libraries are as follows:
  pandas
  numpy
  sys
  os
  warnings
  matplotlib.pyplot
  georinex
  pymap3d

Running Program:
To run this program, set the directories for the files you wish to use in lines 586, 589, and 595 in the main function.

File Header for more information:

File Name: TECFromRinex_OpusV1.py
Authors: Kenneth Creamer, Jackson Taylor
Last Updated: May 3, 2026
Purpose: Creates a set of vTEC and sTEC csv data from a rinex .26o file.
Input format: A .26o rinex obeservation file.
   Uses a .sp3 file for elevation angles preferably. Also intakes
   a rinex .26n file for elevation angle compuation fallback.
Output Files: a CSV of all computed data,
   and a seperate csv of average vTEC per timestamp, which is an average
   of all vTEC computations for all satellites at each timestamp.
   To set rinex files to be processed, change directory
   in lines 586, 589, and 595

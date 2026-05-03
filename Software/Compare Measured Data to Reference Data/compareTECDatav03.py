# File Name: compareTECDatav03.py
# Author: Jackson Taylor
# Last Updated: May 3, 2026
# Purpose: Intakes a set of measured and reference TEC data and runs a comparison between the two. Specifically compares
#   average vTEC measurements per timestamp. Computes error of measured compared to reference per timestamp, and plots
#   error. Also generates a comparison .csv file for all overlapping data points
# Format of input: Measured data set (.csv) must be in the format outputted by the Team6 Space Weather Station
#   data collection code (radioModulev3.py).
#   Reference data set (.csv) must be in format of vTEC average data set outputted by TECFromRinex_OpusV1.py.
# Outputs: Graph of reference data average vTEC and measured data average vTEC for overlapping timestamps.
#   Also graphs error per timestamp as well. Also computes mean bias error, mean absolute error, and error RMS.
#   Outputs .csv file of overlapping points and error valuess

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates

#Read in data, change directory to match your file names
referenceDataAvgvTEC = pd.read_csv('referenceData_2026_4_26.csv')
collectedData = pd.read_csv('gnss_log_04-25-2026_01-46PM.csv')

#Prints data to verify correct sets
print("Reference Data:")
print(referenceDataAvgvTEC)
print("Collected Data")
print(collectedData)

#Filter data points in collected data. Uncomment to further filter data how you'd like
collectedData = collectedData[collectedData['cno_db'] >= 30] #CNO filter
#collectedData = collectedData[collectedData['elevation_deg'] >= 20] #Elevation filter
#collectedData = collectedData[abs(collectedData['vTECp_tecu']) <= 150] #Filter for unrealistic values
#collectedData = collectedData[collectedData['vTECp_tecu'] > 0] # Filter for negative values
#collectedData = collectedData[collectedData['gnssId'] == 0] # Filter for GPS satellites specifically

#Compute average vTEC at each timestamp, store to seperate pandas DF
collectedDataAvgvTEC = collectedData.groupby('timestamp_utc', as_index=False)['vTECp_tecu'].mean()
collectedDataAvgvTEC.columns = ['time', 'measured_avg_vTECp']

#Rename column in referenceDataAvgvTEC
referenceDataAvgvTEC.columns = ['time', 'reference_avg_vTECp']

#Convert to UTC, round collected data to nearest second
collectedDataAvgvTEC['time'] = pd.to_datetime(collectedDataAvgvTEC['time'], utc=True).dt.round('s')
referenceDataAvgvTEC['time'] = pd.to_datetime(referenceDataAvgvTEC['time'], utc=True)

#Average vTEC values that might have same timestamp now in collected data from the rounding
collectedDataAvgvTEC = collectedDataAvgvTEC.groupby('time', as_index=False)['measured_avg_vTECp'].mean()

#Merge into new combined DF
comparisonDF = pd.merge(referenceDataAvgvTEC, collectedDataAvgvTEC, on=['time'])

#Compute error between measured and reference, store in DF
comparisonDF['vTECp_Error'] = comparisonDF['measured_avg_vTECp'] - comparisonDF['reference_avg_vTECp']

#compute mean bias error, mean absolute error, and root mean square error

meanAbsError = abs(comparisonDF['vTECp_Error']).mean()
meanBiasError = comparisonDF['vTECp_Error'].mean()
rmsError = ((comparisonDF['reference_avg_vTECp'] - comparisonDF['measured_avg_vTECp']) ** 2).mean() ** 0.5

print(f"Mean Absolute Error: {meanAbsError}")
print(f"Mean Bias Error: {meanBiasError}")
print(f"Root mean squared error: {rmsError}")

#Save to csv
comparisonDF.to_csv('vTEC_Comparison_Table.csv', index=False)

# Add column with CST 
comparisonDF['time_CST'] = comparisonDF['time'].dt.tz_convert('America/Chicago')
comparisonDF['measured_shifted_by_MBE'] = comparisonDF['measured_avg_vTECp'] - meanBiasError

#Create 2x2 figure with extra column for table
fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1], height_ratios=[0.2, 1, 1], figure=fig)

ax_table = fig.add_subplot(gs[0, :])  # spans both columns
ax1 = fig.add_subplot(gs[1, 0])
ax2 = fig.add_subplot(gs[1, 1])
ax3 = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[2, 1])

# Plot measured and reference data on same graph
ax1.scatter(comparisonDF['time_CST'], comparisonDF['measured_avg_vTECp'], color='blue', s=10, label='Measured')
ax1.scatter(comparisonDF['time_CST'], comparisonDF['reference_avg_vTECp'], color='orange', s=10, label='Reference')
ax1.legend(loc='lower right')
ax1.set_title('vTEC Measurements and Reference Values', fontweight='bold')
ax1.set_ylabel('vTEC (TECU)')

# Plot error
ax2.set_title('Error between Measured and Reference', fontweight='bold')
ax2.scatter(comparisonDF['time_CST'], comparisonDF['vTECp_Error'], color='green', s=10)
ax2.set_ylabel('Error (TECU)')

# Plot only reference values
ax3.set_title('Reference Values', fontweight='bold')
ax3.scatter(comparisonDF['time_CST'], comparisonDF['reference_avg_vTECp'], color='orange', s=10, label='Reference')
ax3.set_ylabel('vTEC (TECU)')
ax3.set_xlabel('Time (CST)')

# Plot only measured values
ax4.set_title('Measured Values (C/N0 >= 30 dBHz)', fontweight='bold')
ax4.scatter(comparisonDF['time_CST'], comparisonDF['measured_avg_vTECp'], color='blue', s=10, label='Measured (Filtered)')
ax4.set_ylabel('vTEC (TECU)')
ax4.set_xlabel('Time (CST)')

# Error metrics table
ax_table.axis('off')
table_data = [
    [f'Mean Abs. Error: {meanAbsError:.3f} TECU', f'Mean Bias Error: {meanBiasError:.3f} TECU', f'RMS Error: {rmsError:.3f} TECU']
]
table = ax_table.table(
    cellText=table_data,
    loc='center',
    cellLoc='center'
)

table.auto_set_font_size(True)
table.scale(1, 2.5)
ax_table.set_title('Error Metrics', fontweight='bold')

formatter = mdates.DateFormatter('%I:%M %p', tz=comparisonDF['time'].dt.tz)
ax1.xaxis.set_major_formatter(formatter)
ax2.xaxis.set_major_formatter(formatter)
ax3.xaxis.set_major_formatter(formatter)
ax4.xaxis.set_major_formatter(formatter)

fig.autofmt_xdate()

plt.tight_layout(h_pad=2)
plt.show()

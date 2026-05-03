Overview of folder:
  In this folder is the python script used to compare a set of measured TEC data to a set of reference TEC data.
  This python script outputs a graph of the reference average vTEC and measured average vTEC, and a graph of the error between the
  two with respect to timestamp. Only overlapping timestamps are graphed.
  Program also computes Mean Absoulte Error, Mean Bias Error, and Error RMS between the two data sets

Options:
  In the script, filters in the measured data can be added or removed by un-commenting or commenting out the lines 30-34,
  to the users discretion. By default, a filter to the mesured data of signal values being above 30dbHZ is used.
  These filters can be used to remove outliers in data

Input files:
  Measured Data (.csv):
    - Contains measured satellite signal data and TEC measurements
    - .csv must be in the format saved by the Space Weather Station Data Collection program
  Reference Data (.csv):
    - Contains average vTEC per timestamp from a set of reference RINEX data.
    - Must be in the format of the set of average vTEC data, "vTECAverageReferenceData.csv",
      outputted by the Reference Data Computation program described in this repository.
      Link to Reference Data Computation program:
      https://github.com/TnTech-ECE/F25_Team6_SpaceWeatherStation/blob/main/Software/Reference%20Data%20Computation/TECFromRinex_OpusV1.py

Program Output File:
  vTEC_Comparison_Table.csv:
    - .csv file containing a column of timestamps, a column of reference average vTEC values, a column of measured average vTEC values,
      and a column of the error between the measured and reference average vTEC values.
    - Only data of overlapping timestamps is used in this program (rounded to the nearest whole second), so make sure inputted data
      refers to an overlapping time period.

Program output graphs:
  Reference Data:
    - Plot of reference average vTEC values (yellow/orange)
    - Only plots values with timestamps overlapping with values in the measured dataset
  Measured Data:
    - Plot of measured average vTEC values (blue)
    - Only plots values with timestamps overlapping with values in the reference dataset
  Reference Data and Measured Data:
    - Plot of both measured and reference average vTEC values on the same graph
    - Only plots values with timestamps overlapping between the two datasets
  Error:
    - Plot of error between measured and reference average vTEC data (Measured - Reference) (green)
  Table of Error Statistics
    - Includes Mean Absoulte Error, Mean Bias Error, and Error RMS

Dependencies:
  Make sure all relevant python libraries are installed on your device first. Required Python libraries are as follows:
    pandas
    matplotlib.pyplot
    matplotlib.gridspec
    matplotlib.dates

Running Program:
  To run this program, set the directories for the files you wish to use in lines 20 and 21.
  Also, verify a modern version of python is installed. This program was written for python 3.
  To run the file, use the following:
  python3 compareTECDatav03.py

File Header for more information:

  File Name: compareTECDatav03.py
  Author: Jackson Taylor
  Last Updated: May 3, 2026
  Purpose: Intakes a set of measured and reference TEC data and runs a comparison between the two. Specifically compares
    average vTEC measurements per timestamp. Computes error of measured compared to reference per timestamp, and plots
    error. Also generates a comparison .csv file for all overlapping data points
  Format of input: Measured data set (.csv) must be in the format outputted by the Team6 Space Weather Station
    data collection code (radioModulev3.py).
    Reference data set (.csv) must be in format of vTEC average data set outputted by TECFromRinex_OpusV1.py.
  Outputs: Graph of reference data average vTEC and measured data average vTEC for overlapping timestamps.
    Also graphs error per timestamp as well. Also computes mean bias error, mean absolute error, and error RMS.
    Outputs .csv file of overlapping points and error valuess

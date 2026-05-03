Overview of folder:
  Folder of miscellaneous python scripts.

satGraph.py:
----------------------------------------------------------------------------------------------------------------------
Overview of File:
  Python script containing a function for graphing a set of satellites on a compass graph, with each the color of each point
  dependent on the sTEC value for that satellite. Could be modified to show vTEC values in set locations, potentially creating
  a rough heat map of TEC.

  Not implemented anywhere, core functionality finished but could be refined for a nicer output

Input:
  Dictionary of satellites of the form outputted by radioModulev3.py's getSatMeasurements function
Output:
  PIL Image of satellite compass graph, with each point's color relating to the satellite's sTEC value.

Dependencies:
  Python libraries:
    PIL
    math

File Header for more information:

  File Name: satGraph.py
  Author: Jackson Taylor
  Last Updated: May 3, 2026
  Purpose: Function file that creates a compass graph of
    slant TEC values per satellite. Intakes a dictionary
    of satellites, as outputted by radioModulev3.py's getSatMeasurements function.
    Outputs graph of satellite postion with reference to the receiver, with color
    associated with sTEC value
    Outputted data type is PIL Image

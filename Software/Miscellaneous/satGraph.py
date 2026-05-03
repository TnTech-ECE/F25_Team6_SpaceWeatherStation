# File Name: satGraph.py
# Author: Jackson Taylor
# Last Updated: May 3, 2026
# Purpose: Function file that creates a compass graph of
#   slant TEC values per satellite. Intakes a dictionary
#   of satellites, as outputted by radioModulev3.py's getSatMeasurements function.
#   Outputs graph of satellite postion with reference to the receiver, with color
#   associated with sTEC value
#   Outputted data type is PIL Image

from PIL import Image, ImageDraw
import math

# Parameters of graph
LINE_WIDTH = 3
LINE_WIDTH_SMALL = 1
MARGIN_WIDTH = 40
POINT_RADIUS = 4

def createGraph(sat_dic: dict, imWidth: int):

    imHeight = imWidth

    radius = (imHeight - MARGIN_WIDTH*2) / 2

    if(imWidth <=MARGIN_WIDTH):
        imWidth = MARGIN_WIDTH

    if(imHeight <=MARGIN_WIDTH):
        imHeight = MARGIN_WIDTH

    graph = Image.new('RGB', (imWidth, imHeight))

    draw = ImageDraw.Draw(graph)

    # Draw outer circle (0 degree elevation line)
    draw.ellipse([MARGIN_WIDTH, MARGIN_WIDTH, imWidth - MARGIN_WIDTH, imHeight - MARGIN_WIDTH], outline="lightgray", width=LINE_WIDTH)

    # Draw inner circle (45 degree elevation line)
    draw.ellipse([(imWidth - 2*MARGIN_WIDTH)*1/4 + MARGIN_WIDTH, (imHeight - 2*MARGIN_WIDTH)*1/4 + MARGIN_WIDTH, (imWidth - 2*MARGIN_WIDTH)*3/4 + MARGIN_WIDTH, (imHeight - 2*MARGIN_WIDTH)*3/4 + MARGIN_WIDTH], outline="lightgray", width=LINE_WIDTH_SMALL)

    # Draw cross
    draw.line([imWidth/2, MARGIN_WIDTH, imWidth/2, imHeight - MARGIN_WIDTH], fill="lightgray", width=LINE_WIDTH_SMALL)
    draw.line([MARGIN_WIDTH, imHeight/2, imWidth - MARGIN_WIDTH, imHeight/2], fill="lightgray", width=LINE_WIDTH_SMALL)

    # Draw cardinal directions

    draw.text([imWidth/2, MARGIN_WIDTH/2], 'N', fill= "lightgray", anchor='mm')
    draw.text([imWidth/2, imHeight - MARGIN_WIDTH/2], 'S', fill= "lightgray", anchor='mm')
    draw.text([MARGIN_WIDTH/2, imHeight/2], 'W', fill= "lightgray", anchor='mm')
    draw.text([imWidth - MARGIN_WIDTH/2, imHeight/2], 'E', fill= "lightgray", anchor='mm')

    # Iterate through satellites, plotting a point for each at its location dependent on its
    # elevation angle and azimuth angle
    for sat_key, info in sat_dic.items():

        x = radius * (90 - sat_dic[sat_key]['elevation']) / 90 * math.sin(sat_dic[sat_key]['azimuth'] * math.pi / 180) + imWidth / 2
        y = -1 * radius * (90 - sat_dic[sat_key]['elevation']) / 90 * math.cos(sat_dic[sat_key]['azimuth'] * math.pi / 180) + imHeight / 2

        color = "white"

        #Set color of point dependent on TEC value
        if "TECp" in info:
            if sat_dic[sat_key]['TECp'] < 10:
                color = "lime"
            elif sat_dic[sat_key]['TECp'] < 30:
                color = "yellowgreen"
            elif sat_dic[sat_key]['TECp'] < 50:
                color = "yellow"
            elif sat_dic[sat_key]['TECp'] < 70:
                color = "orange"
            else:
                color = "red"

        draw.circle([x, y], POINT_RADIUS, fill=color, outline=color, width=1)

    return graph

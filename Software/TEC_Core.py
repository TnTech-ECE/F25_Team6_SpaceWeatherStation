#Add shebang and make executable for Pi4B

#-----------------NOTES_START---------------------

#I have started coding this on my mac so the pi4B is not setup for any protcol.
#We will need to install several python libraries like pyserial and pyubx2

#-----------------NOTES_END-----------------------

import threading #enables us to read UART while processing Epochs
import serial 
from pyubx2 import UBXReader
import time
from collections import defaultdict
import spidev #https://pypi.org/project/spidev/
from datetime import datetime #uses computer's set timezone, https://docs.python.org/3/library/datetime.html


#-----------------INITS_START---------------------
#dictionary for epoch queue
epoch_list = defaultdict(dict)

#SPI for Pi4B and MCU communication
spi = spidev.SpiDev() #create a spi object
spi.open(1,0) #open spi bus 1, cs 0, needs to be configured on pi for SPI1
spi.max_speed_hz = 1_000_000 #not sure what this speed should be for pico and 4B


#-----------------INITS_END-----------------------

#-----------------FUNCTIONS_START-----------------
def ublox_UART_reader(): #using UART0 on Pi4B, Using GPIO 14 (TX) and GPIO 15 (RX)
    serial_port = "/dev/serial0" #ensure this is correct, points to the GPIO 14 and 15 pins
    baudrate = 115200 #match this baud rate to the ublox

    stream = serial.Serial(serial_port,baudrate,timeout=1) #what is a proper timeout value?
    ubr  UBXReader(stream)

    while True:
        (raw_data, parsed_data) = ubr.read() #parsed_data is a python object that has function calls

        if parsed_data is None: #if no serial input exit back to ubr.read
            continue
        if parsed_data.identity() == "RXM-RAWX": #RXM-RAWX is what we care about per epoch
            tow = parsed_data.rcvTow #this is used as a key for a dictionary to associate the proper satellites with TOWs

            for obs in parsed_data.obs: #parsed_data.obs is a list of all observations in one epoch 
                sv = obs.svId

                #store values in dictionary associated with tow and particular satellite
                epoch_list[tow][sv] = {
                    "L1": obs.carrierPhase,
                    "L2": obs.carrierPhase2,
                    "P1": obs.pseudorange,
                    "P2": obs.psuedorange2,
                    "CNO": obs.cno
                }
             
            
def processEpoch(): #consider a while True in this function
    for tow in list(epoch_list.keys()):
        epoch_data = epoch_list[tow]
        for sv, obs in epoch_data.items():

            #example--> obs["L1"] to get L1 phase as seen stored in epoch_list 
            slant_tec = compute_Slant_TEC() #arguments here will be needed
            vert_tec = compute_Vert_TEC(slant_tec)#idk if more arguments needed here
            scint = computeSCINT() #arguments needed here

            #timestamp send only hour and minute, send update to LoRa every minute
            now = datetime.now()
            hour = now.hour()
            minute = now.minute()
            
            TXandRX_MCU(hour,minute, sv, vert_tec) #this will return mag data and other sensor data
            storeInTXT() 
            
    del epoch_list[tow]
    
def compute_Slant_TEC():


def compute_Vert_TEC(slantTEC): #not sure what arguments here but may need more
    

def computeSCINT(): #stretch function, leave blank until others are working
    
    
def TXandRX_MCU(hour,minute,sv,vert_tec): 
    # each message must be 16 bytes or less, code so that each message is 16 bytes

    flags = 0 #no flags set
    extra = 0.0 #placeholder for 4 bytes all set to 0
    
    msg = struct.pack( #pack creates a binary representation of its arguments according to the format in the first arg
    "<BBBffB4x", #little enedian, hour,minute,sv,vert_tec,extrafloat,flags,4bytepad, https://docs.python.org/3/library/struct.html
    int(hour),
    int(minute),
    int(sv),
    float(vert_tec),
    float(extra),
    int(flags)
    )

    #full duplex xfer2 with cs held active, xfer2 returns the received message from slave, https://sigmdel.ca/michel/ha/rpi/dnld/draft_spidev_doc.pdf
    rx = spi.xfer2(list(msg))
    rx_bytes = bytes(rx)
    
    magx,magy,magz,temp = struct.unpack("<ffff",rx_bytes) #this is assuming four values returned all as floats

    return magx, magy, magz, temp


def storeInTXT():

#-----------------FUNCTIONS_END-----------------

#-----------------MAIN_START--------------------

if __name__=="__main__":
#threading enables multi-threading so ublox input is always working while TEC processing concurrently works
#daemon=True ensures that the thread ends when the full program ends
    threading.Thread(target=ublox_UART_reader,daemon=True).start()

    processEpoch()


#-----------------MAIN_END----------------------

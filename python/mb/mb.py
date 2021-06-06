#!/usr/bin/env python3
import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('COM9', 1)#, minimalmodbus.MODE_ASCII) #/dev/ttyUSB1', 1)  # port name, slave address (in decimal)

#instrument.serial.baudrate = 96004800#9600#2400#1200#9600
instrument.serial.bytesize = 7
instrument.serial.parity = serial.PARITY_EVEN#NONE#EVEN#ODD#EVEN #MARK#SPACE#NONE
instrument.serial.stopbits = 2
instrument.serial.dsrdtr = False
instrument.serial.rtscts = False

instrument.debug = True

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(100)#, 1)  # Registernumber, number of decimals
print(temperature)

## Change temperature setpoint (SP) ##
#NEW_TEMPERATURE = 95
#instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage

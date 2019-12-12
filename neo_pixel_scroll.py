#! /usr/bin/env python3

import serial
import time

ArduinoUnoSerial = serial.Serial('/dev/ttyACM0',9600) #change according to actual setup

def neo_pixel_print(message):
	return
	print("Sending neopixel message")
	bytez = message.encode('utf-16be')
	print("Finished converting bytes")
	print (ArduinoUnoSerial.readline()) #read a line from arduino
	ArduinoUnoSerial.write(bytez)   #write the message to the arduino
	print (ArduinoUnoSerial.readline()) #read a line from the arduino
	print("Finished sending message")

#neo_pixel_print("DIMBOT")
=======
import serial
import time
ArduinoUnoSerial = serial.Serial('/dev/ttyACM0',9600) #change according to actual setup

def neo_pixel_print(message):
    print ArduinoUnoSerial.readline() #read a line from arduino
    ArduinoUnoSerial.write(message)   #write the message to the arduino
    print ArduinoUnoSerial.readline() #read a line from the arduino


neo_pixel_print("DIMBOT")
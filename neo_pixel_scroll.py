import serial
import time
ArduinoUnoSerial = serial.Serial('/dev/ttyACM0',9600) #change according to actual setup

def neo_pixel_print(message):
    print ArduinoUnoSerial.readline() #read a line from arduino
    ArduinoUnoSerial.write(message)   #write the message to the arduino
    print ArduinoUnoSerial.readline() #read a line from the arduino


neo_pixel_print("DIMBOT")

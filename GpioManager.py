#! /usr/bin/env python3

# Handles the GPIO interface for the LED strip that helps signal to the 
# user when the robot is ready for interaction

import RPi.GPIO as GPIO

RED_PIN = 37  # 26
YELLOW_PIN = 35 # 19
YELLOWGREEN_PIN = 33 # 13
GREEN1_PIN = 31 #6
GREEN2_PIN = 29 #5


class GpioManager():

    def __init__(self):
        print("GPIO setup...")
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
        GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(YELLOWGREEN_PIN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GREEN1_PIN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GREEN2_PIN, GPIO.OUT, initial=GPIO.LOW)


    def ledON(self, group):
        if group == 0:
            GPIO.output(RED_PIN, GPIO.HIGH)
        if group == 1:
            GPIO.output(YELLOW_PIN, GPIO.HIGH)
        if group == 2:
            GPIO.output(YELLOWGREEN_PIN, GPIO.HIGH)
        if group == 3:
            GPIO.output(GREEN1_PIN, GPIO.HIGH)
        if group == 4:
            GPIO.output(GREEN2_PIN, GPIO.HIGH)    


    def ledOFF(self):
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(YELLOWGREEN_PIN, GPIO.LOW)
        GPIO.output(GREEN1_PIN, GPIO.LOW)
        GPIO.output(GREEN2_PIN, GPIO.LOW)    


gpioManager = GpioManager()
if __name__ == "__main__":  
    print("Running Bot Interaction tests")

if __name__ == "__main__":  
    print("Running Bot Interaction tests")
    gpioManager.ledON(1)

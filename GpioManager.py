#! /usr/bin/env python3

# Handles the GPIO interface for the LED strip that helps signal to the 
# user when the robot is ready for interaction

import RPi.GPIO as GPIO


def Setup(self):
	print("GPIO setup...")
	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BCM) # Use physical pin numbering
	GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
	GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(23,GPIO.OUT, initial=GPIO.LOW)

def RedOn():
    GPIO.output(23,GPIO.HIGH)

def RedOff():
    GPIO.output(23,GPIO.LOW)

def YellowOn():
    GPIO.output(15, GPIO.HIGH)

def YellowOff():
    GPIO.output(15,GPIO.LOW)

def GreenOn():
    GPIO.output(18, GPIO.HIGH) # Turn on

def GreenOff():
    GPIO.output(18, GPIO.LOW) # Turn off
    #sleep(1) # Sleep for 1 second


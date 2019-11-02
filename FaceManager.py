#! /usr/bin/env python3


'''	#################################################################################################
	
	DimBot FaceClass

	This class handles the movements for the face servos. It provides an interface for displaying
	varying emotional responses by the roboto

'''

import time
from ServoManager import *

# ======================= DEFINES ======================= #
RIGHT = 'Right'
LEFT = 'Left'





def FaceReset():
	EyebrowFlat(RIGHT)
	EyebrowFlat(LEFT)
	EyeOpen(RIGHT)
	EyeOpen(LEFT)
	EyeCenter()
	EyeMiddle()
	MouthClose()
	print("Reset is done")


def Excited():
	MouthOpen()
	EyebrowFlat(RIGHT)
	EyebrowFlat(LEFT)
	EyeMiddle()
	EyeOpen(RIGHT)
	EyeOpen(LEFT)
	time.sleep(2)
	FaceReset()
	print("Display excited expression")


def VeryHappy():
	MouthOpen()
	EyeUp()
	EyeOpen(RIGHT)
	EyeOpen(LEFT)
	EyebrowUp(RIGHT)
	EyebrowUp(LEFT)
	time.sleep(2)
	FaceReset()
	print("Display very happy expression")


def Sad():
	MouthClose()
	EyebrowFlat(RIGHT)
	EyebrowFlat(LEFT)
	EyeClose(RIGHT)
	EyeClose(LEFT)
	EyeDown()
	time.sleep(2)
	FaceReset()
	print("Display sad expression")


# blink both eyes
def Blink():
	i = 0
	MouthClose()
	EyebrowUp(RIGHT)
	EyebrowUp(LEFT)
	EyeOpen()

	while(i < 2):
		EyebrowDown(RIGHT)
		EyebrowDown(LEFT)
		EyeClose()
		time.sleep(0.3)
		EyebrowUp(RIGHT)
		EyebrowUp(LEFT)
		EyeOpen()
		time.sleep(0.3)
		i = i + 1	
		time.sleep(0.3)
	time.sleep(2)
	FaceReset()
	print("Blinking expression")


# Wink right eye
def WinkRight(): 
	for i in range(2):
		EyebrowUp(RIGHT)
		EyeOpen(RIGHT)
		time.sleep(0.5)
		EyebrowDown(RIGHT)
		EyeClose(RIGHT)
	EyebrowUp(RIGHT)
	EyeOpen(RIGHT)
	time.sleep(2)
	FaceReset()
	print("Wink right eye")


def Angry():
	MouthClose()
	EyeMiddle()
	EyebrowDown(RIGHT)
	EyebrowDown(LEFT)
	EyeLeft()
	time.sleep(1)
	EyeRight()
	time.sleep(1)
	EyeCenter()
	time.sleep(2)
	FaceReset()
	print("Display angry expression")


# ================================================================ #
if __name__ == "__main__":  
	print("Running face tests...")
	Face = FaceClass()

	Face.FaceReset()
	time.sleep(2)

	Face.Excited()
	time.sleep(2)

	Face.VeryHappy()
	time.sleep(2)

	Face.Sad()
	time.sleep(2)

	Face.Blink()
	time.sleep(2)

	Face.WinkRight()
	time.sleep(2)

	Face.Angry()
	time.sleep(2)
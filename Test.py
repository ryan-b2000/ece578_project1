#! /usr/bin/env python3

# Handles the main testing for the robot

from ServoManager import *
from ArmManager import *
from FaceManager import *


def MainTest():
	time.sleep(0.8)
	print("Running main test")
	
	# Reset everything
	FaceReset()
	ArmReset()

	# Test audio output
	PlayAudio('I am working on test my body! If my movement is not matched to my words, it means something is broken!')
	time.sleep(0.8)
	

	# Test All servos
	TestAllServos()
	time.sleep(1)
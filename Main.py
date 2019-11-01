#! /usr/bin/env python3



import copy
import cv2
import numpy as np
from keras.models import load_model
import pygame
import time
from keras.preprocessing import image
import os
from random import randint


import threading            #multithreading library

# NEW
###################################################################
import ArmClass
import FaceClass
import GameClass
import BotSpeak
import ImageProcessing
import SpeechRecognition
import GPIO
  

# ======================= DEFINES ======================= #
arms = ArmClass()       # initialize the object to manage the arms
face = FaceClass()      # initialize the object to manage the face 
game = GameClass()      # initialize the class to manage the game





# ================================================================ #
# ============================ MAIN ============================== #
# ================================================================ #
def Main():

    # Initialize servos, face, and arms
    face = FaceClass()
    arms = ArmClass()

    face.FaceReset()
    arms.ArmsReset()
    
    # Initialize OpenCV

    while (1):

    	# Indicate that we are ready for input from the user

    	# Get input from user and check for any keywords
    	validInput = False
    	while (validInput == False):
	    	user_input = DetectAudio()
	    	if (user_input == ""):
	    		print("Unable to get valid audio input...")
	    	else:
	    		music = KeywordCheck(user_input, 'music')
	    		flirt = KeywordCheck(user_input, 'flirt')
	    		happy = KeywordCheck(user_input, 'happy') 
	    		game = KeywordCheck(user_input, 'game')
	    		test = KeywordCheck(user_input, 'test')

    	# Handle the robot response based on the identified keywords
    	if (music):
    		PlayMusic()

    	elif (test):
    		MainTest()

    	elif (happy):
    		BotAction(EMOTION_HAPPY)

    	elif (game):
    		print("Play a game...")
    		PlayGame()

    	else:
    		BotAction(INVALID_ACTION)






# ================================================================ #
if __name__ == "__main__":  
    Main()
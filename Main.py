#! /usr/bin/env python3


# NEW
###################################################################
from BotInteraction import *
from human_detection import *
from ArmManager import arms
from FaceManager import face
from BotInteraction import *
from GameManager import game
from SpeechRecognition import speech
from Test import *
from human_detection import *

# ======================= DEFINES ======================= #
TEST = False

# ======================= GLOBAL VARIABLES ======================= #
do_music = False
do_flirt = False
do_game = False
do_test = False
do_happy = False



# ================================================================ #
# ============================ MAIN ============================== #
# ================================================================ #



	personcount = 0
	timecount = 0
	getPerson(personcount, timecount)
	# Initialize OpenCV



while 1:

    # Get input from user and check for any keywords
    validInput = False
    while validInput == False:
        
        if TEST:
            keyInput = input("Waiting for keyboard input... ")
            if keyInput == "music":
                do_music = True
            if keyInput == 'game':
                do_game = True
            if keyInput == 'flirt':
                do_flirt = True
            if keyInput == 'test':
                do_test = True
            if keyInput == 'happy':
                do_happy = True
            validInput = True

        else:
            # wait for a person to come to the window
            personcount = 0
            timecount = 0
            getPerson(personcount, timecount)

            # Indicate that we are ready for input from the user
            botReady()

            # Get the audio command from the user
            userInput = speech.detectAudio()
            
            # Determine if the user said one of the valid keywords
            if userInput == "":
                print("Unable to get valid audio input...")
                speak("I did not hear you. Please say again.")
            else:
                validInput = True
                do_music = speech.keywordCheck(userInput, 'music')
                do_flirt = speech.keywordCheck(userInput, 'flirt')
                do_happy = speech.keywordCheck(userInput, 'happy') 
                do_game = speech.keywordCheck(userInput, 'game')
                do_test = speech.keywordCheck(userInput, 'test')

    # Handle the robot response based on the identified keywords
    if do_music:
        botAction(ACTION_MUSIC)
        do_music = False

    elif test:
        MainTest()
        do_test = False

    elif happy:
        botAction(ACTION_HAPPY)
        do_happy = False

    elif do_game:
        game.playGame()
        do_game = False
        
    elif do_flirt:
        botAction(ACTION_FLIRT)
        do_flirt = False

    else:
        botAction(ACTION_INVALID)


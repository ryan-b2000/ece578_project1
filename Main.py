#! /usr/bin/env python3


# NEW
###################################################################
from ArmManager import *
from FaceManager import *
from GameManager import *
from BotInteraction import *
from SpeechRecognition import *
from Test import *

#import GpioManager

#import ImageProcessing


  

# ======================= DEFINES ======================= #
TEST = False

# ======================= GLOBAL VARIABLES ======================= #
music = False
flirt = False
game = False
test = False
happy = False



# ================================================================ #
# ============================ MAIN ============================== #
# ================================================================ #


# Initialize servos, face, and arms
FaceReset()
ArmReset()


# Initialize OpenCV

# Indicate that we are ready for input from the user
BotReady()

while (1):

    # Get input from user and check for any keywords
    validInput = False
    while (validInput == False):
        
        if (TEST):
            keyInput = input("Waiting for keyboard input... ")
            if (keyInput == "music"):
                music = True
            if (keyInput == 'game'):
                game = True
            if (keyInput == 'flirt'):
                flirt = True
            if (keyInput == 'test'):
                test = True
            if (keyInput == 'happy'):
                happy = True
            validInput = True

        else:
            # Get the audio command from the user
            userInput = DetectAudio()
            
            # Determine if the user said one of the valid keywords
            if (userInput == ""):
                print("Unable to get valid audio input...")
                Speak("I did not hear you. Please say again.")
            else:
                validInput = True
                music = KeywordCheck(userInput, 'music')
                flirt = KeywordCheck(userInput, 'flirt')
                happy = KeywordCheck(userInput, 'happy') 
                game = KeywordCheck(userInput, 'game')
                test = KeywordCheck(userInput, 'test')



    # Handle the robot response based on the identified keywords
    if (music):
        BotAction(ACTION_MUSIC)
        music = False

    elif (test):
        MainTest()
        test = False

    elif (happy):
        BotAction(ACTION_HAPPY)
        happy = False

    elif (game):
        PlayGame()
        game = False

    elif (flirt):
        BotAction(ACTION_FLIRT)
        flirt = False

    else:
        BotAction(ACTION_INVALID)




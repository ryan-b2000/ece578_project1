#! /usr/bin/env python3
import os

# NEW
###################################################################
from BotInteraction import *
from human_detection import *
from ArmManager import arms
from FaceManager import face
from BotInteraction import *
#from GameManager import game
from SpeechRecognition import speech
from Test import *
from human_detection import *
from game import *


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

personFlag = False
speakCount = 0



while 1:

    if personFlag == False:
        # wait for a person to come to the window
        personcount = 0
        timecount = 0
        getPerson(personcount, timecount)
        speak("Hello I am Dimbot. Can I show you what I can do?", "Intro.mp3")
        speak("Please say: music, game, happy, flirt, or test66", "Menu.mp3")
        personFlag = True
    else:
        userInput = ""
        # Get the audio command from the user
        # Indicate that we are ready for input from the user
        #justAudioOut("Ready.mp3")
        
        os.popen('arecord -D hw:1,0 -d 2 -f S16_LE --disable-channels -c 2 -r 44100 -t wav test')
        time.sleep(2)
        #userInput = speech.detectAudio()
        userInput = speech.transcribeFile()
   
        do_music = speech.keywordCheck(userInput, 'music')
        do_flirt = speech.keywordCheck(userInput, 'flirt')
        do_happy = speech.keywordCheck(userInput, 'happy') 
        do_game = speech.keywordCheck(userInput, 'game')
        do_test = speech.keywordCheck(userInput, 'test')

        # Handle the robot response based on the identified keywords
        if do_music:
            botAction(ACTION_MUSIC)
            do_music = False
            speak("I am ready for command", "Ready.mp3")

        elif do_test:
            MainTest()
            do_test = False
            speak("I am ready for command", "Ready.mp3")

        elif do_happy:
            botAction(ACTION_HAPPY)
            do_happy = False
            speak("I am ready for command", "Ready.mp3")

        elif do_game:
            main_game()
            do_game = False
            speak("I am ready for command", "Ready.mp3")
            
        elif do_flirt:
            botAction(ACTION_FLIRT)
            do_flirt = False
            speak("I am ready for command", "Ready.mp3")

        else:
            print("Bot Interaction: Invalid")
            speak("I do not understand the command.", "dont_understand.mp3")
            speakCount += 1
            
            if speakCount == 4:
                personFlag = False
                speakCount = 0



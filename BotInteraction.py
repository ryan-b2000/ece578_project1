#! /usr/bin/env python3

# Handles the human bot interactions
import os
import time
import threading
from ServoManager import *
from FaceManager import *
from ArmManager import *


# ============================================================================ #
ACTION_INVALID = 'Invalid'
ACTION_FLIRT = 'flirt'
ACTION_HAPPY = 'happy'
ACTION_MUSIC = 'music'
#Add this address after moving to PI
#MP3ADDRESS =

speakFlag = True
speakLock = threading.Lock()

# ============================================================================ #
def OutputSpeech(content, filename):
    print("Output speech: " + str(content))
    global speakFlag
    speakFlag = True
    text = str(content)
    f = str(filename)
    #os.popen( 'espeak -s 110 "'+text+'" --stdout | aplay 2>/dev/null')

    #TEST THIS
    os.popen( 'mpg321 "'+MP3ADDRESS+'""'+f+'" ')

    # Calculate the length of the speech and go to sleep while talking
    #print("Text length: " + str(len(text)))
    time.sleep(len(text) * 0.1)
    # Set the flag to stop the mouth from moving
    speakLock.acquire(blocking=True)
    speakFlag = False
    speakLock.release()
    #print("Flag set to false")


# ============================================================================ #
def TalkingMouth():
    print("Moving mouth...")
    global speakFlag
    while (True):
        # Do the mouth movement
        MouthOpen()
        time.sleep(0.6)
        MouthClose()
        time.sleep(0.6)
        # Check if the flag was set by other thread
        #print("Trying to acquire flag")
        speakLock.acquire()
        if (speakFlag == False):
            #print("Flag is false")
            break
        speakLock.release()
    speakLock.release()


# ============================================================================ #
def Speak(content, mp3):
    # Use multithreading library named threading
    mouth = threading.Thread(target=OutputSpeech, args=(content, mp3))
    voice = threading.Thread(target=TalkingMouth)
    mouth.start()
    voice.start()
    mouth.join()
    voice.join()
    print("Finished speaking function")


# ============================================================================ #
def BotReady():
    print("Bot Interaction: Ready")
    Speak("I am ready for your command.", "Ready.mp3")
    time.sleep(2)


# ============================================================================ #
def BotWinner():
    print("Bot Interaction: Game Winner")
    Speak("I am the winner!", "I_win.mp3")
    VeryHappy()
    BangDrumLeft()
    BangDrumRight()
    BangDrumBoth()


# ============================================================================ #
def BotLoser():
    print("Bot Interaction: Game Loser")
    Speak("You are the winner!", "You_win.mp3")
    Sad()
    ArmReset()


# ============================================================================ #
def BotTied():
    print("Bot Interaction: Game Tied")
    Speak("We tied the game.", "Tie.mp3")
    ArmReset()
    FaceReset()


# ============================================================================ #
def PlayMusic():
    print("Bot Interaction: Playing music")
    Speak("Look at me playing music!", "Playing_music.mp3")
    BangDrumLeft()
    BangDrumLeft()
    BangDrumRight()
    BangDrumBoth()


# ============================================================================ #
def Flirt():
    print("Bot Interaction: Flirt")
    Speak("Well. Hello there, good looking.", "Flirt.mp3")
    WinkRight()


# ============================================================================ #
def BotAction(type):
    # Display a happy emotion
    if (type == ACTION_MUSIC):
        PlayMusic()

    if (type == ACTION_HAPPY):
        Speak("I am very happy!", "Happy.mp3")
        VeryHappy()

    if (type == ACTION_FLIRT):
        Flirt()

    if (type == ACTION_INVALID):
        print("Bot Interaction: Invalid")
        Speak("I do not understand the command.", "Don't_understand.mp3")
        time.sleep(1)
        Speak("Please say: music, game, happy, flirt, or test")



# ============================================================================ #
def TestSpeech():
    text = 0
    while(text != 'e'):
        text = input("I am testing my speech!", "Speech_test.mp3")
        Speak(text)


# ============================================================================ #
if __name__ == "__main__":
    print("Running speech testing")

    # Test
    TestSpeech()

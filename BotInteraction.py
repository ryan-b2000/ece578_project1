#! /usr/bin/env python3

# Handles the human bot interactions
import os
import time
import threading
from ServoManager import *
from FaceManager import *
from ArmManager import *


# ============================================================================ #
TalkFlag = 1
condition = threading.Condition()

def OutputSpeech(content):
	print("Output speech: " + str(content))
	global TalkFlag
	text = str(content)
	os.popen( 'espeak -s 110 "'+text+'" --stdout | aplay 2>/dev/null')
	time.sleep(1)
	condition.acquire()
	TalkFlag = 0
	condition.release()

def TalkingMouth():
	print("Moving mouth...")
	global TalkFlag
	
	while (True):
		condition.acquire()
		if (TalkFlag == 1):
			MouthOpen()
			time.sleep(0.6)
			MouthClose()
			time.sleep(0.6)
		else:
			break
		condition.release()

def Speak(content):
	# Use multithreading library named threading
	mouth = threading.Thread(target=OutputSpeech, args=(content,))
	voice = threading.Thread(target=TalkingMouth)
	mouth.start()
	voice.start()
	mouth.join()
	voice.join()
	print("Finished speaking function")



# ============================================================================ #
def BotReady():
	print("Bot Interaction: Ready")
	Speak("I am ready for your command.")


def BotWinner():
	print("Bot Interaction: Game Winner")
	Speak("I am the winner!")
	VeryHappy()
	BangDrumLeft()
	BangDrumRight()
	BangDrumBoth()


def BotLoser():
	print("Bot Interaction: Game Loser")
	Speak("You are the winner!")
	Sad()
	ArmReset()


def BotTied():
	print("Bot Interaction: Game Tied")
	Speak("We tied the game.")
	ArmReset()
	FaceReset()
	



# ============================================================================ #
def PlayMusic():
	print("Bot Interaction: Playing music")


# ============================================================================ #
def BotAction(type):
	# Display a happy emotion
	if (type == "Happy"):
		print("Bot Interaction: Happy")
		VeryHappy()

	if (type == INVALID_ACTION):
		print("Bot Interaction: Invalid")


def TestSpeech():
	text = 0
	while(text != 'e'):
		text = input("What to say? ")
		Speak(text)


# ============================================================================ #
if __name__ == "__main__":  
	print("Running speech testing")

	# Test 
	TestSpeech()
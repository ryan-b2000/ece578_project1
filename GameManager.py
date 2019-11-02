#! /usr/bin/env python3

# Manages the rock, paper, scissors game

import time
from BotInteraction import *
from ArmClass import ArmClass

WINNER = 'winner'
LOSER = 'loser'
TIE = 'tie'

PAPER = 'paper'
ROCK = 'rock'
SCISSORS = 'scissors'


# ============================================================================ #
# Generate the rock/paper/scissors gesture the robot uses for the game	

def GenerateGesture():
    index = randint(0,2)
    if (index == 0):
        return PAPER
    elif (index == 1):
        return ROCK
    else:
        return SCISSORS


# ============================================================================ #
# Take input of robot and user gesture
# Return the user result: if the user won, lost, or tied

def GameResult(bot, user):
    if user == PAPER:
    	if bot == PAPER:
    		print("Result: Paper - Paper")
    		return TIE
    	elif bot == ROCK:
    		print("Result: Paper - Rock")
    		return WINNER
    	else:
    		print("Result: Paper - Scissors")
    		return LOSER

    if user == ROCK:
    	if bot == PAPER:
    		print("Result: Rock - Paper")
    		return LOSER
    	elif bot == ROCK:
    		print("Result: Rock - Rock")
    		return TIE
    	else:
    		print("Result: Rock - Scissors")
    		return WINNER

    if user == SCISSORS:
    	if bot == PAPER:
    		print("Result: Scissors - Paper")
    		return WINNER
    	elif bot == ROCK:
    		print("Result: Scissors - Rock")
    		return LOSER
    	else:
    		print("Result: Scissors - Scissors")
    		return TIE


# ============================================================================ #
def PlayGame():
	print("Playing game...")

	# Do countdown for the user
	print("Ready?...")
	Speak("Ready?")
	BangDrumBoth()

	print("Rock...")
	Speak("Rock")
	BangDrumBoth()

	print("Paper...")
	Speak("Paper")
	BangDrumBoth()

	print("Scissors...")
	Speak("Scissors")
	BangDrumBoth()

	print("Go!")
	Speak("Go!")
	BangDrumBoth()

	# Get gesture from the user
	user_gesture = ROCK

	# Calculate robot gesture and determine winner
	bot_gesture = GenerateGesture()
	result = GameResult(bot_gesture, user_gesture)

	if (result == WINNER):
		print("User is the winner")
	if (result == LOSER):
		print("User is the loser")
	else:
		print("User and robot tied")

	# Reset the robot servos
	ArmReset()
	FaceReset()
	time.sleep(2)

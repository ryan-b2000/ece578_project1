#! /usr/bin/env python3

# Manages the rock, paper, scissors game

import time
from random import randint
from BotInteraction import *
from ArmManager import *
from neo_pixel_scroll import *

WINNER = 'winner'
LOSER = 'loser'
TIE = 'tie'

PAPER = 'paper'
ROCK = 'rock'
SCISSORS = 'scissors'
STUPID = True

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
	print("        USER -  BOT")
	if user == PAPER:
		if bot == PAPER:
			print("Result: Paper - Paper")
			neo_pixel_print("PAPER")
			return TIE	   
		elif bot == ROCK:
			print("Result: Paper - Rock")
			neo_pixel_print("ROCK")
			return WINNER
		else:
			print("Result: Paper - Scissors")
			neo_pixel_print("SCISSORS")
			return LOSER

	if user == ROCK:
		if bot == PAPER:
			print("Result: Rock - Paper")
			neo_pixel_print("PAPER")
			return LOSER
		elif bot == ROCK:
			print("Result: Rock - Rock")
			neo_pixel_print("ROCK")
			return TIE
		else:
			print("Result: Rock - Scissors")
			neo_pixel_print("SCISSORS")
			return WINNER


	if user == SCISSORS:
		if bot == PAPER:
			print("Result: Scissors - Paper")
			neo_pixel_print("PAPER")
			return WINNER
		elif bot == ROCK:
			print("Result: Scissors - Rock")
			neo_pixel_print("ROCK")
			return LOSER
		else:
			print("Result: Scissors - Scissors")
			neo_pixel_print("SCISSORS")
			return TIE




# ============================================================================ #
def PlayGame():
	print("Playing game...")
	Speak("OK. Let's play rock paper scissors.")
	time.sleep(0.5)

	# Do countdown for the user
	print("Ready?...")
	Speak("Ready?")
	neo_pixel_print("READY?")
	BangDrumBoth()
	time.sleep(2)

	print("Rock...")
	Speak("Rock")
	BangDrumBoth()
	time.sleep(2)

	print("Paper...")
	Speak("Paper")
	BangDrumBoth()
	time.sleep(2)

	print("Scissors...")
	Speak("Scissors")
	BangDrumBoth()
	time.sleep(2)

	print("Go!")
	Speak("Go!")
	neo_pixel_print("GO!")
	BangDrumBoth()
	time.sleep(2)

	# Get gesture from the user
	user_gesture = ROCK # Testing

	# Calculate robot gesture and determine winner
	bot_gesture = GenerateGesture()
	result = GameResult(bot_gesture, user_gesture)

	if (result == WINNER):
		print("User is the winner")
		neo_pixel_print("WINNER!")
		BotWinner()

	if (result == LOSER):
		print("User is the loser")
		neo_pixel_print("LOSER!")
		BotLoser()
	else:
		print("User and robot tied")
		neo_pixel_print("TIE!")
		BotTied()

	# Reset the robot servos
	ArmReset()
	FaceReset()
	time.sleep(3)


#! /usr/bin/env python3

# Manages the rock, paper, scissors game

import time
from random import randint
from BotInteraction import bot
from ArmManager import arms
from FaceManager import face
#from neo_pixel_scroll import *

WINNER = 'winner'
LOSER = 'loser'
TIE = 'tie'

PAPER = 'paper'
ROCK = 'rock'
SCISSORS = 'scissors'
STUPID = True



class GameManager():

	def __init__(self):
		print("Game Manager initialized")


	# ============================================================================ #
	# Generate the rock/paper/scissors gesture the robot uses for the game  
	def generateGesture(self):
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

	def gameResult(self, bot, user):
		print("        USER -  BOT")
		if user == PAPER:
			if bot == PAPER:
				print("Result: Paper - Paper")
				#neo_pixel_print("PAPER")
				return TIE	   
			elif bot == ROCK:
				print("Result: Paper - Rock")
				#neo_pixel_print("ROCK")
				return WINNER
			else:
				print("Result: Paper - Scissors")
				#neo_pixel_print("SCISSORS")
				return LOSER

		if user == ROCK:
			if bot == PAPER:
				print("Result: Rock - Paper")
				#neo_pixel_print("PAPER")
				return LOSER
			elif bot == ROCK:
				print("Result: Rock - Rock")
				#neo_pixel_print("ROCK")
				return TIE
			else:
				print("Result: Rock - Scissors")
				#neo_pixel_print("SCISSORS")
				return WINNER


		if user == SCISSORS:
			if bot == PAPER:
				print("Result: Scissors - Paper")
				#neo_pixel_print("PAPER")
				return WINNER
			elif bot == ROCK:
				print("Result: Scissors - Rock")
				#neo_pixel_print("ROCK")
				return LOSER
			else:
				print("Result: Scissors - Scissors")
				#neo_pixel_print("SCISSORS")
				return TIE


	# ============================================================================ #
	def playGame(self):
		print("Playing game...")
		bot.speak("OK. Let's play rock paper scissors.")
		time.sleep(0.5)

		# Do countdown for the user
		print("Ready?...")
		bot.speak("Ready?")
		#neo_pixel_print("READY?")
		arms.bangDrumBoth()
		time.sleep(2)

		print("Rock...")
		bot.speak("Rock")
		arms.bangDrumBoth()
		time.sleep(2)

		print("Paper...")
		bot.speak("Paper")
		arms.bangDrumBoth()
		time.sleep(2)

		print("Scissors...")
		bot.speak("Scissors")
		arms.bangDrumBoth()
		time.sleep(2)

		print("Go!")
		bot.speak("Go!")
		#neo_pixel_print("GO!")
		arms.bangDrumBoth()
		time.sleep(2)

		# Get gesture from the user
		user_gesture = ROCK # Testing

		# Calculate robot gesture and determine winner
		bot_gesture = self.generateGesture()
		result = self.gameResult(bot_gesture, user_gesture)

		if (result == WINNER):
			print("User is the winner")
			#neo_pixel_print("WINNER!")
			bot.botWinner()

		if (result == LOSER):
			print("User is the loser")
			#neo_pixel_print("LOSER!")
			bot.botLoser()
		else:
			print("User and robot tied")
			#neo_pixel_print("TIE!")
			bot.botTied()

		# Reset the robot servos
		arms.reset()
		face.reset()
		time.sleep(3)
		print("Finished playing game")


# Create single of the face class to import elsewhere
game = GameManager()

# ============================================================================ #
if __name__ == "__main__":
	print("Doing Game Manager test")
	game.playGame()
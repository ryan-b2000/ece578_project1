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


	def take_image(self):
	    cam = cv2.VideoCapture(0)
	    i = 0
	    start = datetime.now()
	    while True:
	        s, im = cam.read()  # captures image
	        #gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	        cv2.imshow('frame',im)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	        ends = datetime.now()
	        duration = ends - start
	        if duration.total_seconds() > 5:
	            break
	    cv2.imwrite('/home/pi/Desktop/ece578_project1/images/3.jpg', im)
	    cam.release()
	    cv2.destroyAllWindows()

	# ============================================================================ #
	# Generate the rock/paper/scissors gesture the robot uses for the game  
	def generateGesture(self):
		gesture = ['rock', 'paper', 'scissors']
    	index = random.randint(0, 2)
    	return gesture[index]


	# ============================================================================ #
	# Take input of robot and user gesture
	# Return the user result: if the user won, lost, or tied

	def gameResult(self, bot, user):
		print("        USER -  BOT")
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
	def playGame(self):
		print("Playing game...")
		speak("OK. Let's play rock paper scissors.", "RPC.mp3")
		time.sleep(0.5)

		# Do countdown for the user
		print("Ready?...")
		speak("Ready?", "ready.mp3")
		time.sleep(1)

		print("Rock...")
		speak("Rock", "rock.mp3")
		time.sleep(1)

		print("Paper...")
		speak("Paper", "paper.mp3")
		time.sleep(1)

		print("Scissors...")
		speak("Scissors", "scissors.mp3")
		time.sleep(1)

		print("Go!")
		speak("Go!", "go.mp3")
		time.sleep(1)

		# Get the user gesture
		user_gest = "unknown"
		while user_gest != 'rock' and user_gest != 'paper' and user_gest != 'scissors':
	    	take_image()
	    	user_gest = get_gesture()
	    	print("User gesture: " + user_gest)
	    	if user_gest != 'rock' and user_gest != 'paper' and user_gest != 'scissors':
	    		print("Bot Confused")
	    		speak("Please try again.")

		# Calculate robot gesture and determine winner
		bot_gesture = self.generateGesture()
		result = self.gameResult(bot_gesture, user_gest)

		if (result == WINNER):
			print("User is the winner")
			botWinner()

		if (result == LOSER):
			print("User is the loser")
			botLoser()
		else:
			print("User and robot tied")
			botTied()

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
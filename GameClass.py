#! /usr/bin/env python3

PAPER = 'paper'
ROCK = 'rock'
SCISSORS = 'scissors'

# Manages the rock, paper, scissors game
class GameClass:

	def __init__ (self):
		print("Gameclass initialized")
		self.gesture = PAPER

	# Generate the rock/paper/scissors gesture the robot uses for the game	
	def GenerateGesture(self):
	    index = randint(0,2)
	    if (index == 0):
	        self.gesture = PAPER
	    elif (index == 1):
	        self.gesture = ROCKs
	    else:
	        self.gesture = SCISSORS

	# Determine who won the game based on the gesture from the user and the
	# gesture for the robot
	def GameResult(self, user):
	    if user == PAPER:
	    	if self.gesture == PAPER:
	    		print("Result: Paper - Paper")
	    		return TIE
	    	elif self.gesture == ROCK:
	    		print("Result: Paper - Rock")
	    		return WINNER
	    	else:
	    		print("Result: Paper - Scissors")
	    		return LOSER

	    if user == ROCK:
	    	if self.gesture == PAPER:
	    		print("Result: Rock - Paper")
	    		return LOSER
	    	elif self.gesture == ROCK:
	    		print("Result: Rock - Rock")
	    		return TIE
	    	else:
	    		print("Result: Rock - Scissors")
	    		return WINNER

	    if user == SCISSORS:
	    	if self.gesture == PAPER:
	    		print("Result: Scissors - Paper")
	    		return WINNER
	    	elif self.gesture == ROCK:
	    		print("Result: Scissors - Rock")
	    		return LOSER
	    	else:
	    		print("Result: Scissors - Scissors")
	    		return TIE

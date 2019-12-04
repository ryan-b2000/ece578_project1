#! /usr/bin/env python3


# NEW
###################################################################
from ArmManager import *
from FaceManager import *
from GameManager import *
#import GpioManager
from BotInteraction import *
#import ImageProcessing
import SpeechRecognition
from human_detection import *
  

# ======================= DEFINES ======================= #




# ================================================================ #
# ============================ MAIN ============================== #
# ================================================================ #
def Main():

	# Initialize servos, face, and arms
	FaceReset()
	ArmReset()

	personcount = 0
	timecount = 0
	getPerson(personcount, timecount)
	# Initialize OpenCV

	while (1):

		# Indicate that we are ready for input from the user
		BotReady()

		# Get input from user and check for any keywords
		validInput = False
		while (validInput == False):
			user_input = DetectAudio()
			if (user_input == ""):
				print("Unable to get valid audio input...")
			else:
				music = KeywordCheck(user_input, 'music')
				flirt = KeywordCheck(user_input, 'flirt')
				happy = KeywordCheck(user_input, 'happy') 
				game = KeywordCheck(user_input, 'game')
				test = KeywordCheck(user_input, 'test')

		# Handle the robot response based on the identified keywords
		if (music):
			arms.PlayMusic()

		elif (test):
			MainTest()

		elif (happy):
			BotAction(EMOTION_HAPPY)

		elif (game):
			print("Play a game...")
			PlayGame()

		else:
			BotAction(INVALID_ACTION)






# ================================================================ #
if __name__ == "__main__":  
	Main()

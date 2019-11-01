#! /usr/bin/env python3

# Handles the human bot interactions


def PlayMusic():
	print("Playing music...")


def BotAction(type):
	# Display a happy emotion
	if (type == "Happy"):
		print("Showing happy emotion...")

	if (type == INVALID_ACTION):
		print("Unable to determine user command...")
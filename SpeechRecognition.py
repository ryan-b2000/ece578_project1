#! /usr/bin/env python3

# Handles the speech recognition capabilities

import re
import speech_recognition as sr

VOICE_COMMAND_MUSIC     = "music"
VOICE_COMMAND_FLIRT     = "flirt"
VOICE_COMMAND_HAPPY     = "happy"
VOICE_COMMAND_GAME      = "game"
VOICE_COMMAND_TEST      = "test"
VOICE_COMMAND_INVALID   = "invalid"

# =================================================================================================== #
# Detect audio in through microphone
#
# Start a speech recognizer and listen for speech. This uses Googles cloud speech recognition
# Return back the  string of text

def DetectAudio():
    
    print("Detecting audio...")
    
    #USE_RECOGNIZER = 'Google'
    USE_RECOGNIZER = 'Sphinx'

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source,phrase_time_limit=2)
 
        if (USE_RECOGNIZER == 'Google'):
            # Speech recognition using Google Speech Recognition                                                                                         
            try:
                input_speech = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                input_speech = ""
                print("Google Speech Recognition could not understand audio")
                pass
            except sr.RequestError as e:
                input_speech = ""
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                pass

        else:
            # recognize speech using Sphinx
            try:
                input_speech = recognizer.recognize_sphinx(audio)
                print("Sphinx thinks you said " + input_speech)
            except sr.UnknownValueError:
                input_speech = ""
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                input_speech = ""
                print("Sphinx error; {0}".format(e))

    return input_speech


# =================================================================================================== #
# Check text for a specific keyword
#
# Use RegEx to parse the string and look for a certain word
# Return true if the test word is in the input speech string
# Return false otherwise

def KeywordCheck(input_speech, test):
    
    if (test == VOICE_COMMAND_MUSIC):
        regexp = re.compile(r'music')
    elif (test == VOICE_COMMAND_FLIRT):
        regexp = re.compile(r'flirt')
    elif (test == VOICE_COMMAND_HAPPY):    
        regexp = re.compile(r'happy')
    elif (test == VOICE_COMMAND_GAME):    
        regexp = re.compile(r'game')
    elif (test == VOICE_COMMAND_TEST):
        regexp = re.compile(r'test')
    else:
        return False

    if (regexp.search(input_speech)):
        return True

    return False


# =================================================================================================== #
# Test Audio Detection

def TestAudioDetection():
    exit = 1
    while (exit != 'e'):
        print("Testing audio detection...")
        text = DetectAudio()
        print("Speech was " + text)
        exit = input("Exit? ")

def TestKeywordCheck():
    print("Testing Keyword Check...")
    
    string = 'the music car is loud'
    print("String: " + string)    
    
    print("Check for 'music'")
    if (KeywordCheck(string, 'music')):
        print("PASS Match found")
    else:
        print("FAIL No match found")

    print("Check for 'brown'")
    if (KeywordCheck(string, 'brown')):
        print("FAIL Match found")
    else:
        print("PASS No match found")


# ================================================================ #
if __name__ == "__main__":  
    TestAudioDetection()
    #TestKeywordCheck()
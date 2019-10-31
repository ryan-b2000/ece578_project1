#! /usr/bin/env python3

# Handles the speech recognition capabilities

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
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source,phrase_time_limit=5)
 
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

    return input_speech


# =================================================================================================== #
# Check text for a specific keyword
#
# Use RegEx to parse the string and look for a certain word

def keyword_check(input_speech):
    
    music_regexp = re.compile(r'music')
    flirt_regexp = re.compile(r'flirt')
    happy_regexp = re.compile(r'happy')
    game_regexp = re.compile(r'game')
    test_regexp = re.compile(r'test')

    if music_regexp.search(input_speech):
        return VOICE_COMMAND_MUSIC

    if flirt_regexp.search(input_speech):
        return VOICE_COMMAND_FLIRT

    if happy_regexp.search(input_speech):
        return VOICE_COMMAND_HAPPY

    if game_regexp.search(input_speech):
        return VOICE_COMMAND_GAME

    if test_regexp.search(input_speech):
        return VOICE_COMMAND_TEST
    
    return VOICE_COMMAND_INVALID


# =================================================================================================== #
# Test Audio Detection

def TestAudioDetection():
    print("Testing audio detection...")
    text = DetectAudio()
    print("Speech was " + text)
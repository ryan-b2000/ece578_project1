#! /usr/bin/env python3

# Handles the speech recognition capabilities

import re
import speech_recognition as sr
from os import path

VOICE_COMMAND_MUSIC     = "music"
VOICE_COMMAND_FLIRT     = "flirt"
VOICE_COMMAND_HAPPY     = "happy"
VOICE_COMMAND_GAME      = "game"
VOICE_COMMAND_TEST      = "test"
VOICE_COMMAND_INVALID   = "invalid"

# arecord -D hw:1,0 -d 5 -f S16_LE --disable-channels -c 2 -r 44100 -t wav test

class SpeechRecognition():

    def __init__(self):
        print("Initialized speech recognition")


    def transcribeFile(self):
 
        #AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)
        #AUDIO_FILE = path.join('/home/pi/Desktop/test/ece578_project1/', "test.wav")
        AUDIO_FILE = "/home/pi/Desktop/test/ece578_project1/test"
        print("Transcribing: " + AUDIO_FILE)
        
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            speech = r.recognize_google(audio)
            #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            print("Google Speech Recognition thinks you said " + speech)

            return speech
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    # =================================================================================================== #
    # Detect audio in through microphone
    #
    # Start a speech recognizer and listen for speech. This uses Googles cloud speech recognition
    # Return back the  string of text

    def detectAudio(self):
        
        print("Detecting audio...")
        
        USE_RECOGNIZER = 'Google'
        #USE_RECOGNIZER = 'Sphinx'

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
                except sr.Request.error as e:
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

    def keywordCheck(self, input_speech, test):
        
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

        if (regexp.search(str(input_speech))):
            return True

        return False


speech = SpeechRecognition()

# =================================================================================================== #
# Test Audio Detection

def TestAudioDetection():
    exit = 1
    while (exit != 'e'):
        print("Testing audio detection...")
        text = speech.detectAudio()
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

# Create single of the face class to import elsewhere
speech = SpeechRecognition()

# ================================================================ #
if __name__ == "__main__":  
    print("Testing speech recognition")
    #TestAudioDetection()
    speech.transcribeFile("nocamera")

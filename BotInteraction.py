#! /usr/bin/env python3

# Handles the human bot interactions
import os
import time
import threading
from FaceManager import face
from ArmManager import arms


# ============================================================================ #
ACTION_INVALID = 'Invalid'
ACTION_FLIRT = 'flirt'
ACTION_HAPPY = 'happy'
ACTION_MUSIC = 'music'


speakLock = threading.Lock()

class BotIteraction:

    def __init__(self):
        print("Bot Interaction initialized")
        self.__speakFlag = True

    # ============================================================================ #
    def __outputSpeech(self, content):
        print("Output speech: " + str(content))
        self.__speakFlag = True
        text = str(content)
        os.popen( 'espeak -s 110 "'+text+'" --stdout | aplay 2>/dev/null')
        
        # Calculate the length of the speech and go to sleep while talking
        #print("Text length: " + str(len(text)))
        time.sleep(len(text) * 0.1)
        # Set the flag to stop the mouth from moving
        speakLock.acquire(blocking=True)
        self.__speakFlag = False
        speakLock.release()
        #print("Flag set to false")


    # ============================================================================ #
    def __talkingMouth(self):
        print("Moving mouth...")
        while (True):
            # Do the mouth movement
            face.mouthOpen()
            face.mouthClose()
            # Check if the flag was set by other thread
            #print("Trying to acquire flag")
            speakLock.acquire()
            if (self.__speakFlag == False):
                #print("Flag is false")
                break
            speakLock.release()
        speakLock.release()


    # ============================================================================ #
    def speak(self, content):
        # Use multithreading library named threading
        mouth = threading.Thread(target=self.__outputSpeech, args=(content,))
        voice = threading.Thread(target=self.__talkingMouth)
        mouth.start()
        voice.start()
        mouth.join()
        voice.join()
        print("Finished speaking function")


    # ============================================================================ #
    def botReady(self):
        print("Bot Interaction: Ready")
        self.speak("I am ready for your command.")
        time.sleep(2)


    # ============================================================================ #
    def botWinner(self):
        print("Bot Interaction: Game Winner")
        self.speak("I am the winner!")
        face.veryHappy()
        arms.bangDrumLeft()
        arms.bangDrumRight()
        arms.bangDrumBoth()


    # ============================================================================ #
    def botLoser(self):
        print("Bot Interaction: Game Loser")
        self.speak("You are the winner!")
        face.sad()
        arms.reset()


    # ============================================================================ #
    def botTied(self):
        print("Bot Interaction: Game Tied")
        self.speak("We tied the game.")
        arms.reset()
        face.reset()
        

    # ============================================================================ #
    def playMusic(self):
        print("Bot Interaction: Playing music")
        self.speak("Look at me playing music!")
        arms.bangDrumLeft()
        arms.bangDrumRight()
        arms.bangDrumBoth()


    # ============================================================================ #
    def flirt(self):
        print("Bot Interaction: Flirt")
        self.speak("Well. Hello there, good looking.")


    # ============================================================================ #
    def botAction(type):
        # Display a happy emotion
        if (type == ACTION_MUSIC):
            self.playMusic()

        if (type == ACTION_HAPPY):
            self.speak("I am very happy!")
            face.veryHappy()

        if (type == ACTION_FLIRT):
            self.flirt()

        if (type == ACTION_INVALID):
            print("Bot Interaction: Invalid")
            self.speak("I do not understand the command.")
            time.sleep(1)
            self.speak("Please say: music, game, happy, flirt, or test")



    # ============================================================================ #
    def testSpeech(self):
        text = 0
        while(text != 'e'):
            text = input("What to say? ")
            self.speak(text)

# Create single of the face class to import elsewhere
bot = BotIteraction()

# ============================================================================ #
if __name__ == "__main__":  
    print("Running Bot Interaction tests")

    bot.botReady()
    time.sleep(4)
    
    bot.botTied()
    time.sleep(4)

    bot.botLoser()
    time.sleep(4)

    bot.botWinner()
    time.sleep(4)

    bot.playMusic()
    time.sleep(4)

    bot.flirt()
    time.sleep(4)

    print("End of bot interaction test")

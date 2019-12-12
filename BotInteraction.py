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

TEST_SLEEP_TIME = 1

#Add this address after moving to PI
MP3ADDRESS = '/home/pi/Fall_2019/mp3s/'

speakFlag = True
speakLock = threading.Lock()




# ============================================================================ #
def outputSpeech(content, filename):
    print("Output speech: " + str(content))
    global speakFlag
    speakFlag = True

    text = str(content)
    f = str(filename)
    os.popen( 'mpg321 "'+MP3ADDRESS+'""'+f+'" ')

    # Calculate the length of the speech and go to sleep while talking
    print("Text length: " + str(len(text)))
    time.sleep(len(text) * 0.1)
    # Set the flag to stop the mouth from moving
    print("output speech trying to acquire lock...")
    speakLock.acquire(blocking=True)
    speakFlag = False
    print("speakflag set to false")
    speakLock.release()
    print("Flag set to false")


# ============================================================================ #
def talkingMouth():
    print("Moving mouth...")
    global speakFlag
    while (True):
        # Do the mouth movement
        face.mouthOpen()
        face.mouthClose()
        # Check if the flag was set by other thread
        print("Trying to acquire lock")
        speakLock.acquire()
        print("speak flag status: " + str(speakFlag))
        if speakFlag == False:
            print("Flag is false")
            break
        speakLock.release()
        print("speak lock released")
    speakLock.release()


# ============================================================================ #
def speak(content, mp3):
    # Use multithreading library named threading
    mouth = threading.Thread(target=outputSpeech, args=(content,mp3))
    voice = threading.Thread(target=talkingMouth)
    mouth.start()
    voice.start()
    mouth.join()
    voice.join()
    print("Finished speaking function")


# ============================================================================ #
def botReady():
    print("Bot Interaction: Ready")
    speak("I am ready for your command.", "Ready.mp3")
    time.sleep(2)


# ============================================================================ #
def botWinner():
    print("Bot Interaction: Game Winner")
    speak("I am the winner!", "I_win.mp3")
    face.veryHappy()
    arms.bangDrumLeft()
    arms.bangDrumRight()
    arms.bangDrumBoth()


# ============================================================================ #
def botLoser():
    print("Bot Interaction: Game Loser")
    speak("You are the winner!", "You_win.mp3")
    face.sad()
    arms.reset()


# ============================================================================ #
def botTied():
    print("Bot Interaction: Game Tied")
    speak("We tied the game.", "Tie.mp3")
    arms.reset()
    face.reset()
    

# ============================================================================ #
def playMusic():
    print("Bot Interaction: Playing music")
    speak("Look at me playing music!", "Playing_music.mp3")
    arms.bangDrumLeft()
    arms.bangDrumRight()
    arms.bangDrumBoth()


# ============================================================================ #
def flirt():
    print("Bot Interaction: Flirt")
    speak("Well. Hello there, good looking.", "Flirt.mp3")


# ============================================================================ #
def botAction(type):
    # Display a happy emotion
    if (type == ACTION_MUSIC):
        playMusic()

    if (type == ACTION_HAPPY):
        speak("I am very happy!", "Happy.mp3")
        face.veryHappy()

    if (type == ACTION_FLIRT):
        flirt()

    if (type == ACTION_INVALID):
        print("Bot Interaction: Invalid")
        speak("I do not understand the command.", "Don't_understand.mp3")
        time.sleep(1)
        speak("Please say: music, game, happy, flirt, or test", "Menu.mp3")



# ============================================================================ #
def testSpeech():
    print("Running main test")

    # Test audio output
    speak('I am running a test on my body! If my movement is not matched to my words, it means something is broken!', "Diagnostic.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right eyebrow up", "right_eyebrow_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right eyebrown down", "right_eyebrow_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right eyebrow flat", "right_eyebrow_flat.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left eyebrow up", "left_eyebrow_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left eyebrow down", "left_eyebrow_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left eyebrow flat", "left_eyebrow_flat.mp3")
    time.sleep(TEST_SLEEP_TIME)

    #Speak("eyes close", "eyes_close.mp3")
    #servos.setServoPosition(servoID, pos)
    #servos.beginMotion()

    #Speak("eyes open", "eyes_open.mp3")
    #servos.setServoPosition(servoID, pos)
    #servos.beginMotion()

    speak("mouth open", "mouth_open.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("mouth close", "mouth_close.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right shoulder up", "right_shoulder_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right shoulder down", "right_shoulder_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left shoulder up", "left_shoulder_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left shoulder down", "left_shoulder_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right arm out", "right_arm_out.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right arm in", "right_arm_in.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left arm out", "left_arm_out.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left arm in", "left_arm_in.mp3")
    time.sleep(TEST_SLEEP_TIME)
    
    speak("right elbow down", "right_elbow_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right elbow up", "right_elbow_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left elbow down", "left_elbow_down.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("left elbow up", "left_elbow_up.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("Bang right drum", "bang_right_drum.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("Bang left drum", "bang_left_drum.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("Bang Both drums", "bang_both_drums.mp3")
    time.sleep(TEST_SLEEP_TIME)
    
    speak("Play music!", "music.mp3")
    time.sleep(TEST_SLEEP_TIME)
    

# ============================================================================ #
if __name__ == "__main__":  
    print("Running Bot Interaction tests")

    testSpeech()
'''
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
'''

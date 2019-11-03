#! /usr/bin/env python3

# Handles the main testing for the robot

from ServoManager import *
from ArmManager import *
from FaceManager import *

TEST_SLEEP_TIME = 1

def MainTest():
    time.sleep(0.8)
    print("Running main test")
    
    # Reset everything
    FaceReset()
    ArmReset()

    # Test audio output
    OutputSpeech('I am working on test my body! If my movement is not matched to my words, it means something is broken!')
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right eyebrow up")
    EyebrowUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right eyebrown down")
    EyebrowDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right eyebrow flat")
    EyebrowFlat(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("left eyebrow up")
    EyebrowUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left eyebrow down")
    EyebrowDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left eyebrow flat")
    EyebrowFlat(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("eyes close")
    EyeClose(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("eyes open")
    EyeOpen(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("mouth open")
    MouthOpen()
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("mouth close")
    MouthClose()
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("right shoulder up")
    ShoulderUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right shoulder down")
    ShoulderDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left should up")
    ShoulderUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left shoulder down")
    ShoulderDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("right arm out")
    ArmOut(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right arm in")
    ArmIn(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left arm out")
    ArmOut(LEFT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left arm in")
    ArmIn(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("right elbow down")
    ElbowDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("right elbow up")
    ElbowUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left elbow down")
    ElbowDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("left elbow up")
    ElbowUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("Bang right drum")
    BangDrumRight()
    time.sleep(TEST_SLEEP_TIME)
    
    OutputSpeech("Bang left drum")
    BangDrumLeft()
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("Bang Both drums")
    BangDrumBoth()
    time.sleep(TEST_SLEEP_TIME)

    OutputSpeech("Play music!")
    PlayMusic()
    time.sleep(TEST_SLEEP_TIME)


#! /usr/bin/env python3

# Handles the main testing for the robot

from ServoManager import *
from ArmManager import *
from FaceManager import *
from BotInteraction import *

TEST_SLEEP_TIME = 1

def MainTest():
    time.sleep(0.8)
    print("Running main test")

    # Reset everything
    FaceReset()
    ArmReset()

    # Test audio output
    Speak('I am running a test on my body! If my movement is not matched to my words, it means something is broken!', "Diagnostic.mp3")
    time.sleep(TEST_SLEEP_TIME)

    Speak("right eyebrow up", "right_eyebrow_up.mp3")
    EyebrowUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right eyebrown down", "right_eyebrow_down.mp3")
    EyebrowDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right eyebrow flat", "right_eyebrow_flat.mp3")
    EyebrowFlat(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left eyebrow up", "left_eyebrow_up.mp3")
    EyebrowUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left eyebrow down", "left_eyebrow_down.mp3")
    EyebrowDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left eyebrow flat", "left_eyebrow_flat.mp3")
    EyebrowFlat(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("eyes close", "eyes_close.mp3")
    EyeClose(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("eyes open", "eyes_open.mp3")
    EyeOpen(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("mouth open", "mouth_open.mp3")
    MouthOpen()
    time.sleep(TEST_SLEEP_TIME)

    Speak("mouth close", "mouth_close.mp3")
    MouthClose()
    time.sleep(TEST_SLEEP_TIME)

    Speak("right shoulder up", "right_shoulder_up.mp3")
    ShoulderUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right shoulder down", "right_shoulder_down.mp3")
    ShoulderDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left shoulder up", "left_shoulder_up.mp3")
    ShoulderUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left shoulder down", "left_shoulder_down.mp3")
    ShoulderDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right arm out", "right_arm_out.mp3")
    ArmOut(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right arm in", "right_arm_in.mp3")
    ArmIn(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left arm out", "left_arm_out.mp3")
    ArmOut(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left arm in", "left_arm_in.mp3")
    ArmIn(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right elbow down", "right_elbow_down.mp3")
    ElbowDown(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("right elbow up", "right_elbow_up.mp3")
    ElbowUp(RIGHT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left elbow down", "left_elbow_down.mp3")
    ElbowDown(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("left elbow up", "left_elbow_up.mp3")
    ElbowUp(LEFT)
    time.sleep(TEST_SLEEP_TIME)

    Speak("Bang right drum", "bang_right_drum.mp3")
    BangDrumRight()
    time.sleep(TEST_SLEEP_TIME)

    Speak("Bang left drum", "bang_left_drum.mp3")
    BangDrumLeft()
    time.sleep(TEST_SLEEP_TIME)

    Speak("Bang Both drums", "bang_both_drums.mp3")
    BangDrumBoth()
    time.sleep(TEST_SLEEP_TIME)

    Speak("Play music!", "music.mp3")
    PlayMusic()
    time.sleep(TEST_SLEEP_TIME)

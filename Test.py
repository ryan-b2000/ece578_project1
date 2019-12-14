#! /usr/bin/env python3

# Handles the main testing for the robot

from ServoManager import servos
from ArmManager import arms
from FaceManager import face
from BotInteraction import *

TEST_SLEEP_TIME = 1
EYEBROW_R = 0
EYEBROW_L = 1
EYELID_L = 2
EYELID_R = 3
EYE_VERTICAL = 4
EYE_HORIZONTAL = 5
MOUTH = 6
ARM_UPDOWN_L = 7
ARM_ROTATE_L = 8
ELBOW_L = 9
ARM_UPDOWN_R = 10
ARM_ROTATE_R = 11
ELBOW_R = 12


def MainTest():
    time.sleep(0.8)
    print("Running main test")


    servos.setMovementFrame(0)
    arms.reset()
    

    # Test audio output
    speak('I am running a test on my body! If my movement is not matched to my words, it means something is broken!', "Diagnostic.mp3")
    time.sleep(TEST_SLEEP_TIME)

    speak("right eyebrow up", "right_eyebrow_up.mp3")
    servos.setServoPosition(EYEBROW_R, 100)
    servos.beginMotion()

    speak("right eyebrown down", "right_eyebrow_down.mp3")
    servos.setServoPosition(EYEBROW_R, 50)
    servos.beginMotion()

    speak("right eyebrow flat", "right_eyebrow_flat.mp3")
    servos.setServoPosition(EYEBROW_R, 80)
    servos.beginMotion()

    speak("left eyebrow up", "left_eyebrow_up.mp3")
    servos.setServoPosition(EYEBROW_L, 100)
    servos.beginMotion()

    speak("left eyebrow down", "left_eyebrow_down.mp3")
    servos.setServoPosition(EYEBROW_L, 50)
    servos.beginMotion()

    speak("left eyebrow flat", "left_eyebrow_flat.mp3")
    servos.setServoPosition(EYEBROW_L, 80)
    servos.beginMotion()

    #speak("eyes close", "eyes_close.mp3")
    #servos.setServoPosition(servoID, pos)
    #servos.beginMotion()

    #speak("eyes open", "eyes_open.mp3")
    #servos.setServoPosition(servoID, pos)
    #servos.beginMotion()

    speak("mouth open", "mouth_open.mp3")
    servos.setServoPosition(MOUTH, 50)
    servos.beginMotion()

    speak("mouth close", "mouth_close.mp3")
    servos.setServoPosition(MOUTH, 20)
    servos.beginMotion()

    speak("right shoulder up", "right_shoulder_up.mp3")
    servos.setServoPosition(ARM_UPDOWN_R, 30)
    servos.beginMotion()

    speak("right shoulder down", "right_shoulder_down.mp3")
    servos.setServoPosition(ARM_UPDOWN_R, 70)
    servos.beginMotion()

    speak("left shoulder up", "left_shoulder_up.mp3")
    servos.setServoPosition(ARM_UPDOWN_L, 90)
    servos.beginMotion()

    speak("left shoulder down", "left_shoulder_down.mp3")
    servos.setServoPosition(ARM_UPDOWN_L, 50)
    servos.beginMotion()

    speak("right arm out", "right_arm_out.mp3")
    servos.setServoPosition(ARM_ROTATE_R, 80)
    servos.beginMotion()
    
    speak("right elbow down", "right_elbow_down.mp3")
    servos.setServoPosition(ELBOW_R, 90)
    servos.beginMotion()

    speak("right elbow up", "right_elbow_up.mp3")
    servos.setServoPosition(ELBOW_R, 30)
    servos.beginMotion()

    speak("right arm in", "right_arm_in.mp3")
    servos.setServoPosition(ARM_ROTATE_R, 30)
    servos.beginMotion()
    #recenter the arm
    servos.setServoPosition(ARM_ROTATE_R, 55)

    speak("left arm out", "left_arm_out.mp3")
    servos.setServoPosition(ARM_ROTATE_L, 50)
    servos.beginMotion()
    
    speak("left elbow down", "left_elbow_down.mp3")
    servos.setServoPosition(ELBOW_L, 100)
    servos.beginMotion()

    speak("left elbow up", "left_elbow_up.mp3")
    servos.setServoPosition(ELBOW_L, 120)
    servos.beginMotion()

    speak("left arm in", "left_arm_in.mp3")
    servos.setServoPosition(ARM_ROTATE_L, 65)
    servos.beginMotion()
    #recenter the arm
    servos.setServoPosition(ARM_ROTATE_L, 65)
    servos.beginMotion()

    speak("Bang right drum", "bang_right_drum.mp3")
    arms.bangDrumRight()

    speak("Bang left drum", "bang_left_drum.mp3")
    arms.bangDrumLeft()

    speak("Play music!", "music.mp3")
    playMusic()


# ================================================================ #
if __name__ == "__main__":  
    MainTest()

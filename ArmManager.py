#! /usr/bin/env python3

'''
#################################################################################################
    
    DimBot Arm Manager

    This module creates an abstraction for the arm movements allowing a higher level call for 
    specific arm movements. It relies on the servo manager to do the actual servo control

'''
import time
from ServoManager import servos

EYEBROW_R = 0
EYEBROW_L = 1
EYELID_L = 2
EYELID_R = 3
EYE_VERTICAL = 4
EYE_HORIZONTAL = 5
MOUTH = 6
ARM_UPDOWN_R = 12
ARM_ROTATE_R = 13
ELBOW_R = 14
ARM_UPDOWN_L = 8
ARM_ROTATE_L = 9
ELBOW_L = 10

class ArmManager:

    def __init__(self):
        print("Arm manager initialized")


    def reset(slef):
        print("Arm reset...")
        servos.setMovementFrame(0)
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 0)    # arm relax
        servos.setServoPosition(ARM_UPDOWN_L, 0)    # arm relax

    def bangDrumRight(self):
        print("Bang Right Drum")
        servos.setMovementFrame(0)
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 40)   # arm up
        servos.setServoPosition(ELBOW_R, 90)        # elbow  down
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 0)    # arm relax
        servos.beginMotion()

    def bangDrumLeft(self):
        print("Bang Left Drum")
        servos.setMovementFrame(0)
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_UPDOWN_L, 80)   # arm up
        servos.setServoPosition(ELBOW_L, 80)        # elbow down
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_UPDOWN_L, 0)    # arm relax


    def bangDrumBoth(self):
        print("Bang Both Drum")
        # bring the arms up
        servos.setMovementFrame(0.1)
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 40)   # arm up
        servos.setServoPosition(ARM_UPDOWN_L, 80)   # arm up
        servos.beginMotion()
        # bang the drum
        servos.setMovementFrame(0)
        servos.setServoPosition(ELBOW_L, 80)        # elbow down
        servos.setServoPosition(ELBOW_R, 90)        # elbow  down
        servos.beginMotion()
        # bring arms back
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.beginMotion()
        # relax arms
        servos.setServoPosition(ARM_UPDOWN_L, 0)    # arm relax
        servos.setServoPosition(ARM_UPDOWN_R, 0)    # arm relax
        servos.beginMotion()


    def armCelebration(self):
        print("Arm Celebration")
        # arms up
        servos.setMovementFrame(0.1)
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 40)   # arm up
        servos.setServoPosition(ARM_UPDOWN_L, 80)   # arm up
        servos.beginMotion()
        # right arm high/out and back
        servos.setServoPosition(ELBOW_R, 60)        # elbow  down
        servos.setServoPosition(ARM_ROTATE_R, 70)   # arm out
        servos.beginMotion()
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ARM_ROTATE_R, 30)   # arm in
        servos.beginMotion()
        #left arm high/out and back
        servos.setServoPosition(ELBOW_L, 90)        # elbow down
        servos.setServoPosition(ARM_ROTATE_L, 50)   # arm out
        servos.beginMotion()
        servos.setServoPosition(ELBOW_L, 100)       # elbow up
        servos.setServoPosition(ARM_ROTATE_L, 80)   # arm in
        servos.beginMotion()


    def armTest(self):
        print("Arm Test")
        servos.setMovementFrame(0)
        # Right arm rotate
        servos.setServoPosition(ARM_ROTATE_R, 55)   # in
        servos.beginMotion()
        servos.setServoPosition(ARM_ROTATE_R, 80)   # out
        servos.beginMotion()
        servos.setServoPosition(ARM_ROTATE_R, 55)   # center
        servos.beginMotion()
        # Right arm up/down
        servos.setServoPosition(ARM_UPDOWN_R, 30)   # in
        servos.beginMotion()
        servos.setServoPosition(ARM_UPDOWN_R, 70)   # out
        servos.beginMotion()
        servos.setServoPosition(ARM_UPDOWN_R, 0)   # center
        servos.beginMotion()


# Initialize class singleton for importing
arms = ArmManager()

# ================================================================ #
if __name__ == "__main__":  
    print("Running arm tests...")
    arms.bangDrumRight()
    time.sleep(1)

    arms.bangDrumLeft()
    time.sleep(1)

    arms.bangDrumBoth()
    time.sleep(1)

    arms.armCelebration()
    time.sleep(1)
    
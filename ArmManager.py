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
ARM_UPDOWN_L = 7
ARM_ROTATE_L = 8
ELBOW_L = 9
ARM_UPDOWN_R = 10
ARM_ROTATE_R = 11
ELBOW_R = 12


class ArmManager:

    def __init__(self):
        print("Arm manager initialized")


    def reset(self):
        print("Arm reset...")
        servos.setMovementFrame(0)
        servos.setServoPosition(ELBOW_R, 50)        # elbow up
        servos.setServoPosition(ELBOW_L, 140)       # elbow up
        servos.beginMotion()
        time.sleep(.5)
        servos.setServoPosition(ARM_ROTATE_R, 55) #arm in 
        servos.setServoPosition(ARM_ROTATE_L, 60) #arm in 
        servos.beginMotion()
        time.sleep(.5)
        servos.setServoPosition(ARM_UPDOWN_R, 50)    # arm relax
        servos.setServoPosition(ARM_UPDOWN_L, 70)    # arm relax
        servos.beginMotion()
       

    def bangDrumRight(self):
        print("Bang Right Drum")
        servos.setMovementFrame(0)
        servos.setServoPosition(ARM_ROTATE_R, 55)# arm in
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 55)   # arm up
        servos.beginMotion()
        servos.setServoPosition(ELBOW_R, 80)        # elbow  down
        servos.beginMotion()
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.beginMotion()

    def bangDrumLeft(self):
        print("Bang Left Drum")
        servos.setMovementFrame(0)
        servos.setServoPosition(ARM_ROTATE_L, 65)   # arm in
        servos.setServoPosition(ELBOW_L, 140)       # elbow up
        servos.beginMotion()
        servos.setServoPosition(ARM_UPDOWN_L, 70)   # arm up
        servos.setServoPosition(ELBOW_L, 90)        # elbow down
        servos.beginMotion()
        servos.setServoPosition(ELBOW_L, 140)       # elbow up
        servos.beginMotion()

    def armCelebration(self):
        print("Arm Celebration")
        #arms ready
        arms.reset()
        time.sleep(1)
        # RIGHT ARM
        # right arm high/out and back
        servos.setServoPosition(ELBOW_R, 30)        # elbow up
        servos.setServoPosition(ARM_UPDOWN_R, 55)   # arm center
        servos.setServoPosition(ARM_ROTATE_R, 60)   # arm in
        servos.beginMotion()
        #arm out
        servos.setServoPosition(ARM_ROTATE_R, 100)   # arm out
        servos.beginMotion()
        #elbow down
        servos.setServoPosition(ELBOW_R, 120)
        servos.beginMotion()
        #elbow up
        servos.setServoPosition(ELBOW_R, 30)
        servos.beginMotion()
        #arm in 
        servos.setServoPosition(ARM_ROTATE_R, 60)   # arm in
        servos.beginMotion()
        #arm out
        servos.setServoPosition(ARM_ROTATE_R, 100)   # arm out
        servos.beginMotion()
        #arm in
        servos.setServoPosition(ARM_ROTATE_R, 60)   # arm in
        servos.beginMotion()
        
        # LEFT ARM
        # left arm high/out and back
        servos.setServoPosition(ELBOW_L, 140)        # elbow up
        servos.setServoPosition(ARM_UPDOWN_L, 90)   # arm center
        servos.setServoPosition(ARM_ROTATE_L, 65)   # arm in
        servos.beginMotion()
        #arm out
        servos.setServoPosition(ARM_ROTATE_L, 40)   # arm out
        servos.beginMotion()
        #elbow down
        servos.setServoPosition(ELBOW_L, 100)   # elbow down
        servos.beginMotion()
        #elbow up
        servos.setServoPosition(ELBOW_L, 140)        # elbow up
        servos.beginMotion()
        #arm in
        servos.setServoPosition(ARM_ROTATE_L, 65)   # arm in
        servos.beginMotion()
        #arm out
        servos.setServoPosition(ARM_ROTATE_L, 40)   # arm out
        servos.beginMotion()
        #arm in
        servos.setServoPosition(ARM_ROTATE_L, 65)   # arm in
        servos.beginMotion()
   

# Initialize class singleton for importing
arms = ArmManager()

# ================================================================ #
if __name__ == "__main__":  
    print("Running arm tests...")
    time.sleep(1)
    arms.reset()
    time.sleep(3)
    arms.bangDrumRight()
    arms.bangDrumLeft()
    time.sleep(3)
    arms.reset()
    time.sleep(3)
    arms.armCelebration()
    time.sleep(1)
    arms.reset()
    time.sleep(1)


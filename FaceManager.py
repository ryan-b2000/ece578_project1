#! /usr/bin/env python3


''' #################################################################################################
    
    DimBot FaceClass

    This class handles the movements for the face servos. It provides an interface for displaying
    varying emotional responses by the roboto

'''

import time
from ServoManager import servos

# ======================= DEFINES ======================= #
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



class FaceManager():

    def __init__(self):
        print("Face Manager initialized")
        self.reset()

    def reset(self):
        print("Face reset...")
        servos.setMovementFrame(0)
        servos.setServoPosition(EYEBROW_R, 80)      # eyebrow flat
        servos.setServoPosition(EYEBROW_L, 80)      # eyebrow flat
        servos.setServoPosition(EYELID_R, 60)       # eye open
        servos.setServoPosition(EYELID_L, 60)       # eye open
        servos.setServoPosition(EYE_HORIZONTAL, 80) # eye center
        servos.setServoPosition(EYE_VERTICAL, 70)   # eye center
        servos.setServoPosition(MOUTH, 20)          # mouth close
        servos.beginMotion()


    def excited(self):
        print("Display excited expression")
        servos.setMovementFrame(0.1)
        servos.setServoPosition(MOUTH, 50)          # mouth open
        servos.setServoPosition(EYEBROW_R, 90)     # eyebrow up
        servos.setServoPosition(EYEBROW_L, 90)     # eyebrow up
        servos.setServoPosition(EYE_HORIZONTAL, 80) # eye center
        servos.setServoPosition(EYELID_R, 60)       # eye open
        servos.setServoPosition(EYELID_L, 60)       # eye open
        servos.beginMotion()
        time.sleep(2)
        self.reset()


    def veryHappy(self):
        print("Display very happy expression")
        servos.setMovementFrame(0.1)
        servos.setServoPosition(MOUTH, 50)          # mouth open
        servos.setServoPosition(EYEBROW_R, 100)     # eyebrow up
        servos.setServoPosition(EYEBROW_L, 100)     # eyebrow up
        servos.setServoPosition(EYE_HORIZONTAL, 80) # eye center
        servos.setServoPosition(EYELID_R, 60)       # eye open
        servos.setServoPosition(EYELID_L, 60)       # eye open
        servos.setServoPosition(MOUTH, 50)          # mouth open
        servos.beginMotion()
        time.sleep(2)
        self.reset()


    def sad(self):
        print("Display sad expression")
        servos.setMovementFrame(0.1)
        servos.setServoPosition(MOUTH, 50)          # mouth close
        servos.setServoPosition(EYEBROW_L, 70)      # eyebrow low
        servos.setServoPosition(EYEBROW_L, 70)      # eyebrow low
        servos.setServoPosition(EYE_VERTICAL, 60)   # eyes down
        servos.beginMotion()
        time.sleep(4)
        self.reset()


    def angry(self):
        print("Display angry expression")
        servos.setMovementFrame(0.1)
        servos.setServoPosition(MOUTH, 50)          # mouth close
        servos.setServoPosition(EYE_VERTICAL, 70)   # eyes down
        servos.setServoPosition(EYEBROW_R, 50)      # eyebrow down
        servos.setServoPosition(EYEBROW_L, 50)      # eyebrow down
        servos.setServoPosition(EYE_HORIZONTAL, 60)
        servos.beginMotion()
        servos.setServoPosition(EYE_HORIZONTAL, 60)     # eye left
        servos.beginMotion()
        servos.setServoPosition(EYE_HORIZONTAL, 100)    # eye right
        servos.beginMotion()
        servos.setServoPosition(EYE_HORIZONTAL, 80)     # eye center
        self.reset()

    def mouthClose(self):
        servos.setMovementFrame(0)
        servos.setServoPosition(MOUTH, 20)          # mouth close
        servos.beginMotion()


    def mouthOpen(self):
        servos.setMovementFrame(0)
        servos.setServoPosition(MOUTH, 50)          # mouth open
        servos.beginMotion()        

# Create single of the face class to import elsewhere
face = FaceManager()

# ================================================================ #
if __name__ == "__main__":  
    print("Running face tests...")

    face.reset()
    time.sleep(2)

    face.excited()
    time.sleep(2)

    face.veryHappy()
    time.sleep(2)

    face.sad()
    time.sleep(2)

    face.angry()
    print("End of face manager test")

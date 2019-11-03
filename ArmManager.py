#! /usr/bin/env python3

''' #################################################################################################
    
    DimBot FaceClass

    This class handles the movements for the face servos. It provides an interface for displaying
    varying emotional responses by the roboto

'''
import time
from ServoManager import *



def ArmReset():
    print("Arm reset...")
    ElbowUp(RIGHT)
    ElbowUp(LEFT)
    ArmIn(RIGHT)
    ArmIn(LEFT)
    ShoulderDown(RIGHT)
    ShoulderDown(LEFT)

def BangDrumRight():
    print("Bang drum right")
    ElbowDown(RIGHT)
    ElbowUp(RIGHT)

def BangDrumLeft():
    print("Bang drum left")
    ElbowDown(LEFT)
    ElbowUp(LEFT)

def BangDrumBoth():
    print("Bang both drums")
    ElbowDown(LEFT)
    ElbowDown(RIGHT)
    ElbowUp(LEFT)
    ElbowUp(RIGHT)


# ================================================================ #
if __name__ == "__main__":  
    print("Running arm tests...")

    ArmReset()
    time.sleep(4)

    BangDrumRight()
    time.sleep(4)
    
    BangDrumLeft()
    time.sleep(4)

    BangDrumBoth()
    time.sleep(4)

    PlayMusic()
    time.sleep(4)

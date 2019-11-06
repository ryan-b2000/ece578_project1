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
    ElbowUp(RIGHT) # not received
    ElbowDown(RIGHT)
    ElbowUp(RIGHT)
    Sleep()
    ElbowDown(RIGHT)
    Sleep()
    ElbowUp(RIGHT)
    Sleep()

def BangDrumLeft():
    print("Bang drum left")
    ElbowUp(LEFT)
    Sleep()
    ElbowDown(LEFT)
    Sleep()
    ElbowUp(LEFT)

def BangDrumBoth():
    print("Bang both drums")
    BangDrumLeft()
    BangDrumRight()


# ================================================================ #
if __name__ == "__main__":  
    print("Running arm tests...")

    ArmReset()
    time.sleep(2)

    BangDrumRight()
    time.sleep(2)
    
    BangDrumLeft()
    time.sleep(2)

    BangDrumBoth()
    time.sleep(2)



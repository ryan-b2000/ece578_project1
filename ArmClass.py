#! /usr/bin/env python3

''' #################################################################################################
    
    DimBot FaceClass

    This class handles the movements for the face servos. It provides an interface for displaying
    varying emotional responses by the roboto

'''
import time
import MoveClass


class ArmClass:
    
    def __init__ (self):
        print("Move class initialized")
        self.__Move = MoveClass()

    def ArmReset(self):
        print("Arm reset")
        self.__Move.ElbowUp(RIGHT)
        self.__Move.ElbowUp(LEFT)
        self.__Move.ArmIn(RIGHT)
        self.__Move.ArmIn(LEFT)
        self.__Move.ShoulderDown(RIGHT)
        self.__Move.ShoulderDown(LEFT)

    def BangDrumRight(self):
        print("Bang drum right")
        self.__Move.ElbowDown(RIGHT)
        self.__Move.ElbowUp(RIGHT)

    def BandDrumLeft(self):
        print("Bang drum left")
        self.__Move.ElbowDown(LEFT)
        self.__Move.ElbowUp(LEFT)


# ================================================================ #
if __name__ == "__main__":  
    print("Running arm tests...")
    
    arm = ArmClass()
    arm.ArmReset()
    time.sleep(2)

    arm.BangDrumRight()
    time.sleep(2)
    
    arm.BandDrumLeft()
    time.sleep(2)

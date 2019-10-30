#! /usr/bin/env python3

''' #################################################################################################
    
    DimBot FaceClass

    This class handles the movements for the face servos. It provides an interface for displaying
    varying emotional responses by the roboto

'''

import MoveClass


class ArmClass:
    
    def __init__ (self):
        print("Move class initialized")
        self.__Move = MoveClass()

    def Arm_Reset(self):
        print("Arm reset")
        self.__Move.ElbowUp(RIGHT)
        self.__Move.ElbowUp(LEFT)
        self.__Move.ArmIn(RIGHT)
        self.__Move.ArmIn(LEFT)
        self.__Move.ShoulderDown(RIGHT)
        self.__Move.ShoulderDown(LEFT)

    def Bang_Drum_Right(self):
        print("Bang drum right")
        self.__Move.ElbowDown(RIGHT)

    def Band_Drum_Left(self):
        print("Bang drum left")
        self.__Move.ElbowDown(LEFT)


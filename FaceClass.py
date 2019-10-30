#! /usr/bin/env python3


'''	#################################################################################################
	
	DimBot FaceClass

	This class handles the movements for the face servos. It provides an interface for displaying
	varying emotional responses by the roboto

'''

import time
import MoveClass


class FaceClass:
        
    def __init__ (self):
        print("Face class initialized")
        self.__Move = MoveClass()


    def FaceReset(self):
        self.__Move.EyebrowFlat(RIGHT)
        self.__Move.EyebrowFlat(LEFT)
        self.__Move.EyeOpen(RIGHT)
        self.__Move.EyeOpen(LEFT)
        self.__Move.EyeCenter()
        self.__Move.EyeMiddle()
        self.__Move.MouthClose()
        print("Reset is done")


    def Excited(self):
        self.__Move.MouthOpen()
        self.__Move.EyebrowFlat(RIGHT)
        self.__Move.EyebrowFlat(LEFT)
        self.__Move.EyeMiddle()
        self.__Move.EyeOpen(RIGHT)
        self.__Move.EyeOpen(LEFT)
        time.sleep(2)
        self.FaceReset()
        print("Display excited expression")

    
    def VeryHappy(self):
        self.__Move.MouthOpen()
        self.__Move.EyeUp()
        self.__Move.EyeOpen(RIGHT)
        self.__Move.EyeOpen(LEFT)
        self.__Move.EyebrowUp(RIGHT)
        self.__Move.EyebrowUp(LEFT)
        time.sleep(2)
        self.FaceReset()
        print("Display very happy expression")


    def Sad(self):
        self.__Move.MouthClose()
        self.__Move.EyebrowFlat(RIGHT)
        self.__Move.EyebrowFlat(LEFT)
        self.__Move.EyeClose(RIGHT)
        self.__Move.EyeClose(LEFT)
        self.__Move.EyeDown()
        time.sleep(2)
        self.FaceReset()
        print("Display sad expression")
    

    # blink both eyes
    def Blink(self):
        i = 0
        self.__Move.MouthClose()
        self.__Move.EyebrowUp(RIGHT)
        self.__Move.EyebrowUp(LEFT)
        self.__Move.EyeOpen()

        while(i < 2):
            self.__Move.EyebrowDown(RIGHT)
            self.__Move.EyebrowDown(LEFT)
            self.__Move.EyeClose()
            time.sleep(0.3)
            self.__Move.EyebrowUp(RIGHT)
            self.__Move.EyebrowUp(LEFT)
            self.__Move.EyeOpen()
            time.sleep(0.3)
            i = i + 1	
            time.sleep(0.3)
        time.sleep(2)
        self.FaceReset()
        print("Blinking expression")


    # Wink right eye
    def WinkRight(self): 
        for i in range(2):
            self.__Move.EyebrowUp(RIGHT)
            self.__Move.EyeOpen(RIGHT)
            time.sleep(0.5)
            self.__Move.EyebrowDown(RIGHT)
            self.__Move.EyeClose(RIGHT)
        self.__Move.EyebrowUp(RIGHT)
        self.__Move.EyeOpen(RIGHT)
        time.sleep(2)
        self.FaceReset()
        print("Wink right eye")


    def Angry(self):
        self.__Move.MouthClose()
        self.__Move.EyeMiddle()
        self.__Move.EyebrowDown(RIGHT)
        self.__Move.EyebrowDown(LEFT)
        self.__Move.EyeLeft()
        time.sleep(1)
        self.__Move.EyeRight()
        time.sleep(1)
        self.__Move.EyeCenter()
        time.sleep(2)
        self.FaceReset()
        print("Display angry expression")


# ================================================================ #
if __name__ == "__main__":  
    print("Running face tests...")
    Face = FaceClass()

    Face.FaceReset()
    time.sleep(2)

    Face.Excited()
    time.sleep(2)

    Face.VeryHappy()
    time.sleep(2)

    Face.Sad()
    time.sleep(2)

    Face.Blink()
    time.sleep(2)

    Face.WinkRight()
    time.sleep(2)

    Face.Angry()
    time.sleep(2)

#! /usr/bin/env python3

'''	#################################################################################################
	
	DimBot FaceClass

	This class handles the movements for the face servos. It provides an interface for displaying
	varying emotional responses by the roboto

'''

import MoveClass


class FaceClass:
        
    def __init__ (self):
        print("Face class initialized")
        self.__Move = MoveClass()

    def FaceReset(self):
        self.__Move.EyebrowFlat(RIGHT)

        self.Left_Eyebrow(EYEBROW_L,DEGREE_120)
        self.Right_Eyebrow(EYEBROW_R,DEGREE_120)
        self.Mouth(MOUTH,DEGREE_0)
        self.Right_Eye_Lid(EYELID_R,DEGREE_90)
        self.Left_Eye_Lid(EYELID_L,DEGREE_120)
        self.Eye_Vertical(EYE_VERTICAL,DEGREE_100)
        self.Eye_Horizontal(EYE_HORIZONTAL,DEGREE_110)
        print("Reset is done")

    def Excited(self):
        self.Mouth(MOUTH,DEGREE_60)
        self.Right_Eyebrow(EYEBROW_R,DEGREE_135)
        self.Left_Eyebrow(EYEBROW_L,DEGREE_135)
        self.Right_Eye_Lid(EYELID_R,DEGREE_90)
        self.Left_Eye_Lid(EYELID_L,DEGREE_120)
        os.system('flite -voice rms -t "Hey, I am Excited"')
        time.sleep(0.5)
    
    def Very_happy(self):
        self.Mouth(MOUTH,DEGREE_60)
        self.Eye_Vertical(EYE_VERTICAL,DEGREE_100)
        self.Right_Eyebrow(EYEBROW_R,DEGREE_135)
        self.Left_Eyebrow(EYEBROW_L,DEGREE_135)
        self.Right_Eye_Lid(EYELID_R,DEGREE_140)
        self.Left_Eye_Lid(EYELID_L,DEGREE_70)
        self.Eye_Vertical(EYE_VERTICAL,DEGREE_120)
        speaking('Do not be sad. You will win next time! Hahahahahahaha')
        time.sleep(0.5)
   

    def Sad(self):
        Robo_face.Mouth(MOUTH,DEGREE_45)
        Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_140)
        Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_140)
        Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_130)
        Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_85)
        Robo_face.Eye_Vertical(EYE_VERTICAL,DEGREE_100)
        speaking('I will win next time!')
        time.sleep(0.5)
    
    # wink both eyes together
    def Winky(self):
        i = 0
        Robo_face.Mouth(MOUTH,DEGREE_60)
        Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_135)
        Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_135)
        Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_90)
        Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_120)
        while(i < 2):
            Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_60)
            Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_150)
            Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_90)
            Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_90)
            time.sleep(0.3)
            Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_120)
            Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_90)
            Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_135)
            Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_135)
            time.sleep(0.3)
            i = i + 1	
            time.sleep(0.3)

    def Angry(self):
        Robo_face.Mouth(MOUTH,DEGREE_45)
        self.Eye_Horizontal(EYE_HORIZONTAL,DEGREE_160)
        time.sleep(1)
        self.Eye_Horizontal(EYE_HORIZONTAL,DEGREE_80)
        time.sleep(1)
        self.Eye_Horizontal(EYE_HORIZONTAL,DEGREE_110)
        time.sleep(0.3)
        Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_90)
        Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_90)
        Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_100)
        Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_110)
        Robo_face.Eye_Vertical(EYE_VERTICAL,DEGREE_100)
        speaking('I will win next time!')
        time.sleep(0.5)

    # Wink left and right eyes by turns
    def Winky_new(self): #left 90 open 150 close right 120 open 60 close brow 120 h 135\ 90 / 
        i = 0
        Robo_face.Mouth(MOUTH,DEGREE_60)
        Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_120)
        Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_120)
        Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_90)
        Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_120)
        while(i < 3):
            Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_120)
            Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_150)
            Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_110)
            Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_135)
            time.sleep(1)
            Robo_face.Left_Eye_Lid(EYELID_L,DEGREE_60)
            Robo_face.Right_Eye_Lid(EYELID_R,DEGREE_90)
            Robo_face.Left_Eyebrow(EYEBROW_L,DEGREE_135)
            Robo_face.Right_Eyebrow(EYEBROW_R,DEGREE_110)
            time.sleep(1)
            i = i + 1	
            time.sleep(0.3)

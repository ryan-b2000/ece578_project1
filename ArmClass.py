#! /usr/bin/env python3

''' #################################################################################################
    
    DimBot FaceClass

    This class handles the movements for the face servos. It provides an interface for displaying
    varying emotional responses by the roboto

'''

# ======================= ROBOT GAME GESTURES ======================= #
#
# This class provides the gestures of the robot in response to the game

class Game_Gesture:
    
    
    def Arm_Reset(self):
        self.move(ELBOW_L,DEGREE_150)
        self.move(ELBOW_R,DEGREE_150)
        time.sleep(1)
        self.move(ARM_ROTATE_L,DEGREE_120)
        self.move(ARM_SIDEWAYS_L,DEGREE_180)
        time.sleep(1)
        self.move(ARM_ROTATE_L,DEGREE_120)
        self.move(ARM_SIDEWAYS_R,DEGREE_0)
        self.move(ARM_ROTATE_R,DEGREE_90)
        self.move(ELBOW_L,DEGREE_30)
        self.move(ELBOW_R,DEGREE_150)
        self.move(ARM_SIDEWAYS_L,DEGREE_180)
    
    #  beat the drum once  
    def Paper(self):
        self.move(ELBOW_R,DEGREE_170) #low
        time.sleep(1)
        self.move(ELBOW_R,DEGREE_150) #high
        time.sleep(1)
    
    #  beat the drum twice  
    def Scissors(self):
        self.move(ELBOW_R,DEGREE_170) #low
        time.sleep(0.5)
        self.move(ELBOW_R,DEGREE_150) #high
        time.sleep(0.8)
        self.move(ELBOW_R,DEGREE_170) #low
        time.sleep(0.5)
        self.move(ELBOW_R,DEGREE_150) #high
        time.sleep(0.8)
    
    #   beat the side of drum once
    def Rock(self):
        PCA9685.set_pwm(ARM_ROTATE_L,0,DEGREE_90) #outside
        time.sleep(1)
        self.move(ELBOW_R,DEGREE_175) #low 
        time.sleep(1)
        PCA9685.set_pwm(ARM_ROTATE_L,0,DEGREE_120) #inside
        time.sleep(1)
        PCA9685.set_pwm(ARM_ROTATE_L,0,DEGREE_85) #outside
        time.sleep(1)
        self.move(ELBOW_R,DEGREE_150) #high 
        time.sleep(1)
        PCA9685.set_pwm(ARM_ROTATE_L,0,DEGREE_120) #inside
        time.sleep(1)

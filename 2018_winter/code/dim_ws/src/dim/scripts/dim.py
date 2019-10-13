#!/usr/bin/env python

'''
says a line if the line exists for the robot.
Then publishes increment to indicate its done.
'''

import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import rospy
import pygame
import os
import time
from std_msgs.msg import Int32
import sys


# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()


##Pulse length to degrees
degree_0 = 102
degree_30 = 171
degree_40 = 194
degree_45 = 206
degree_50 = 220
degree_60 = 240
degree_70 = 263
degree_80 = 286
degree_85 = 297
degree_90 = 310
degree_100 = 333
degree_110 = 356
degree_120 = 379
degree_130 = 400
degree_135 = 414
degree_140 = 430
degree_150 = 448
degree_160 = 471
degree_180 = 505

#pwm channel number on PWM Driver
pwm_channel_0 = 0 #Left Eyebrow
pwm_channel_1 = 1 #Right Eyebrow
pwm_channel_2 = 2 #Left Eye Lid
pwm_channel_3 = 3 #Right Eye Lid
pwm_channel_4 = 4 #Left and Right Horizontal
pwm_channel_5 = 5 #Left and Right Vertical
pwm_channel_6 = 6 #Mouth
pwm_channel_7 = 7 #Left Shoulder joint
pwm_channel_8 = 8 #Right Shoulder joint
pwm_channel_9 = 9 #Left Arm_side ways
pwm_channel_10 = 10 #Right Arm_side ways
pwm_channel_11 = 11 #Left Elbow
pwm_channel_12 = 12 #right Elbow
pwm_channel_13 = 13
pwm_channel_14 = 14
pwm_channel_15 = 15

class Face:
    
    def __init__ (self):
        print ("init")

    def Right_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Left_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Eye_Center(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
    
    def Mouth(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
        
    def Left_Eye_Lid(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
        
    def Right_Eye_Lid(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Eye_Vertical(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
    
    def Eye_Horizontal(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
    
    def Face_Reset(self):
        self.Right_Eyebrow(pwm_channel_1,degree_120)
        self.Left_Eyebrow(pwm_channel_0,degree_120)
        self.Mouth(pwm_channel_6,degree_0)
        self.Left_Eye_Lid(pwm_channel_2,degree_150)
        self.Right_Eye_Lid(pwm_channel_3,degree_60)
        self.Eye_Vertical(pwm_channel_5,degree_100)
        self.Eye_Horizontal(pwm_channel_4,degree_120)
        print("Reset is done")

def lineCallback(data):
	line = data.data
	audio_file = "/home/pi/dim_ws/src/dim/scripts/Act1/" + str(line) +".wav"

#        Mouth(pwm_channel_6,degree_60)

	if(os.path.isfile(audio_file)):
		pygame.mixer.init(44100, -16, 2, 2048)
		pygame.mixer.init()
		audio_play = pygame.mixer.Sound(audio_file)
		free_channel = pygame.mixer.find_channel()
		playing = audio_play.play()
		while playing.get_busy():
			pygame.time.wait(50)
		print("stopped")
                time.sleep(1)
		increment.publish(line)
	return

rospy.init_node("Dim")
increment = rospy.Publisher('/increment', Int32, queue_size=1)
rospy.Subscriber("/lines",Int32,lineCallback)
rospy.spin()


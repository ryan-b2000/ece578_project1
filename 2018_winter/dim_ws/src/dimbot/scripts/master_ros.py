#!/usr/bin/env python
# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

# Import the PCA9685 module.
import Adafruit_PCA9685
#import cv2
import sys
import os


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths

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

    
class Arm:
    def __init__ (self):
        print ("init")

    def right_shoulder(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def left_shoulder(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
    
    def right_biceps(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def left_biceps(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def right_hand(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def left_hand(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def normal(self,channel,degree):
        pwm.set_pwm(channel,0,degree)
	
    def Arm_Reset(self):
        Robo_arm.right_hand(pwm_channel_12,degree_150)
        Robo_arm.left_hand(pwm_channel_11,degree_60)
        time.sleep(1)
        Robo_arm.left_biceps(pwm_channel_9,degree_90)
        Robo_arm.right_biceps(pwm_channel_10,degree_180)
        time.sleep(1)
        Robo_arm.left_biceps(pwm_channel_9,degree_90)
        Robo_arm.right_shoulder(pwm_channel_8,degree_0)
        Robo_arm.left_shoulder(pwm_channel_7,degree_90)
        Robo_arm.right_hand(pwm_channel_12,degree_30)
        Robo_arm.left_hand(pwm_channel_11,degree_180)
        Robo_arm.right_biceps(pwm_channel_10,degree_180)
    
    def Arm_Initial(self):
        Robo_arm.right_hand(pwm_channel_12,degree_150)
        Robo_arm.left_hand(pwm_channel_11,degree_60)
        time.sleep(1)
        Robo_arm.right_shoulder(pwm_channel_8,degree_0)
        Robo_arm.left_shoulder(pwm_channel_7,degree_90)
        time.sleep(1)
        Robo_arm.left_biceps(pwm_channel_9,degree_120)
        Robo_arm.right_biceps(pwm_channel_10,degree_130)
        time.sleep(1)

    def Drum(self):
        i = 0
        os.system('flite -voice rms -t "Hey, this is first pattern i am composing"')
        while i < 15:
            Robo_arm.right_hand(pwm_channel_12,degree_30)
            Robo_arm.left_hand(pwm_channel_11,degree_150)
            Robo_arm.left_biceps(pwm_channel_9,degree_120)
            time.sleep(0.5)
            Robo_arm.right_hand(pwm_channel_12,degree_60)
            time.sleep(0.2)
            Robo_arm.right_hand(pwm_channel_12,degree_30)
            Robo_arm.left_hand(pwm_channel_11,degree_180)
            time.sleep(0.2)
            Robo_arm.right_hand(pwm_channel_12,degree_60)
            Robo_arm.left_hand(pwm_channel_11,degree_150)
            Robo_arm.left_biceps(pwm_channel_9,degree_120)
            time.sleep(0.2)
            i = i + 1
    
    def Drum1(self):
        os.system('flite -voice rms -t "this is second one"')
        i = 0
        j = 0
        k = 0
        while k < 3:
            Robo_arm.left_hand(pwm_channel_11,degree_150)

            while i < 10:
                Robo_arm.right_hand(pwm_channel_12,degree_30)
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                time.sleep(0.2)
                Robo_arm.right_hand(pwm_channel_12,degree_60)
                time.sleep(0.3)
                i = i + 1

            Robo_arm.right_hand(pwm_channel_12,degree_60)
            while j < 5:
                Robo_arm.left_hand(pwm_channel_11,degree_180)
                time.sleep(0.5)
                Robo_arm.left_hand(pwm_channel_11,degree_130)
                time.sleep(1)
                j = j + 1

            k = k + 1
    
    def Drum2(self):
        os.system('flite -voice rms -t "Just look at this one"')
        i = 0
        j = 0
        k = 0
        while k < 3:
            Robo_arm.left_hand(pwm_channel_11,degree_150)

            while i < 10:
                Robo_arm.right_hand(pwm_channel_12,degree_30)
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                time.sleep(0.2)
                Robo_arm.right_hand(pwm_channel_12,degree_60)
                time.sleep(0.1)
                i = i + 1

            Robo_arm.right_hand(pwm_channel_12,degree_60)
            while j < 10:
                Robo_arm.left_hand(pwm_channel_11,degree_180)
                time.sleep(0.7)
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                time.sleep(0.7)
                j = j + 1

            k = k + 1
    
    def Drum3(self):
        os.system('flite -voice rms -t "pattern three"')
        i = 0
        while i < 10:
            Robo_arm.left_hand(pwm_channel_11,degree_180)
            time.sleep(0.1)
            Robo_arm.right_hand(pwm_channel_12,degree_60)
            time.sleep(0.2)
            Robo_arm.right_hand(pwm_channel_12,degree_30)
            time.sleep(0.1)
            Robo_arm.left_hand(pwm_channel_11,degree_150)
            time.sleep(0.5)
            i = i + 1

    def Drum4(self):
        os.system('flite -voice rms -t "I bet this is Awesome"')
        i = 0
        while i < 15:
            Robo_arm.left_hand(pwm_channel_11,degree_150)
            #Robo_arm.left_biceps(pwm_channel_9,degree_150)
            Robo_arm.right_hand(pwm_channel_12,degree_60)
            time.sleep(0.2)
            Robo_arm.right_hand(pwm_channel_12,degree_30)
            Robo_arm.left_biceps(pwm_channel_9,degree_120)
            time.sleep(0.2)
            Robo_arm.left_hand(pwm_channel_11,degree_180)
            time.sleep(0.2)
            i = i + 1


        
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)



# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)
print('Moving servo on channel 0, press Ctrl-C to quit...')

Robo_arm = Arm()

def music1(data):
    Robo_arm.Drum1()
    print("working")
    
def test():    
    # Create Vision node
    rospy.init_node('arm', anonymous = True)
    rate = rospy.Rate(10)
    print("node init")
    rospy.Subscriber('music1', Int32, music1)
    rospy.spin()


if __name__ == '__main__':
    try:
        Robo_arm.Arm_Reset()
        time.sleep(3)
        Robo_arm.Arm_Initial()
        time.sleep(5)
        test()
    except rospy.ROSInterruptException:
        pass

  

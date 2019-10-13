# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import cv2
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

#Class Face contains methods for the Facial expressions
class Face:
    
    def __init__ (self):
        print ("init")

    def Right_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Left_Eyebrow(self,channel,degree):
        pwm.set_pwm(channel,0,degree)

    def Eye_Center(self,channel,degree):
        #110
        pwm.set_pwm(channel,0,degree)
    
    def Mouth(self,channel,degree):
        #60 open | 0 close
        pwm.set_pwm(channel,0,degree)
    
    def Left_Eye_Lid(self,channel,degree):
        #150 close | 90 open
        pwm.set_pwm(channel,0,degree)
    
    def Right_Eye_Lid(self,channel,degree):
        #60 close | 120 open
        pwm.set_pwm(channel,0,degree)

    def Eye_Vertical(self,channel,degree):
        #60 up | 100 down
        pwm.set_pwm(channel,0,degree)
    
    def Eye_Horizontal(self,channel,degree):
        #160 left | 80 Right
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

    def Excited(self):
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_135)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_135)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_90)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)
        os.system('flite -voice rms -t "Hey, I am Excited"')
        time.sleep(0.5)
    
    def Very_happy(self):
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_135)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_135)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_140)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_70)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_120)
        os.system('flite -voice rms -t "I am Very Happy Right now"')
        time.sleep(0.5)

    def Sleepy(self):
        Robo_face.Mouth(pwm_channel_6,degree_0)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_135)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_135)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_140)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_70)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_80)
        os.system('flite -voice rms -t "I am feeling sleepy"')
        time.sleep(0.5)
    
    def Sleep(self):
        Robo_face.Mouth(pwm_channel_6,degree_0)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_120)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_120)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_150)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_60)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_60)
        os.system('aplay snore.wav')
        time.sleep(0.5)

    def Sad(self):
        Robo_face.Mouth(pwm_channel_6,degree_45)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_140)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_140)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_130)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_85)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        os.system('flite -voice rms -t "I am sad man and really really very upset"')
        time.sleep(0.5)
    
    def Suspicious(self):
        Robo_face.Mouth(pwm_channel_6,degree_0)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_100)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_100)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_135)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_80)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        os.system('flite -voice rms -t "Whose down there hmm I am suspicious"')
        time.sleep(0.5)
    
    def Angry(self):
        Robo_face.Mouth(pwm_channel_6,degree_45)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_90)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_90)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_100)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_110)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        os.system('flite -voice rms -t "Angry about What u did to me"')
        time.sleep(0.5)
    
    def Winky(self):
        i = 0
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Left_Eyebrow(pwm_channel_0,degree_135)
        Robo_face.Right_Eyebrow(pwm_channel_1,degree_135)
        Robo_face.Left_Eye_Lid(pwm_channel_2,degree_90)
        Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)
        os.system('flite -voice rms -t "how are u doing"')
        while(i < 3):
            Robo_face.Right_Eye_Lid(pwm_channel_3,degree_60)
            Robo_face.Right_Eyebrow(pwm_channel_1,degree_90)
            time.sleep(0.5)
            Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)
            Robo_face.Right_Eyebrow(pwm_channel_1,degree_135)
            time.sleep(0.5)
            i = i + 1	
        time.sleep(0.5)

	
    
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
        Robo_arm.left_biceps(pwm_channel_9,degree_100)
        Robo_arm.right_biceps(pwm_channel_10,degree_180)
        time.sleep(1)
        Robo_arm.left_biceps(pwm_channel_9,degree_100)
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
        Robo_arm.left_biceps(pwm_channel_9,degree_135)
        Robo_arm.right_biceps(pwm_channel_10,degree_130)
        time.sleep(1)
        #Robo_arm.right_biceps(pwm_channel_10,degree_130)
        #Robo_arm.left_biceps(pwm_channel_9,degree_135)
        #Robo_arm.right_hand(pwm_channel_12,degree_90)
        #Robo_arm.left_hand(pwm_channel_11,degree_60)
        #time.sleep(1)

    def Drum(self):
        Robo_arm.right_hand(pwm_channel_12,degree_30)
        Robo_arm.left_hand(pwm_channel_11,degree_150)
        Robo_arm.left_biceps(pwm_channel_9,degree_140)
        time.sleep(0.2)
        Robo_arm.right_hand(pwm_channel_12,degree_60)
        time.sleep(0.1)
        Robo_arm.right_hand(pwm_channel_12,degree_30)
        Robo_arm.left_hand(pwm_channel_11,degree_180)
        time.sleep(0.2)
        Robo_arm.right_hand(pwm_channel_12,degree_60)
        Robo_arm.left_hand(pwm_channel_11,degree_150)
        Robo_arm.left_biceps(pwm_channel_9,degree_135)
        time.sleep(0.1)
    
    def Drum1(self):
        i = 0
        j = 0
        k = 0
        while k < 3:
            Robo_arm.left_hand(pwm_channel_11,degree_150)

            while i < 10:
                Robo_arm.right_hand(pwm_channel_12,degree_30)
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                Robo_arm.left_biceps(pwm_channel_9,degree_140)
                time.sleep(0.2)
                Robo_arm.right_hand(pwm_channel_12,degree_60)
                time.sleep(0.1)
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
                time.sleep(1)
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                time.sleep(1)
                j = j + 1

            k = k + 1
        

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


#if __name__ == "main":

# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)
print('Moving servo on channel 0, press Ctrl-C to quit...')

k = 0

Robo_face = Face()
Robo_arm = Arm()

Robo_face.Face_Reset()
Robo_arm.Arm_Reset()
time.sleep(5)


Robo_face.Excited()
time.sleep(2)
Robo_face.Winky()
time.sleep(2)
Robo_face.Sad()
time.sleep(2)
Robo_face.Sleepy()
time.sleep(2)
Robo_face.Sleep()
time.sleep(2)
Robo_face.Suspicious()
time.sleep(2)
Robo_face.Angry()
time.sleep(2)
Robo_face.Very_happy()
time.sleep(2)

Robo_face.Face_Reset()
Robo_face.Left_Eye_Lid(pwm_channel_2,degree_90)
Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)

Robo_arm.Arm_Initial()
time.sleep(1)


Robo_arm.Drum1()
time.sleep(5)
Robo_arm.Drum2()
    
	
#Robo_face.Face_Reset()
Robo_arm.Arm_Reset()
time.sleep(1)

#cascPath = sys.argv[1]
#faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    Robo_face.Winky()
 #   time.sleep(0.5)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
#        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        Robo_face.Mouth(pwm_channel_6,degree_60)
        os.system('flite -t "Hi"')
        ##GPIO.output(18,GPIO.HIGH)
        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()

cv2.destroyAllWindows()
    
  

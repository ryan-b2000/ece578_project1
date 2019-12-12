
'''
Class: ECE 510 Intelligent Robotics
Author: Ming Ma & Ting Wang & Xiaoqiao Mu
Date: 6/13/2019
game_program: This is a program about the paper, scissos, rock game, which is interactive game.
The robot receives the user's gesture from the camera and produce his gesture randomly.
Finally, the robot can declare the game result according to the game rule.
'''
#! /usr/bin/env python3
#Reference Design: https://github.com/athena15/project_kojak
import copy
import cv2
import numpy as np
from keras.models import load_model
import pygame
import time
from keras.preprocessing import image
import os
from random import randint
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import threading            #multithreading library

pwm = Adafruit_PCA9685.PCA9685()
# set the frequency of the system as 50Hz
pwm.set_pwm_freq(50)
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
degree_170 = 480    #added degree
degree_175 = 490    #added degree
degree_180 = 505
degree_190 = 528
degree_200 = 551

#pwm channel number on PWM Driver
pwm_channel_0 = 0 #Right Eyebrow
pwm_channel_1 = 1 #Left Eyebrow
pwm_channel_2 = 2 #Right Eye Lid
pwm_channel_3 = 3 #Left Eye Lid
pwm_channel_4 = 4 #Left and Right Horizontal
pwm_channel_5 = 5 #Left and Right Vertical
pwm_channel_6 = 6 #Mouth
pwm_channel_7 = 7 #Right Shoulder joint
pwm_channel_8 = 8 #Left Shoulder joint
pwm_channel_9 = 9 #Right Arm_side ways
pwm_channel_10 = 10 #Left Arm_side ways
pwm_channel_11 = 11 #Right Elbow
pwm_channel_12 = 12 #Left Elbow
pwm_channel_13 = 13
pwm_channel_14 = 14
pwm_channel_15 = 15

#=======================    ROBOT EXPRESSION SETTING ============================

#the class provide the face expression after declaring the result
class Game_Face:
        
    def Left_Eyebrow(self,channel,degree):
        #80 \  | 140 /  | 120 flat -
        pwm.set_pwm(channel,0,degree)

    def Right_Eyebrow(self,channel,degree):
        #80 \  | 140 /  | 120 flat -
        pwm.set_pwm(channel,0,degree)

    def Eye_Center(self,channel,degree):
        #110
        pwm.set_pwm(channel,0,degree)
    
    def Mouth(self,channel,degree):
        #60 open | 0 close
        pwm.set_pwm(channel,0,degree)
    
    def Right_Eye_Lid(self,channel,degree):
        #150 close | 90 open
        pwm.set_pwm(channel,0,degree)
    
    def Left_Eye_Lid(self,channel,degree):
        #60 close | 120 open
        pwm.set_pwm(channel,0,degree)

    def Eye_Vertical(self,channel,degree):
        #80 up | 120 down | 100 center
        pwm.set_pwm(channel,0,degree)
    
    def Eye_Horizontal(self,channel,degree):
        #160 left | 80 Right | 110 center
        pwm.set_pwm(channel,0,degree)

    def Face_Reset(self):
        self.Left_Eyebrow(pwm_channel_1,degree_120)
        self.Right_Eyebrow(pwm_channel_0,degree_120)
        self.Mouth(pwm_channel_6,degree_0)
        self.Right_Eye_Lid(pwm_channel_2,degree_90)
        self.Left_Eye_Lid(pwm_channel_3,degree_120)
        self.Eye_Vertical(pwm_channel_5,degree_100)
        self.Eye_Horizontal(pwm_channel_4,degree_110)
        print("Reset is done")

    def Excited(self):
        self.Mouth(pwm_channel_6,degree_60)
        self.Right_Eyebrow(pwm_channel_0,degree_135)
        self.Left_Eyebrow(pwm_channel_1,degree_135)
        self.Right_Eye_Lid(pwm_channel_2,degree_90)
        self.Left_Eye_Lid(pwm_channel_3,degree_120)
        os.system('flite -voice rms -t "Hey, I am Excited"')
        time.sleep(0.5)
    
    def Very_happy(self):
        self.Mouth(pwm_channel_6,degree_60)
        self.Eye_Vertical(pwm_channel_5,degree_100)
        self.Right_Eyebrow(pwm_channel_0,degree_135)
        self.Left_Eyebrow(pwm_channel_1,degree_135)
        self.Right_Eye_Lid(pwm_channel_2,degree_140)
        self.Left_Eye_Lid(pwm_channel_3,degree_70)
        self.Eye_Vertical(pwm_channel_5,degree_120)
        speaking('Do not be sad. You will win next time! Hahahahahahaha')
        time.sleep(0.5)
   

    def Sad(self):
        Robo_face.Mouth(pwm_channel_6,degree_45)
        Robo_face.Right_Eyebrow(pwm_channel_0,degree_140)
        Robo_face.Left_Eyebrow(pwm_channel_1,degree_140)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_130)
        Robo_face.Left_Eye_Lid(pwm_channel_3,degree_85)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        speaking('I will win next time!')
        time.sleep(0.5)
    
    # wink both eyes together
    def Winky(self):
        i = 0
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Right_Eyebrow(pwm_channel_0,degree_135)
        Robo_face.Left_Eyebrow(pwm_channel_1,degree_135)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_90)
        Robo_face.Left_Eye_Lid(pwm_channel_3,degree_120)
        while(i < 2):
            Robo_face.Left_Eye_Lid(pwm_channel_3,degree_60)
            Robo_face.Right_Eye_Lid(pwm_channel_2,degree_150)
            Robo_face.Left_Eyebrow(pwm_channel_1,degree_90)
            Robo_face.Right_Eyebrow(pwm_channel_0,degree_90)
            time.sleep(0.3)
            Robo_face.Left_Eye_Lid(pwm_channel_3,degree_120)
            Robo_face.Right_Eye_Lid(pwm_channel_2,degree_90)
            Robo_face.Left_Eyebrow(pwm_channel_1,degree_135)
            Robo_face.Right_Eyebrow(pwm_channel_0,degree_135)
            time.sleep(0.3)
            i = i + 1	
            time.sleep(0.3)

    def Angry(self):
        Robo_face.Mouth(pwm_channel_6,degree_45)
        self.Eye_Horizontal(pwm_channel_4,degree_160)
        time.sleep(1)
        self.Eye_Horizontal(pwm_channel_4,degree_80)
        time.sleep(1)
        self.Eye_Horizontal(pwm_channel_4,degree_110)
        time.sleep(0.3)
        Robo_face.Right_Eyebrow(pwm_channel_0,degree_90)
        Robo_face.Left_Eyebrow(pwm_channel_1,degree_90)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_100)
        Robo_face.Left_Eye_Lid(pwm_channel_3,degree_110)
        Robo_face.Eye_Vertical(pwm_channel_5,degree_100)
        speaking('I will win next time!')
        time.sleep(0.5)

    # Wink left and right eyes by turns
    def Winky_new(self): #left 90 open 150 close right 120 open 60 close brow 120 h 135\ 90 / 
        i = 0
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Right_Eyebrow(pwm_channel_0,degree_120)
        Robo_face.Left_Eyebrow(pwm_channel_1,degree_120)
        Robo_face.Right_Eye_Lid(pwm_channel_2,degree_90)
        Robo_face.Left_Eye_Lid(pwm_channel_3,degree_120)
        while(i < 3):
            Robo_face.Left_Eye_Lid(pwm_channel_3,degree_120)
            Robo_face.Right_Eye_Lid(pwm_channel_2,degree_150)
            Robo_face.Left_Eyebrow(pwm_channel_1,degree_110)
            Robo_face.Right_Eyebrow(pwm_channel_0,degree_135)
            time.sleep(1)
            Robo_face.Left_Eye_Lid(pwm_channel_3,degree_60)
            Robo_face.Right_Eye_Lid(pwm_channel_2,degree_90)
            Robo_face.Left_Eyebrow(pwm_channel_1,degree_135)
            Robo_face.Right_Eyebrow(pwm_channel_0,degree_110)
            time.sleep(1)
            i = i + 1	
            time.sleep(0.3)

class Game_Gesture:
    #Right Shoulder joint   channel_7
    #Left Shoulder joint    channel_8
    #Right Arm_side ways    channel_9   |   outside 90 | inside 120 
    #Left Arm_side ways     channel_10
    #Right Elbow            channel_11  |   High   150 | Low 170 
    #Left Elbow             channel_12
    def move (self,channel,degree):
        pwm.set_pwm(channel,0,degree)
    def Arm_Reset(self):
        self.move(pwm_channel_12,degree_150)
        self.move(pwm_channel_11,degree_150)
        time.sleep(1)
        self.move(pwm_channel_9,degree_120)
        self.move(pwm_channel_10,degree_180)
        time.sleep(1)
        self.move(pwm_channel_9,degree_120)
        self.move(pwm_channel_8,degree_0)
        self.move(pwm_channel_7,degree_90)
        self.move(pwm_channel_12,degree_30)
        self.move(pwm_channel_11,degree_150)
        self.move(pwm_channel_10,degree_180)
    #  beat the drum once  
    def Paper(self):
        self.move(pwm_channel_11,degree_170) #low
        time.sleep(1)
        self.move(pwm_channel_11,degree_150) #high
        time.sleep(1)
    #  beat the drum twice  
    def Scissors(self):
        self.move(pwm_channel_11,degree_170) #low
        time.sleep(0.5)
        self.move(pwm_channel_11,degree_150) #high
        time.sleep(0.8)
        self.move(pwm_channel_11,degree_170) #low
        time.sleep(0.5)
        self.move(pwm_channel_11,degree_150) #high
        time.sleep(0.8)
    #   beat the side of drum once
    def Rock(self):
        pwm.set_pwm(pwm_channel_9,0,degree_90) #outside
        time.sleep(1)
        self.move(pwm_channel_11,degree_175) #low 
        time.sleep(1)
        pwm.set_pwm(pwm_channel_9,0,degree_120) #inside
        time.sleep(1)
        pwm.set_pwm(pwm_channel_9,0,degree_85) #outside
        time.sleep(1)
        self.move(pwm_channel_11,degree_150) #high 
        time.sleep(1)
        pwm.set_pwm(pwm_channel_9,0,degree_120) #inside
        time.sleep(1)
        
#The function makes robot speak like a human, say words and at the same time, open and close at same time  
def speaking(content):
    def speak(content):
        global Flag
        Flag = 1
        #os.system('flite -t "%s"'%content)
        os.system('flite -voice rms -t "%s"'%content)
        Flag = 0
    def mouth():
        #mouth
        while Flag:
            pwm.set_pwm(6,0,240)
            time.sleep(0.6)
            pwm.set_pwm(6,0,102)
            time.sleep(0.6)
    # Use multithreading library named threading
    thread1 = threading.Thread(target=lambda: speak(content))
    thread2 = threading.Thread(target=mouth)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
#=======================    ROBOT EXPRESSION SETTING ============================

#=============================    GAME SETTING  =====================================

def remove_background(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

def predict_binaryImage(image1):
    predict_image = image.load_img(image1, target_size=(64,64))
    predict_image = image.img_to_array(predict_image)
    predict_image = np.expand_dims(predict_image, axis = 0)
    result = model.predict(predict_image)
    if result[0][0] >= 0.6:
        prediction = 'paper'
        return prediction, result[0][0]
    elif result[0][1] >= 0.6:
        prediction = 'rock'
        return prediction, result[0][1]
    elif result[0][2] >= 0.6:
        prediction = 'scissors'
        return prediction, result[0][2]
    else:
        prediction = 'invalid'
        return prediction, result[0][2]
    print("Prediction: " + prediction + "Score: " + str(result[0]))
	
def generate_randGesture():
    index = randint(0,2)
    if (index == 0):
        Robo_gesture.Paper()
        speaking('Paper')
    elif (index == 1):
        Robo_gesture.Rock()
        speaking('Rock')
    elif (index == 2):
        Robo_gesture.Scissors()
        speaking('Scissors')
    return gesture[index]
    
def game_rule(user_gest, robot_gest):
    if user_gest == 'paper' and robot_gest == 'paper':
        return 'No Winner!'
    elif user_gest == 'paper' and robot_gest == 'rock':
        return 'You Win!'
    elif user_gest == 'paper' and robot_gest == 'scissors':
        return 'I Win!'
    elif user_gest == 'rock' and robot_gest == 'paper':
        return 'I Win!'
    elif user_gest == 'rock' and robot_gest == 'rock':
        return 'No Winner!'
    elif user_gest == 'rock' and robot_gest == 'scissors':
        return 'You Win!'
    elif user_gest == 'scissors' and robot_gest == 'paper':
        return 'You Win!'
    elif user_gest == 'scissors' and robot_gest == 'rock':
        return 'I Win!'
    elif user_gest == 'scissors' and robot_gest == 'scissors':
        return 'No Winner!'

# main loop of game setting
def main_game():
    
    global Predict, action, accuracy, robot_gesture, gesture, img_counter
    global save_images, selected_gesture, model, cap_region_x_begin, cap_region_y_end, threshold
    global blurValue, bgSubThreshold, learningRate, isBgCaptured, triggerSwitch
    global bgModel, Robo_face, Robo_gesture
    
    # General Settings
    Predict = ''
    action = ''
    accuracy = 0
    robot_gesture = ''
    gesture = ['paper', 'rock', 'scissors']
    img_counter = 500


    save_images, selected_gesture = True, 'gesture'


    model = load_model('/home/pi/pyaudio/Spring_2019/HW2model.h5')

    # parameters
    cap_region_x_begin = 0.5  # start point/total width
    cap_region_y_end = 0.8  # start point/total width
    threshold = 60  # binary threshold
    blurValue = 41  # GaussianBlur parameter
    bgSubThreshold = 50
    learningRate = 0

    # variableslt
    isBgCaptured = 0  # bool, whether the background captured
    triggerSwitch = False  # if true, keyboard simulator works
    count = 0
    enable =0
    end = 0

    #Welcome
    speaking('I am glad to play a rock, scissors and paper game with you!')

    #initialize robot's face and gesture
    Robo_face=Game_Face()
    Robo_face.Face_Reset()
    Robo_gesture = Game_Gesture()
    Robo_gesture.Arm_Reset()
    
    # Camera
    camera = cv2.VideoCapture(0)
    camera.set(10, 200)


    while camera.isOpened():

        count += 1
        
        ret, frame = camera.read()
        frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
        frame = cv2.flip(frame, 1)                      # flip the frame horizontally
        cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                  (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)

        cv2.imshow('original', frame)

        # Run once background is captured
        if isBgCaptured == 1:
            img = remove_background(frame)
            img = img[0:int(cap_region_y_end * frame.shape[0]),
                  int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI

            # convert the image into binary image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
            ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    
            # get the contours
            thresh1 = copy.deepcopy(thresh)
            _, contours,_ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            length = len(contours)
            maxArea = -1
            if length > 0:
                for i in range(length):  # find the biggest contour (according to area)
                    temp = contours[i]
                    area = cv2.contourArea(temp)
                    if area > maxArea:
                        maxArea = area
                        ci = i

                res = contours[ci]
                hull = cv2.convexHull(res)
                drawing = np.zeros(img.shape, np.uint8)
                cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
                cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

            cv2.imshow('output', drawing)

        # The face works on waiting
        if count == 3 or count ==6:
            Robo_face.Face_Reset()
            Robo_face.Winky()
            
        if count == 9:
            speaking("I am capturing background!")

        # Get the background enable be 1
        # capture the background
        if count == 10:  
            bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
            time.sleep(2)
            isBgCaptured = 1
            print('Background captured')

        if count == 16:
            speaking("PLease show your gesture after 3 seconds!")

        if count == 19:

            speaking('Three')
            time.sleep(1)

        if count == 20:

            speaking('Two')
            time.sleep(1)
            
        if count == 21:
            speaking('One')
            speaking("Start!")
            time.sleep(1)
            
        # Start receiving the input gesture
        if count == 30:
            enable = 1

        # Start running the end progress
        if count == 40:
            end = 1         # end enable
            time.sleep(1)

  

        # Keyboard OP
        k = cv2.waitKey(10)
        if end == 1:  #If end enable can be 1
            #Close all the windows
            cv2.destroyAllWindows()
            #Delete all files in the folders to release spaces.
            filelist = [ f for f in os.listdir('/home/pi/pyaudio/Spring_2019/frame/') if f.endswith(".jpg") ]
            for f in filelist:
                os.remove(os.path.join('/home/pi/pyaudio/Spring_2019/frame/', f))
            break
            
            
        if enable == 1:
            # If input enable can be 1
            cv2.imshow('original', frame)
            # copies 1 channel BW image to all 3 RGB channels
            target = np.stack((thresh,) * 3, axis=-1)
            target = cv2.resize(target, (224, 224))
            target = target.reshape(1, 224, 224, 3)

            # save the input gesture image into the frame folder
            if save_images:

                img_name2 = './frame/gesture_{}.jpg'.format(img_counter)
                cv2.imwrite(img_name2, thresh)
                print("{} written".format(img_name2))

                image_address = '/home/pi/pyaudio/Spring_2019/frame/gesture_{}.jpg'
                image_add = image_address.format(img_counter)
                Predict, accuracy = predict_binaryImage(image_add)
                if Predict == 'invalid':
                    speaking('The gesture can not be recogenized')
                    try:
                        cv2.destroyWindow('Predict')
                    except:
                        pass
                else:
                    # generate random gesture
                    robot_gesture = generate_randGesture()
                    # generate the game result
                    game_result = game_rule(Predict, robot_gesture)
                    cv2.putText(thresh, "Prediction: {} ({}%)".format(Predict,accuracy*100), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))
                    cv2.putText(thresh, "Robot: {}".format(robot_gesture), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))
                    cv2.putText(thresh, "Result: {}".format(game_result), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))
                    cv2.imshow('Predict', thresh)
                    speaking(game_result)

                    # generate the Robot's result expression
                    if(game_result == "You Win!"):
                        Robo_face.Face_Reset()
                        time.sleep(0.6)
                        Robo_face.Angry()
                        time.sleep(0.6)
                        Robo_face.Face_Reset()
                    elif(game_result == "I Win!"):
                        Robo_face.Face_Reset()
                        time.sleep(0.6)
                        Robo_face.Very_happy()
                        time.sleep(0.6)
                        Robo_face.Face_Reset()
                    elif(game_result == "No Winner!"):
                        Robo_face.Face_Reset()
                        time.sleep(0.6)
                        Robo_face.Winky_new()
                        time.sleep(0.6)
                        Robo_face.Face_Reset()                       


                    img_counter += 1
            enable = 0
#=============================    GAME SETTING  ==================================

if __name__ == "__main__":  
    main_game()






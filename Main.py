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

import MoveClass
import FaceClass
  







# ======================= ROBOT SPEAKING ======================= #    
#
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
            PCA9685.set_pwm(6,0,240)
            time.sleep(0.6)
            PCA9685.set_pwm(6,0,102)
            time.sleep(0.6)
    # Use multithreading library named threading
    thread1 = threading.Thread(target=lambda: speak(content))
    thread2 = threading.Thread(target=mouth)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    

# ======================= GAME FUNCTIONS ======================= #

# Generate the rock/paper/scissors gesture the robot uses for the game	
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
    

# Determine who won the game based on the gesture from the user and the
# gesture for the robot
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


# ======================= IMAGE PROCESSING ======================= #
#
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



# ================================================================ #
# ============================ MAIN ============================== #
# ================================================================ #
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
    threshold = 60  		# binary threshold
    blurValue = 41  		# GaussianBlur parameter
    bgSubThreshold = 50
    learningRate = 0

    # variableslt
    isBgCaptured = 0  # bool, whether the background captured
    triggerSwitch = False  # if true, keyboard simulator works
    count = 0
    enable =0
    end = 0

    # Welcome
    speaking('I am glad to play a rock, scissors and paper game with you!')

    #initialize robot's face and gesture
    Robo_face = Game_Face()
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


# ================================================================ #
if __name__ == "__main__":  
    main_game()
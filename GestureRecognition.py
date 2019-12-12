#! /usr/bin/env python3
# Reference Design: https://github.com/athena15/project_kojak
import copy
import cv2
import numpy as np
from keras.models import load_model
import pygame
import time
from keras.preprocessing import image
import os
from random import randint


def predict_binaryImage(image1):
    # prediction = ''
    predict_image = image.load_img(image1, target_size=(64, 64))
    predict_image = image.img_to_array(predict_image)
    predict_image = np.expand_dims(predict_image, axis=0)
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
    index = randint(0, 2)
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


def remove_background(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


def main_game(frame):
    global Predict, action, accuracy, robot_gesture, gesture, img_counter
    global save_images, selected_gesture, model, cap_region_x_begin, cap_region_y_end, threshold
    global blurValue, bgSubThreshold, learningRate, isBgCaptured, triggerSwitch
    global bgModel

    # General Settings
    Predict = ''
    action = ''
    accuracy = 0
    robot_gesture = ''
    gesture = ['paper', 'rock', 'scissors']
    img_counter = 500

    save_images, selected_gesture = True, 'peace'

    model = load_model('/home/zhe/PycharmProjects/server/New.h5')

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

    # Camera
    camera = cv2.VideoCapture(0)
    camera.set(10, 200)

    while True:
        frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
        frame = cv2.flip(frame, 1)  # flip the frame horizontally
        cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                      (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)

        cv2.imshow('original', frame)

        # Run once background is captured
        if isBgCaptured == 1:
            img = remove_background(frame)
            img = img[0:int(cap_region_y_end * frame.shape[0]),
                  int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
            # cv2.imshow('mask', img)

            # convert the image into binary image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
            # cv2.imshow('blur', blur)
            ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            # ~ Predict, accuracy = predict_binaryImage(thresh);
            # Add prediction and action text to thresholded image
            # cv2.putText(thresh, f"Prediction: {prediction} ({score}%)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
            # cv2.putText(thresh, f"Action: {action}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))  # Draw the text
            # Draw the text

            # ~ cv2.putText(thresh, f"Prediction: {Predict} ({accuracy}%)", (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
            # ~ (255, 255, 255))
            # ~ cv2.putText(thresh, f"Action: {action}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
            # ~ (255, 255, 255))  # Draw the text
            # ~ cv2.imshow('ori', thresh)

            # get the contours
            thresh1 = copy.deepcopy(thresh)
            contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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

        # Keyboard OP
        k = cv2.waitKey(10)
        if k == 27:  # press ESC to exit all windows at any time
            # Delete all files in the folders to release spaces.
            cv2.destroyAllWindows()
            # cv2.VideoCapture(0).release()
            filelist = [f for f in os.listdir('/home/zhe/PycharmProjects/server/frame/') if f.endswith(".jpg")]
            for f in filelist:
                os.remove(os.path.join('/home/zhe/PycharmProjects/server/frame/', f))
            break
        elif k == ord('b'):  # press 'b' to capture the background
            bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
            # ~ b.set_light(6, on_command)
            time.sleep(2)
            isBgCaptured = 1
            print('Background captured')


        elif k == ord('r'):  # press 'r' to reset the background
            time.sleep(1)
            bgModel = None
            triggerSwitch = False
            isBgCaptured = 0
            print('Reset background')

        elif k == 32:
            # If space bar pressed
            cv2.imshow('original', frame)
            # copies 1 channel BW image to all 3 RGB channels
            target = np.stack((thresh,) * 3, axis=-1)
            target = cv2.resize(target, (224, 224))
            target = target.reshape(1, 224, 224, 3)

            if save_images:
                # ~ img_name = f"./frames/drawings/drawing_{selected_gesture}_{img_counter}.jpg".format(
                # ~ img_counter)
                # ~ cv2.imwrite(img_name, drawing)
                # ~ print("{} written".format(img_name))

                img_name2 = './home/zhe/PycharmProjects/server/peace_{}.jpg'.format(img_counter)
                cv2.imwrite(img_name2, thresh)
                print("{} written".format(img_name2))

                # ~ img_name3 = f"./frames/masks/mask_{selected_gesture}_{img_counter}.jpg".format(
                # ~ img_counter)
                # ~ cv2.imwrite(img_name3, img)
                # ~ print("{} written".format(img_name3))

                image_address = '/home/zhe/PycharmProjects/server/frame/peace_{}.jpg'
                image_add = image_address.format(img_counter)
                Predict, accuracy = predict_binaryImage(image_add)
                if Predict == 'invalid':
                    print('The gesture can not be recogenized')
                    try:
                        cv2.destroyWindow('Predict')
                    except:
                        pass
                else:
                    robot_gesture = generate_randGesture()
                    game_result = game_rule(Predict, robot_gesture)
                    cv2.putText(thresh, "Prediction: {} ({}%)".format(Predict, accuracy * 100), (10, 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))
                    cv2.putText(thresh, "Robot: {}".format(robot_gesture), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                (255, 255, 255))
                    cv2.putText(thresh, "Result: {}".format(game_result), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                (255, 255, 255))
                    cv2.imshow('Predict', thresh)

                    img_counter += 1



if __name__ == "__main__":
    main_game()





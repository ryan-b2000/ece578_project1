#! /usr/bin/env python3

# Handles all the OpenCV and image processing from the camera


# Initialize camera
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

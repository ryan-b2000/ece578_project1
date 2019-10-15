from __future__ import division
import speech_recognition as sr
from gtts import gTTS
#quiet the endless 'insecurerequest' warning
import RPi.GPIO as GPIO
import time
import urllib3
import Adafruit_PCA9685
import cv2
import sys
import os
#import board
import neopixel
import numpy as np
import math
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer

# global defines
music_regexp = re.compile(r'music')
flirt_regexp = re.compile(r'flirt')
happy_regexp = re.compile(r'happy')

first = 0

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

cap = cv2.VideoCapture(0)
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
degree_190 = 528
degree_200 = 551

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




def redOn():
    GPIO.output(23,GPIO.HIGH)

def redOff():
    GPIO.output(23,GPIO.LOW)

def yellowOn():
    GPIO.output(15, GPIO.HIGH)

def yellowOff():
    GPIO.output(15,GPIO.LOW)

def greenOn():
    GPIO.output(18, GPIO.HIGH) # Turn on

def greenOff():
    GPIO.output(18, GPIO.LOW) # Turn off
    #sleep(1) # Sleep for 1 second

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23,GPIO.OUT, initial=GPIO.LOW)

mixer.init()

def detect_intent_texts(project_id, session_id, texts, language_code):
    yellowOn()
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(session=session, query_input=query_input)
                      
        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        yellowOff()
        # check if question mark, break up sentence if necessary
        # question_pattern = re.compile(r'(?P<question>[\s\w\d]+\?)(?P<answer>[\s\w\d]+)')
        # is_question = question_pattern.search(response.query_result.fulfillment_text)
        # if is_question:
        #     print("this was a question")
        #     question = is_question.group('question')
        #     speech_command = "flite -t \"" + question +"\""
        #     os.system(speech_command)
        redOn()
        speech_command = "flite -t \"" + response.query_result.fulfillment_text + "\""
        os.system(speech_command)
        redOff()    

       
def detect_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        greenOn()
        audio = r.listen(source,phrase_time_limit=5)
        greenOff()
        # Speech recognition using Google Speech Recognition                                                                                         
        try:
            input_speech = r.recognize_google(audio)
        except sr.UnknownValueError:
            input_speech = ""
            print("Google Speech Recognition could not understand audio")
            pass
        except sr.RequestError as e:
            input_speech = ""
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            pass

    return input_speech


#Class Face contains methods for the Facial expressions
class Face:
    
    #def __init__ (self):
        #print ("init")
        
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
        self.Left_Eye_Lid(pwm_channel_2,degree_90)
        self.Right_Eye_Lid(pwm_channel_3,degree_120)
        self.Eye_Vertical(pwm_channel_5,degree_100)
        self.Eye_Horizontal(pwm_channel_4,degree_110)
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
        os.system('flite -voice rms -t "Whose down there, I am suspicious"')
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
        os.system('flite -voice rms -t "you are a fine looking human"')
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
    
    #def __init__ (self):
        #print ("init")

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
                Robo_arm.right_hand(pwm_channel_12,degree_0) #was 30
                Robo_arm.left_hand(pwm_channel_11,degree_150)
                time.sleep(1)
                Robo_arm.right_hand(pwm_channel_12,degree_60)
                time.sleep(1)
                i = i + 1

            Robo_arm.right_hand(pwm_channel_12,degree_30) #was 60
            while j < 5:
                Robo_arm.left_hand(pwm_channel_11,degree_180) 
                time.sleep(1)
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
                Robo_arm.left_hand(pwm_channel_11,degree_200)
                time.sleep(0.4)
                Robo_arm.left_hand(pwm_channel_11,degree_130)
                time.sleep(0.4)
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

def keyword_check(input_speech):
    music = False
    flirt = False
    happy = False

    if music_regexp.search(input_speech):
        music = True
    if flirt_regexp.search(input_speech):
        flirt = True
    if happy_regexp.search(input_speech):
        happy = True
    
    return music, flirt, happy


def keyword_response(music, flirt,happy):
    if (music and flirt and happy):
        print("im not able to drum and flirt at the same time, I'm not god")
    
    elif music:
        print ("watch me drum")
        # Set frequency to 50hz, good for
        #pwm.set_pwm_freq(50)  #servos.pwm.set_pwm_freq(50)
        #k=0
        #Robo_arm.Arm_Initial()
        #Robo_arm = Arm()
        #Robo_face = Face()
        Robo_arm = Arm()
        Robo_arm.Arm_Initial()
        Robo_arm.Drum3()
        time.sleep(4)
    
    elif happy:
        print ("i'm happy")
        # Set frequency to 50hz, good for
        #pwm.set_pwm_freq(50)  #servos.pwm.set_pwm_freq(50)
        #k=0
        #Robo_arm.Arm_Initial()
        #Robo_arm = Arm()
        k = 0
        Robo_face = Face()
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Very_happy()
        time.sleep(1)
        Robo_face.Mouth(pwm_channel_6,degree_0)
        Robo_face.Face_Reset()
        robo_face = Face()
        time.sleep(2)
	
    elif flirt:
        print ("watch me flirt")
        # Set frequency to 50hz, good for
        #pwm.set_pwm_freq(50)  #servos.pwm.set_pwm_freq(50)
        #k = 0
        #pwm.set_pwm_freq(50)
        #k = 0
        k=0
        Robo_face = Face()
        Robo_face.Mouth(pwm_channel_6,degree_60)
        Robo_face.Winky()
        Robo_face.Mouth(pwm_channel_6,degree_0)
        time.sleep(2)


def speechRec():
    # get input from user
    input_speech = detect_audio()
    print ("you said: %s" %input_speech)
            
    # check if keyword was used
    music, flirt, happy = keyword_check(input_speech)
            
    # if keyword used, respond appropriately
    if (music or flirt or happy):
        keyword_response(music, flirt,happy)
            
    # if keyword not used, and input_speech is not blank, trigger dialog flow
    if (input_speech != "" and not music and not flirt and not happy):
        Robo_face.Mouth(pwm_channel_6,degree_60)
        detect_intent_texts("robotics-test-agent", 123, [input_speech], "en")
        Robo_face.Mouth(pwm_channel_6,degree_0)
	#print("what you said: %s"  %input_speech)
                
        #pass input speech to dialog flow and return google's response
        #google_response = detect_intent_texts("robotics-test-agent", 123, [input_speech], "en")
        # print("what google said is: %s" %google_response)
                
        # respond with voice
        speech_command = "flite -t \"" + google_response + "\""
        print(speech_command)
        os.system(speech_command)
            
	# no speech detected
        if (input_speech == ""):
            print ("no speech detected")



while (1):
    try:
        if (first == 0):
            pwm.set_pwm_freq(50)
            k = 0
            Robo_face = Face()
            Robo_arm = Arm()
            first = 1
        
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
          
        #define region of interest
        roi=frame[100:300, 100:300] 

                                                                    
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        #define range of skin color in HSV
        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)
        
        #extract skin colur imagw  
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
   
        
        #extrapolate the hand to fill dark spots within
        mask = cv2.dilate(mask,kernel,iterations = 4)
        
        #blur the image
        mask = cv2.GaussianBlur(mask,(5,5),100) 
        
        #find contours
        _,contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
        #find contour of max area(hand)
        cnt = max(contours, key = lambda x: cv2.contourArea(x))
        
        #approx the contour a little
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)
       
        #make convex hull around hand
        hull = cv2.convexHull(cnt)
        
        #define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
      
        #find the percentage of area not covered by hand in convex hull
        arearatio=((areahull-areacnt)/areacnt)*100
    
        #find the defects in convex hull with respect to hand
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        
        # l = no. of defects
        l=0
        
        #code for finding no. of defects due to fingers
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt= (100,180)
            
            
            # find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            
            #distance between point and convex hull
            d=(2*ar)/a
            
            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            
        
            # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)
            
            #draw lines around hand
            cv2.line(roi,start, end, [0,255,0], 2)
            
            
        #l+=1
        print(l)        
        #print corresponding gestures which are in their ranges
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==1:
        
            if areacnt<2000:
                #cv2.putText(frame,'Use hand signal in box',(0,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA) 
               
 

            else:
                if arearatio<12:
                    #cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)                   
                    cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                    cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
                    cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA) 
                else:
                    #cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                    cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
                    cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA)
                    #l+=1 
	
        elif l==2:
            speechRec()
            if arearatio<27:
                #cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
                cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA)



        elif l==3:
            # get input from user
            input_speech = detect_audio()
            print ("you said: %s" %input_speech)
            
            # check if keyword was used
            music, flirt, happy = keyword_check(input_speech)
            
            # if keyword used, respond appropriately
            if (music or flirt or happy):
                keyword_response(music, flirt,happy)
            
            # if keyword not used, and input_speech is not blank, trigger dialog flow
            if (input_speech != "" and not music and not flirt and not happy):
                Robo_face.Mouth(pwm_channel_6,degree_60)
                detect_intent_texts("robotics-test-agent", 123, [input_speech], "en")
                Robo_face.Mouth(pwm_channel_6,degree_0)
		#print("what you said: %s"  %input_speech)
                
                #pass input speech to dialog flow and return google's response
                #google_response = detect_intent_texts("robotics-test-agent", 123, [input_speech], "en")
               # print("what google said is: %s" %google_response)
                
                # respond with voice
                speech_command = "flite -t \"" + google_response + "\""
                print(speech_command)
                os.system(speech_command)
            
	    # no speech detected
            if (input_speech == ""):
                print ("no speech detected")

            
        elif l==4:
            #cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA) 
            cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA)



        elif l==5:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            Robo_face.Left_Eye_Lid(pwm_channel_2,degree_90)
            Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)
            time.sleep(0.5)
            Robo_face.Left_Eye_Lid(pwm_channel_2,degree_150)
            Robo_face.Right_Eye_Lid(pwm_channel_3,degree_60)
            time.sleep(0.5)
            Robo_face.Left_Eye_Lid(pwm_channel_2,degree_90)
            Robo_face.Right_Eye_Lid(pwm_channel_3,degree_120)
            time.sleep(0.5)
            
        elif l==6:
            #cv2.putText(frame,'reposition',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA)


        else :
            cv2.putText(frame,'1. Place 2 or 3 fingers in box.',(10,50), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'2. Ask me a question when the LED',(10,350), font, 1, (0,0,255), 3, cv2.LINE_AA)
            cv2.putText(frame,'   on my neck turns green.',(10,390), font, 1, (0,0,255), 3, cv2.LINE_AA)

        redOff()
        greenOff()
        yellowOff()
       # time.sleep(0.6)
        #show the windows
      #cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
 
    except:
        pass

    
   
cv2.destroyAllWindows()
cap.release()



#! /usr/bin/python3

import cv2
import random
from datetime import datetime
from BotInteraction import *
from ArmManager import arms
from GestureRecognition import *


def generate_randGesture():
    gesture = ['rock', 'paper', 'scissors']
    index = random.randint(0, 2)
    return gesture[index]

def game_rule(user_gest, robot_gest):
    if user_gest == 'paper' and robot_gest == 'paper':
        print("Tied")
        botTied()
    elif user_gest == 'paper' and robot_gest == 'rock':
        print("Bot Loser")
        botLoser()
    elif user_gest == 'paper' and robot_gest == 'scissors':
        print("Bot Winner")
        botWinner()
    elif user_gest == 'rock' and robot_gest == 'paper':
        print("Bot Winner")
        botWinner()
    elif user_gest == 'rock' and robot_gest == 'rock':
        print("Tied")
        botTied()
    elif user_gest == 'rock' and robot_gest == 'scissors':
        print("Bot Loser")
        botLoser()
    elif user_gest == 'scissors' and robot_gest == 'paper':
        print("Bot Loser")
        botLoser()
    elif user_gest == 'scissors' and robot_gest == 'rock':
        print("Bot Winner")
        botWinner()
    elif user_gest == 'scissors' and robot_gest == 'scissors':
        print("Tied")
        botTied()


def take_image():
    cam = cv2.VideoCapture(0)
    i = 0
    start = datetime.now()
    while True:
        s, im = cam.read()  # captures image
        #gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ends = datetime.now()
        duration = ends - start
        if duration.total_seconds() > 10:
            break
    cv2.imwrite('/home/pi/Desktop/test/ece578_project1/images/3.jpg', im)
    cam.release()
    cv2.destroyAllWindows()
    
    
def main_game():
    print("Playing game...")
    speak("OK. Let's play rock paper scissors.", "RPC.mp3")
    time.sleep(0.5)
    # Tell user how to give gesture
    print("Giving instruction")
    speak("When the light turns green..", "gesture_instruction.mp3")
    time.sleep(5)
    
    # Do countdown for the user
    print("Ready?...")
    speak("Ready?", "ready.mp3")

    print("Rock...")
    speak("Rock", "rock.mp3")
    arms.bangDrumRight()

    print("Paper...")
    speak("Paper", "paper.mp3")
    arms.bangDrumLeft()

    print("Scissors...")
    speak("Scissors", "scissors.mp3")
    arms.bangDrumRight()

    print("Go!")
    speak("Go!", "go.mp3")
    
    robot_gest = generate_randGesture()

    while True:
        
        take_image()
        user_gest = get_gesture()
        print("User gesture: " + user_gest)
        print("Robot gesture: " + robot_gest)

        if (user_gest == 'rock' or user_gest == 'paper' or user_gest == 'scissors'):
            if robot_gest == 'rock':
                speak("Rock", "rock.mp3")
            elif robot_gest == 'scissors':
                speak("Scissors", "scissors.mp3")
            elif robot_gest == 'paper':
                speak("Paper", "paper.mp3")
                
            game_rule(user_gest, robot_gest)
            break
        else:
            print("Bot Confused")
            speak("I am confused", "confused.mp3")
            speak("Please try again", "try_again.mp3")

# ================================================================ #
if __name__ == "__main__":  
    main_game()

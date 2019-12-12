#from BotInteraction import *
from GestureRecognition import *
import cv2
import random
def generate_randGesture():
    gesture = ['rock', 'paper', 'scissors']
    index = random.randint(0, 2)
    return gesture[index]

def game_rule(user_gest, robot_gest):
    if user_gest == 'paper' and robot_gest == 'paper':
        BotTied()
    elif user_gest == 'paper' and robot_gest == 'rock':
        BotLoser()
    elif user_gest == 'paper' and robot_gest == 'scissors':
        BotWinner()
    elif user_gest == 'rock' and robot_gest == 'paper':
        BotWinner()
    elif user_gest == 'rock' and robot_gest == 'rock':
        BotTied()
    elif user_gest == 'rock' and robot_gest == 'scissors':
        BotLoser()
    elif user_gest == 'scissors' and robot_gest == 'paper':
        BotLoser()
    elif user_gest == 'scissors' and robot_gest == 'rock':
        BotWinner()
    elif user_gest == 'scissors' and robot_gest == 'scissors':
        BotTied()

def take_image():
    cam = cv2.VideoCapture(0)
    s, im = cam.read()  # captures image
    cv2.imwrite('/home/zhe/Desktop/ece578_project1/images/3.jpg', im)
def main_game():
    print("Playing game...")

    # Do countdown for the user
    print("Ready?...")
    Speak("Ready?")
    BangDrumBoth()

    print("Rock...")
    Speak("Rock")
    BangDrumBoth()

    print("Paper...")
    Speak("Paper")
    BangDrumBoth()

    print("Scissors...")
    Speak("Scissors")
    BangDrumBoth()

    print("Go!")
    Speak("Go!")
    BangDrumBoth()
    robot_gest = generate_randGesture()
    if (generate_randGesture() == 'rock'):
        rock()
    elif (generate_randGesture() ==  'paper'):
        paper()
    elif (generate_randGesture() == 'scissors'):
        scissors()
    print(robot_gest)
    take_image()
    user_gest = get_gesture()
    print(user_gest)

    if (user_gest == 'rock' or user_gest == 'paper' or user_gest == 'scissors'):
        game_rule(user_gest, robot_gest)
    else:
        BotConfused()
        main_game()

    # Reset the robot servos
    ArmReset()
    FaceReset()
    time.sleep(2)

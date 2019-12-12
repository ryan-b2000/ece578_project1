#! /usr/bin/env python3

''' #################################################################################################

    DimBot Movement Class

    This class provides the methods for moving various parts of the DimBot.


''' 

import Adafruit_PCA9685
import time

from ServoClass import ServoClass
import threading

# ====================== VARIABLES ======================= #

# Tracks the current position of each servo
servoPositions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Tracks the movement status of each thread (if the thread is doing movement or not)
servoMovement = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# Lock required to synchronize movement flag to start/stop motion
lock = threading.Condition()

# ======================= DEFINES ======================= #
MOVE_FRAME = 0.01
CHECK_TIME = 0.01

EYEBROW_R = 0
EYEBROW_L = 1
EYELID_L = 2
EYELID_R = 3
EYE_VERTICAL = 4
EYE_HORIZONTAL = 5
MOUTH = 6
ARM_UPDOWN_R = 12
ARM_ROTATE_R = 13
ELBOW_R = 14
ARM_UPDOWN_L = 8
ARM_ROTATE_L = 9
ELBOW_L = 10


class ServoManager:
    def __init__(self):
        self.__moveFrame = MOVE_FRAME
        self.__doMovement = False
        self.__initServos();
        print("ServoManager initialized")


    # ======================= FUNCTIONS ======================= #
    def setServoPosition(self, servo, pos):
        print("Set servo: " + str(servo) + "\tDegree: " + str(pos))
        servoPositions[int(servo)] = int(pos)


    # Set the time between interpolated movements (the sleep time)
    def setMovementFrame(self, length):
        print("Set frame length " + str(length))
        self.__moveFrame = length


    def __servoThread(self, servoID):    
        # Initialize the servo
        servo = ServoClass(servoID)             # Create object
        name = servo.getName()
        #servo.move(0)                           # Set to position 0
        servoPositions[servoID] = servo.getPosition()   # set the default old position
        oldPosition = servoPositions[servoID]
        newPosition = servoPositions[servoID]
        

        print("Start Servo thread: " + str(name) + " Position: " + str(oldPosition))

        while (1):          
            # Wait for the signal to start doing movement
            count = 0
            while (True):
                # Check if we need to do movement
                lock.acquire()
                if self.__doMovement == True:
                    #print("Do Movement notice received...")
                    break
                lock.release()
                time.sleep(CHECK_TIME)

            lock.release()
            newPosition = servoPositions[servoID]   # Get the new position    
            
            # if the new position is less than the old position
            while newPosition < oldPosition:          # Decrement until we get to the new position
                servoMovement[servoID] = True
                print(name + str(": ") + str(oldPosition) + " - " + str(newPosition))
                servo.move(oldPosition)                 
                oldPosition = oldPosition - 1
                time.sleep(self.__moveFrame)

            # if the new position is less than the old position
            while newPosition > oldPosition:          # Increment until we get to the new position
                servoMovement[servoID] = True
                print(name + str(": ") + str(oldPosition) + " - " + str(newPosition))
                servo.move(oldPosition)                 
                oldPosition = oldPosition + 1
                time.sleep(self.__moveFrame)

            # Get the positon value from the servo because it has limit checking and
            # we want to stay in bounds
            newPosition = servo.getPosition()               # update the servo position (in degrees)
            oldPosition = servo.getPosition()
            servoPositions[servoID] = servo.getPosition()
            servoMovement[servoID] = False                  # set flag that thread is done with movement



    def __initServos(self):
        print("Initialize servos")
        eyebrowR = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYEBROW_R))
        eyebrowL = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYEBROW_L))
        eyelidR = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYELID_R))
        eyelidL = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYELID_L))
        eyehorz = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYE_HORIZONTAL))
        eyevert = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=EYE_VERTICAL))
        mouth = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=MOUTH))
        arm_updownR = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ARM_UPDOWN_R))
        arm_updownL = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ARM_UPDOWN_L))
        arm_rotateR = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ARM_ROTATE_R))
        arm_rotateL = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ARM_ROTATE_L))
        elbowR = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ELBOW_R))
        elbowL = threading.Thread(target=self.__servoThread, kwargs=dict(servoID=ELBOW_L))
        eyebrowR.start()
        eyebrowL.start()
        eyelidR.start()
        eyelidL.start()
        eyehorz.start()
        eyevert.start()
        mouth.start()
        arm_updownR.start()
        arm_updownL.start()
        arm_rotateR.start()
        arm_rotateL.start()
        elbowL.start()
        elbowR.start()

    def beginMotion(self):
        lock.acquire()
        self.__doMovement = True        # set flag to begin motion
        lock.release()
        print("Begin Movement...")
        time.sleep(0.5)                 # wait a little bit
        lock.acquire()
        self.__doMovement = False       # set flag to end movement when threads finish
        lock.release()
        
        # Make sure call blocks until all threads are finished
        movementFinished = False                # set to False to get into while loop
        while movementFinished == False:    
            movementFinished = True             # set to True and if one isn't finished
            for i in servoPositions:            # it will set it to false and we keep trying
                if i == True:                   # if any thread is still moving, then reset the
                    movementFinished = False    # flag and keep checking
            time.sleep(0.1)
        print("End Movement...")


    def __movementTest(self, servoID, pos):
        self.setMovementFrame(0)
        self.setServoPosition(servoID, pos)
        self.beginMotion()


    def servoTestAll(self):
        print("ServoManager Test")
        self.__movementTest(EYEBROW_L, 100)
        self.__movementTest(EYEBROW_L, 50)
        self.__movementTest(EYEBROW_L, 80)
        
        self.__movementTest(EYEBROW_R, 100)
        self.__movementTest(EYEBROW_R, 50)
        self.__movementTest(EYEBROW_R, 80)
        
        #self.__movementTest(EYELID_L, 60)
        #self.__movementTest(EYELID_L, 80)
        #self.__movementTest(EYELID_L, 60)
        
        #self.__movementTest(EYELID_R, 30)
        #self.__movementTest(EYELID_R, 65)
        #self.__movementTest(EYELID_R, 30)

        self.__movementTest(EYE_VERTICAL, 60)
        self.__movementTest(EYE_VERTICAL, 70)
        self.__movementTest(EYE_VERTICAL, 80)
        self.__movementTest(EYE_VERTICAL, 70)

        self.__movementTest(EYE_HORIZONTAL, 60)
        self.__movementTest(EYE_HORIZONTAL, 80)
        self.__movementTest(EYE_HORIZONTAL, 100)
        self.__movementTest(EYE_HORIZONTAL, 80)

        self.__movementTest(MOUTH, 50)
        self.__movementTest(MOUTH, 20)
        self.__movementTest(MOUTH, 50)
        self.__movementTest(MOUTH, 20)

        self.__movementTest(ELBOW_L, 100)
        self.__movementTest(ELBOW_L, 80)
        self.__movementTest(ELBOW_L, 100)

        self.__movementTest(ARM_ROTATE_L, 70)
        self.__movementTest(ARM_ROTATE_L, 60)
        self.__movementTest(ARM_ROTATE_L, 50)

        self.__movementTest(ARM_UPDOWN_L, 80)
        self.__movementTest(ARM_UPDOWN_L, 50)
        self.__movementTest(ARM_UPDOWN_L, 0)

        self.__movementTest(ELBOW_R, 30)
        self.__movementTest(ELBOW_R, 90)
        self.__movementTest(ELBOW_R, 30)

        self.__movementTest(ARM_ROTATE_R, 55)
        self.__movementTest(ARM_ROTATE_R, 80)
        self.__movementTest(ARM_ROTATE_R, 65)

        self.__movementTest(ARM_UPDOWN_R, 30)
        self.__movementTest(ARM_UPDOWN_R, 70)
        self.__movementTest(ARM_UPDOWN_R, 0)


    def customTest(self):
        while(1):
            chan = input("Channel? ")
            deg = input("degree? ")
            self.setMovementFrame(0)
            self.setServoPosition(chan, deg)
            self.beginMotion()


    # Set the time between interpolated movements (the sleep time)
    def setMovementFrame(self, length):
        print("Set frame length " + str(length))
        self.__moveFrame = length


# Create class singleton for import
servos = ServoManager()


# ================================================================ #
if __name__ == "__main__":  
    #servos.customTest()
    servos.servoTestAll()
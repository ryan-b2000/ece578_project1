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
oldPositions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
ARM_UPDOWN_L = 7
ARM_ROTATE_L = 8
ELBOW_L = 9
ARM_UPDOWN_R = 10
ARM_ROTATE_R = 11
ELBOW_R = 12




class ServoManager:
    def __init__(self):
        self.__moveFrame = MOVE_FRAME
        self.__doMovement = False
        self.__startManager()
        print("ServoManager initialized")


    # ======================= FUNCTIONS ======================= #
    def setServoPosition(self, servo, pos):
        print("Set servo: " + str(servo) + "\tDegree: " + str(pos))
        servoPositions[int(servo)] = int(pos)


    # Set the time between interpolated movements (the sleep time)
    def setMovementFrame(self, length):
        print("Set frame length " + str(length))
        self.__moveFrame = length

    def __manager(self):
        print("ServoManager: Starting servo thread")
        servos = []
        servos.append(ServoClass(EYEBROW_R))             # Create object
        servos.append(ServoClass(EYEBROW_L))             # Create object
        servos.append(ServoClass(EYELID_L))          # Create object
        servos.append(ServoClass(EYELID_R))             # Create object
        servos.append(ServoClass(EYE_VERTICAL))      # Create object
        servos.append(ServoClass(EYE_HORIZONTAL))    # Create object
        servos.append(ServoClass(MOUTH))             # Create object        
        servos.append(ServoClass(ARM_UPDOWN_L))             # Create object
        servos.append(ServoClass(ARM_ROTATE_L))             # Create object
        servos.append(ServoClass(ELBOW_L))             # Create object
        servos.append(ServoClass(ARM_UPDOWN_R))             # Create object
        servos.append(ServoClass(ARM_ROTATE_R))             # Create object
        servos.append(ServoClass(ELBOW_R))             # Create object
        time.sleep(2)

        print("Start Servo thread: ")

        while (1):          
            # Wait for the signal to start doing movement
            count = 0
            while (True):
                # Check if we need to do movement
                if self.__doMovement == True:
                    #print("Do Movement notice received...")
                    break
                time.sleep(CHECK_TIME)

            # Check for tservos that need movement
            for pos in range(0, len(servos)):
                #print("Checking Servo: ", pos)
                currPos = servoPositions[pos]
                oldPos = oldPositions[pos]
                # if this servo has a new position, do the movement
                if currPos != oldPos:
                    newPos = servoPositions[pos]   # Get the new position    
                    
                    # if the new position is less than the old position
                    while newPos < oldPos:          # Decrement until we get to the new position
                        servoMovement[pos] = True
                        #print(str(oldPos) + " - " + str(newPos))
                        servos[pos].move(oldPos)                 
                        oldPos = oldPos - 1
                        time.sleep(self.__moveFrame)
         

                    # if the new position is less than the old position
                    while newPos > oldPos:          # Increment until we get to the new position
                        servoMovement[pos] = True
                        #print(str(oldPos) + " - " + str(newPos))
                        servos[pos].move(oldPos)                 
                        oldPos = oldPos + 1
                        time.sleep(self.__moveFrame)

                    # Get the positon value from the servo because it has limit checking and
                    # we want to stay in bounds
                    oldPositions[pos] = servos[pos].getPosition()     # update the old position
                    servoPositions[pos] = servos[pos].getPosition()   # update the current position
                    servoMovement[pos] = False                  # set flag that thread is done with movement
            time.sleep(0.25)

    def __startManager(self):
        manager = threading.Thread(target=self.__manager)
        manager.start()

    def beginMotion(self):
        self.__doMovement = True        # set flag to begin motion
        print("Begin Movement...")
        time.sleep(0.5)                 # wait a little bit
        self.__doMovement = False       # set flag to end movement when threads finish
        
        # Make sure call blocks until all threads are finished
        movementFinished = False                # set to False to get into while loop
        while movementFinished == False:    
            movementFinished = True             # set to True and if one isn't finished
            for i in servoPositions:            # it will set it to false and we keep trying
                if i == True:                   # if any thread is still moving, then reset the
                    movementFinished = False    # flag and keep checking
            time.sleep(0.1)
        print("End Movement...")


    def __movementTest(self, chan, deg):
        self.setMovementFrame(0)
        self.setServoPosition(chan, deg)
        self.beginMotion()


    def servoTestAll(self):
        print("ServoManager Test")
        self.setMovementFrame(0)

        #self.__movementTest(EYEBROW_L, 100)
        self.setServoPosition(EYEBROW_L, 100)
        self.beginMotion()

        #self.__movementTest(EYEBROW_L, 50)
        self.setServoPosition(EYEBROW_L, 50)
        self.beginMotion()

        #self.__movementTest(EYEBROW_L, 80)
        self.setServoPosition(EYEBROW_L, 80)
        self.beginMotion()

        #self.__movementTest(EYEBROW_R, 100)
        self.setServoPosition(EYEBROW_R, 100)
        self.beginMotion()

        #self.__movementTest(EYEBROW_R, 50)
        self.setServoPosition(EYEBROW_R, 50)
        self.beginMotion()

        #self.__movementTest(EYEBROW_R, 80)
        self.setServoPosition(EYEBROW_R, 80)
        self.beginMotion()
        
        #self.__movementTest(EYELID_L, 60)
        #self.__movementTest(EYELID_L, 80)
        #self.__movementTest(EYELID_L, 60)
        
        #self.__movementTest(EYELID_R, 30)
        #self.__movementTest(EYELID_R, 65)
        #self.__movementTest(EYELID_R, 30)

        #self.__movementTest(EYE_VERTICAL, 60)
        self.setServoPosition(EYE_VERTICAL, 60)
        self.beginMotion()

        #self.__movementTest(EYE_VERTICAL, 70)
        self.setServoPosition(EYE_VERTICAL, 70)
        self.beginMotion()

        #self.__movementTest(EYE_VERTICAL, 80)
        self.setServoPosition(EYE_VERTICAL, 80)
        self.beginMotion()

        #self.__movementTest(EYE_VERTICAL, 70)
        self.setServoPosition(EYE_VERTICAL, 70)
        self.beginMotion()

        #self.__movementTest(EYE_HORIZONTAL, 60)
        self.setServoPosition(EYE_HORIZONTAL, 60)
        self.beginMotion()

        #self.__movementTest(EYE_HORIZONTAL, 80)
        self.setServoPosition(EYE_HORIZONTAL, 80)
        self.beginMotion()

        #self.__movementTest(EYE_HORIZONTAL, 100)
        self.setServoPosition(EYE_HORIZONTAL, 100)
        self.beginMotion()

        #self.__movementTest(EYE_HORIZONTAL, 80)
        self.setServoPosition(EYE_HORIZONTAL, 80)
        self.beginMotion()

        #self.__movementTest(MOUTH, 50)
        self.setServoPosition(MOUTH, 50)
        self.beginMotion()

        #self.__movementTest(MOUTH, 20)
        self.setServoPosition(MOUTH, 20)
        self.beginMotion()

        #self.__movementTest(MOUTH, 50)
        self.setServoPosition(MOUTH, 50)
        self.beginMotion()

        #self.__movementTest(MOUTH, 20)
        self.setServoPosition(MOUTH, 20)
        self.beginMotion()

        #self.__movementTest(ELBOW_L, 100)
        self.setServoPosition(ELBOW_L, 100)
        self.beginMotion()

        #self.__movementTest(ELBOW_L, 80)
        self.setServoPosition(ELBOW_L, 80)
        self.beginMotion()

        #self.__movementTest(ELBOW_L, 100)
        self.setServoPosition(ELBOW_L, 100)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_L, 70)
        self.setServoPosition(ARM_ROTATE_L, 70)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_L, 60)
        self.setServoPosition(ARM_ROTATE_L, 60)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_L, 50)
        self.setServoPosition(ARM_ROTATE_L, 50)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_L, 80)
        self.setServoPosition(ARM_UPDOWN_L, 80)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_L, 50)
        self.setServoPosition(ARM_UPDOWN_L, 50)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_L, 0)
        self.setServoPosition(ARM_UPDOWN_L, 0)
        self.beginMotion()

        #self.__movementTest(ELBOW_R, 30)
        self.setServoPosition(ELBOW_R, 30)
        self.beginMotion()

        #self.__movementTest(ELBOW_R, 90)
        self.setServoPosition(ELBOW_R, 90)
        self.beginMotion()

        #self.__movementTest(ELBOW_R, 30)
        self.setServoPosition(ELBOW_R, 30)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_R, 55)
        self.setServoPosition(ARM_ROTATE_R, 55)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_R, 80)
        self.setServoPosition(ARM_ROTATE_R, 80)
        self.beginMotion()

        #self.__movementTest(ARM_ROTATE_R, 65)
        self.setServoPosition(ARM_ROTATE_R, 65)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_R, 30)
        self.setServoPosition(ARM_UPDOWN_R, 30)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_R, 70)
        self.setServoPosition(ARM_UPDOWN_R, 70)
        self.beginMotion()

        #self.__movementTest(ARM_UPDOWN_R, 0)
        self.setServoPosition(ARM_UPDOWN_R, 0)
        self.beginMotion()

    def customTest(self):
        while(1):
            chan = input("Channel? ")
            deg = input("degree? ")
            self.__movementTest(chan, deg)
            #self.setMovementFrame(0)
            #self.setServoPosition(chan, deg)
            #self.beginMotion()


    # Set the time between interpolated movements (the sleep time)
    def setMovementFrame(self, length):
        print("Set frame length " + str(length))
        self.__moveFrame = length



# Create class singleton for import
servos = ServoManager()


# ================================================================ #
if __name__ == "__main__":  
    servos.customTest()
    #servos.servoTestAll()
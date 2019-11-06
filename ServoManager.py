#! /usr/bin/env python3

''' #################################################################################################

    DimBot Movement Class

    This class provides the methods for moving various parts of the DimBot.


''' 

import Adafruit_PCA9685
import time

# ======================= DEFINES ======================= #
 


#pwm channel number on PWM Driver
EYEBROW_R       = 0           
EYEBROW_L       = 1           
EYELID_R        = 2           
EYELID_L        = 3            
EYE_HORIZONTAL  = 4      
EYE_VERTICAL    = 5        
MOUTH           = 6               
ARM_ROTATE_R    = 7       
ARM_SIDEWAYS_R  = 8       
ARM_ROTATE_L    = 9        
ARM_SIDEWAYS_L  = 10     
ELBOW_R         = 11     
ELBOW_L         = 12   


RIGHT = 'Right'
LEFT = 'Left'

# ======================= SET UP PCA9685 I2C DRIVER ======================= #

pca = Adafruit_PCA9685.PCA9685()    # Sets up the global member for the driver object
pca.set_pwm_freq(40)                # set the frequency of the system as 50Hz
print("PCA9685 initialized")


def Move (channel, degree):
    #print("PCA9685: Channel: " + str(channel) + " Degree: " + str(degree))
    val = __ConvertDegrees(degree)
    #print("Degree: " + str(degree) + " = " + str(val))
    pca.set_pwm(int(channel), 0, int(val))


# ==== Eyebrow Movement ==== #
# Channel: 0
# Channel: 1
def EyebrowUp(side):
    if (side == RIGHT):
        print("Right Eyebrow Up")
        Move(EYEBROW_R, 100)
    else:
        print("Left Eyebrow Up")
        Move(EYEBROW_L, 100)

def EyebrowFlat(side):
    if (side == RIGHT):
        print("Right Eyebrow Center")
        Move(EYEBROW_R, 80)
    else:
        print("Left Eyebrow Center")
        Move(EYEBROW_L, 80)

def EyebrowDown(side):
    if (side == RIGHT):
        print("Right Eyebrow Center")
        Move(EYEBROW_R, 50)
    else:
        print("Left Eyebrow Center")
        Move(EYEBROW_L, 50)


# ==== Eyelid Movement ==== #
# Channel: 2
# Channel: 3
def EyeOpen(side):
    if (side == RIGHT):
        print("Eyelid Right Open")
        Move(EYELID_R, 90)
    else:
        print("Eyelid Left Open")
        Move(EYELID_L, 120)

def EyeClose(side):
    if (side == RIGHT):
        print("Eyelid Right Close")
        Move(EYELID_R, 150)
    else:
        print("Eyelid Left Close")
        Move(EYELID_L, 60)


# ==== Eye Horizontal Movement ==== #
# Channel: 4
def EyeLeft():
    print("Eye Horizontal Left")
    Move(EYE_HORIZONTAL, 70)

def EyeCenter():
    print("Eye Horizontal Center")
    Move(EYE_HORIZONTAL, 85)

def EyeRight():
    print("Eye Horizontal Right")
    Move(EYE_HORIZONTAL, 100)


# ==== Eye Vertical Movement ==== #
# Channel: 5
def EyeUp():
    print("Eye Vertical Up")
    Move(EYE_VERTICAL, 80)

def EyeMiddle():
    print("Eye Vertical Middle")
    Move(EYE_VERTICAL, 70)

def EyeDown():
    print("Eye Vertical Down")
    Move(EYE_VERTICAL, 50)


# ======== Mouth Movement ======== #
# Channel: 6
def MouthOpen():
    print("Mouth Open")
    Move(MOUTH, 50)

def MouthClose():
    print("Mouth Close")
    Move(MOUTH, 30)


# ======== Shoulder Movement ======== #
# Channel: 7
# Channel: 9
def ShoulderUp(side):
    if (side == RIGHT):
        print("Right Shoulder Up")
        Move(ARM_ROTATE_R, 100)
    else:
        print("Left Shoulder Up")
        Move(ARM_ROTATE_L, 100)

def ShoulderDown(side):
    if (side == RIGHT):
        print("Right Shoulder Down")
        Move(ARM_ROTATE_R, 0)
    else:
        print("Left Shoulder Down")
        Move(ARM_ROTATE_L, 0)


# ======== Arm Movement ======== #
# Channel: 8 Right
# Channel: 10 Left
def ArmOut(side):
    if (side == RIGHT):
        print("Right Arm Out")
        Move(ARM_SIDEWAYS_R, 80)
    else:
        print("Left Arm Out")
        Move(ARM_SIDEWAYS_L, 100)

def ArmIn(side):
    if (side == RIGHT):
        print("Right Arm In")
        Move(ARM_SIDEWAYS_R, 100)
    else:
        print("Left Arm In")
        Move(ARM_SIDEWAYS_L, 0)


# ======== Elbow Movement ======== #
# Channel: 11 Right
# Channel: 12 Left
def ElbowUp(side):
    if (side == RIGHT):
        print("Right Elbow Up")
        Move(ELBOW_R, 100)
    else:
        print("Left Elbow Up")
        Move(ELBOW_L, 40)


def ElbowDown(side):
    if (side == RIGHT):
        print("Right Elbow Down")
        Move(ELBOW_R, 60)
    else:
        print("Left Elbow Down")
        Move(ELBOW_L, 90)


def __ConvertDegrees(degree):
    
    deg = int(degree)
    if (deg > 0):
        deg = 2.75 * float(degree) + 40
    else:
        deg = 0

    # safety check
    if (deg > 550):
        deg = 550

    return round(deg, 0)



# Sleep function abstraction
def Sleep():
    time.sleep(1)

def CustomMoveTest():
    while(1):
        chan = input("Channel? ")
        degree = input("Degree? ")
        Move(chan, degree)

# Test all servos 
def TestAllServos():
    EyebrowUp(RIGHT)
    Sleep()
    EyebrowDown(RIGHT)
    Sleep()
    EyebrowFlat(RIGHT)
    Sleep()

    EyebrowUp(LEFT)
    Sleep()
    EyebrowDown(LEFT)
    Sleep()
    EyebrowFlat(LEFT)
    Sleep()

    #EyeClose(RIGHT)
    #Sleep()
    #EyeOpen(RIGHT)
    #Sleep()

    EyeLeft()
    Sleep()
    EyeCenter()
    Sleep()
    EyeRight()
    Sleep()
    EyeCenter()
    Sleep()
    

    MouthOpen()
    Sleep()
    MouthClose()
    Sleep()

    #ShoulderUp(RIGHT)
    #Sleep()
    #ShoulderDown(RIGHT)
    #Sleep()
    #ShoulderUp(LEFT)
    #Sleep()
    #ShoulderDown(LEFT)
    #Sleep()

    #ArmOut(RIGHT)
    #Sleep()
    #ArmIn(RIGHT)
    #Sleep()
    #ArmOut(LEFT)
    #Sleep()
    #ArmIn(LEFT)
    #Sleep()

    ElbowUp(RIGHT) # not received
    #Sleep()
    ElbowDown(RIGHT)
    Sleep()
    ElbowUp(RIGHT)
    Sleep()
    ElbowDown(RIGHT)
    Sleep()
    ElbowUp(RIGHT)
    Sleep()

    ElbowUp(LEFT)
    Sleep()
    ElbowDown(LEFT)
    Sleep()
    ElbowUp(LEFT)



def CustomTest():
    while (1):
        chan = input("Channel? ")
        val = input("Degree? ")
        Move(chan, val)
        time.sleep(1)

# ================================================================ #
if __name__ == "__main__":  
    print("Running servo tests...")
    #CustomTest()
    TestAllServos()


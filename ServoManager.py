#! /usr/bin/env python3

'''	#################################################################################################

	DimBot Movement Class

	This class provides the methods for moving various parts of the DimBot.


''' 

import Adafruit_PCA9685
import time

# ======================= DEFINES ======================= #
 


#pwm channel number on PWM Driver
EYEBROW_R 		= 0           
EYEBROW_L 		= 1           
EYELID_R 		= 2           
EYELID_L 		= 3            
EYE_HORIZONTAL 	= 4      
EYE_VERTICAL 	= 5        
MOUTH 			= 6               
ARM_ROTATE_R 	= 7       
ARM_SIDEWAYS_R 	= 8       
ARM_ROTATE_L 	= 9        
ARM_SIDEWAYS_L 	= 10     
ELBOW_R 		= 11     
ELBOW_L 		= 12   


RIGHT = 'Right'
LEFT = 'Left'

# ======================= SET UP PCA9685 I2C DRIVER ======================= #
# Sets up the global member for the driver object
pca = Adafruit_PCA9685.PCA9685()

# set the frequency of the system as 50Hz
pca.set_pwm_freq(40)
print("PCA9685 initialized")


def InitServos():
	print("Servo manager initialized")

def Move (channel, degree):
	print("PCA9685: Channel: " + str(channel) + " Degree: " + str(degree))
	val = __ConvertDegrees(degree)
	print("Degree: " + str(degree) + " = " + str(val))
	pca.set_pwm(int(channel), 0, int(val))

def CustomMove(channel, degree):
	print("Channel: " + str(channel) + " Degree: " + str(degree))
	val = __ConvertDegrees(degree)
	print("Degree: " + str(degree) + " = " + str(val))
	pca.set_pwm(int(channel), 0, int(val))


# ==== Total Face Reset ==== #
def FaceReset():
	EyebrowFlat(RIGHT)
	EyebrowFlat(LEFT)
	EyeOpen(RIGHT)
	EyeOpen(LEFT)
	EyeCenter()
	EyeMiddle()
	MouthClose()
	

# ==== Eyebrow Movement ==== #
def EyebrowUp(side):
	if (side == RIGHT):
		print("Right Eyebrow Up")
		Move(EYEBROW_R, 150)
	else:
		print("Left Eyebrow Up")
		Move(EYEBROW_L, 150)

def EyebrowFlat(side):
	if (side == RIGHT):
		print("Right Eyebrow Center")
		Move(EYEBROW_R, 85)
	else:
		print("Left Eyebrow Center")
		Move(EYEBROW_L, 85)

def EyebrowDown(side):
	if (side == RIGHT):
		print("Right Eyebrow Center")
		Move(EYEBROW_R, 70)
	else:
		print("Left Eyebrow Center")
		Move(EYEBROW_L, 70)


# ==== Eyelid Movement ==== #
def EyeOpen(side):
	if (side == RIGHT):
		print("Eyelid Right Open")
		Move(EYELID_R, 90)
	else:
		print("Eyelid Left Open")
		Move(EYEBROW_L, 120)

def EyeClose(side):
	if (side == RIGHT):
		print("Eyelid Right Close")
		Move(EYELID_R, 150)
	else:
		print("Eyelid Left Close")
		Move(EYELID_L, 60)


# ==== Eye Horizontal Movement ==== #
def EyeLeft():
	print("Eye Horizontal Left")
	Move(EYE_HORIZONTAL, 80)

def EyeCenter(self,channel,degree):
	print("Eye Horizontal Center")
	Move(EYE_HORIZONTAL, 120)

def EyeRight():
	print("Eye Horizontal Right")
	Move(EYE_HORIZONTAL, 150)


# ==== Eye Vertical Movement ==== #
def EyeUp():
	print("Eye Vertical Up")
	Move(EYE_VERTICAL, 120)

def EyeMiddle():
	print("Eye Vertical Middle")
	Move(EYE_VERTICAL, 100)

def EyeDown():
	print("Eye Vertical Down")
	Move(EYE_VERTICAL, 80)


# ======== Mouth Movement ======== #
def MouthOpen():
	print("Mouth Open")
	Move(MOUTH, 60)

def MouthClose():
	print("Mouth Close")
	Move(MOUTH, 10)


# ======== Shoulder Movement ======== #
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
def ArmOut(side):
	if (side == RIGHT):
		print("Right Arm Out")
		Move(ARM_SIDEWAYS_R, 100)
	else:
		print("Left Arm Out")
		Move(ARM_SIDEWAYS_L, 100)

def ArmIn(side):
	if (side == RIGHT):
		print("Right Arm In")
		Move(ARM_SIDEWAYS_R, 0)
	else:
		print("Left Arm In")
		Move(ARM_SIDEWAYS_L, 0)


# ======== Elbow Movement ======== #
def ElbowUp(side):
	if (side == RIGHT):
		print("Right Elbow Up")
		Move(ELBOW_R, 150)
	else:
		print("Left Elbow Up")
		Move(ELBOW_L, 130)

def ElbowDown(side):
	if (side == RIGHT):
		print("Right Elbow Down")
		Move(ELBOW_R, 170)
	else:
		print("Left Elbow Down")
		Move(ELBOW_L, 180)


def __ConvertDegrees(degree):
	
	deg = int(degree)
	if (deg > 0):
		deg = 2.75 * float(degree) + 40
	else:
		deg = 0

	return round(deg, 0)



# Sleep function abstraction
def Sleep():
	time.sleep(3)

def CustomMoveTest():
	InitServos()
	while(1):
		chan = input("Channel? ")
		degree = input("Degree? ")
		CustomMove(chan, degree)

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

	EyeClose(RIGHT)
	Sleep()
	EyeOpen(RIGHT)
	Sleep()

	EyeClose(LEFT)
	Sleep()
	EyeOpen(LEFT)
	Sleep()

	MouthOpen()
	Sleep()
	MouthClose()
	Sleep()

	ShoulderUp(RIGHT)
	Sleep()
	ShoulderDown(RIGHT)
	Sleep()
	ShoulderUp(LEFT)
	Sleep()
	ShoulderDown(LEFT)
	Sleep()

	ArmOut(RIGHT)
	Sleep()
	ArmIn(RIGHT)
	Sleep()
	ArmOut(LEFT)
	Sleep()
	ArmIn(LEFT)
	Sleep()

	ElbowDown(RIGHT)
	Sleep()
	ElbowUp(RIGHT)
	Sleep()
	ElbowDown(LEFT)
	Sleep()
	ElbowUp(LEFT)
	Sleep()


def CustomTest():
	while (1):
		chan = input("Channel? ")
		val = input("Degree? ")
		CustomMove(chan, val)
		time.sleep(1)

# ================================================================ #
if __name__ == "__main__":  
	print("Running servo tests...")
	CustomTest()
	TestAllServos()


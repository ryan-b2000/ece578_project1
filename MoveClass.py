#! /usr/bin/env python3

'''	#################################################################################################

	DimBot Movement Class

	This class provides the methods for moving various parts of the DimBot.


''' 

#import Adafruit_PCA9685
import time

# ======================= GLOBAL DEFINES ======================= #
 
DEGREE_0 = 102
DEGREE_30 = 171
DEGREE_40 = 194
DEGREE_45 = 206
DEGREE_50 = 220
DEGREE_60 = 240
DEGREE_70 = 263
DEGREE_80 = 286
DEGREE_85 = 297
DEGREE_90 = 310
DEGREE_100 = 333
DEGREE_110 = 356
DEGREE_120 = 379
DEGREE_130 = 400
DEGREE_135 = 414
DEGREE_140 = 430
DEGREE_150 = 448
DEGREE_160 = 471
DEGREE_170 = 480    
DEGREE_175 = 490    
DEGREE_180 = 505
DEGREE_190 = 528
DEGREE_200 = 551


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
#PCA9685 = Adafruit_PCA9685.PCA9685()

# set the frequency of the system as 50Hz
#PCA9685.set_pwm_freq(50)

class MoveClass:

	def __init__(self):
		print("Move class initialized")

	def __Move (self, channel, degree):
		print("PCA9685: Channel: " + str(channel) + " Degree: " + str(degree))
		val = self.__ConvertDegrees(degree)
		print("Degree: " + str(degree) + " = " + str(val))
		PCA9685.set_pwm(channel, 0, val)

	def CustomMove(self, channel, degree):
		print("Channel: " + str(channel) + " Degree: " + str(degree))
		val = self.__ConvertDegrees(degree)
		print("Degree: " + str(degree) + " = " + str(val))
		PCA9685.set_pwm(int(channel), 0, int(val))


	# ==== Total Face Reset ==== #
	def FaceReset(self):
		EyebrowFlat(RIGHT)
		EyebrowFlat(LEFT)
		EyeOpen(RIGHT)
		EyeOpen(LEFT)
		EyeCenter()
		EyeMiddle()
		MouthClose()
		

	# ==== Eyebrow Movement ==== #
	def EyebrowUp(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Up")
			self.__Move(EYEBROW_R, 80)
		else:
			print("Left Eyebrow Up")
			self.__Move(EYEBROW_L, 80)

	def EyebrowFlat(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Center")
			self.__Move(EYEBROW_R, 120)
		else:
			print("Left Eyebrow Center")
			self.__Move(EYEBROW_L, 120)

	def EyebrowDown(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Center")
			self.__Move(EYEBROW_R, 140)
		else:
			print("Left Eyebrow Center")
			self.__Move(EYEBROW_L, 140)


	# ==== Eyelid Movement ==== #
	def EyeOpen(self, side):
		if (side == RIGHT):
			print("Eyelid Right Open")
			self.__Move(EYELID_R, 90)
		else:
			print("Eyelid Left Open")
			self.__Move(EYEBROW_L, 120)

	def EyeClose(self, side):
		if (side == RIGHT):
			print("Eyelid Right Close")
			self.__Move(EYELID_R, 150)
		else:
			print("Eyelid Left Close")
			self.__Move(EYELID_L, 60)


	# ==== Eye Horizontal Movement ==== #
	def EyeLeft(self):
		print("Eye Horizontal Left")
		self.__Move(EYE_HORIZONTAL, 80)

	def EyeCenter(self,channel,degree):
		print("Eye Horizontal Center")
		self.__Move(EYE_HORIZONTAL, 110)
	
	def EyeRight(self):
		print("Eye Horizontal Right")
		self.__Move(EYE_HORIZONTAL, 160)


	# ==== Eye Vertical Movement ==== #
	def EyeUp(self):
		print("Eye Vertical Up")
		self.__Move(EYE_VERTICAL, 80)

	def EyeMiddle(self):
		print("Eye Vertical Middle")
		self.__Move(EYE_VERTICAL, 100)

	def EyeDown(self):
		print("Eye Vertical Down")
		self.__Move(EYE_VERTICAL, 120)


	# ======== Mouth Movement ======== #
	def MouthOpen(self):
		print("Mouth Open")
		self.__Move(MOUTH, 60)

	def MouthClose(self):
		print("Mouth Close")
		self.__Move(MOUTH, 0)


	# ======== Shoulder Movement ======== #
	def ShoulderUp(self, side):
		if (side == RIGHT):
			print("Right Shoulder Up")
			self.__Move(ARM_ROTATE_R, 100)
		else:
			print("Left Shoulder Up")
			self.__Move(ARM_ROTATE_L, 100)

	def ShoulderDown(self, side):
		if (side == RIGHT):
			print("Right Shoulder Down")
			self.__Move(ARM_ROTATE_R, 0)
		else:
			print("Left Shoulder Down")
			self.__Move(ARM_ROTATE_L, 0)


	# ======== Arm Movement ======== #
	def ArmOut(self, side):
		if (side == RIGHT):
			print("Right Arm Out")
			self.__Move(ARM_SIDEWAYS_R, 100)
		else:
			print("Left Arm Out")
			self.__Move(ARM_SIDEWAYS_L, 100)

	def ArmIn(self, side):
		if (side == RIGHT):
			print("Right Arm In")
			self.__Move(ARM_SIDEWAYS_R, 0)
		else:
			print("Left Arm In")
			self.__Move(ARM_SIDEWAYS_L, 0)


	# ======== Elbow Movement ======== #
	def ElbowUp(self, side):
		if (side == RIGHT):
			print("Right Elbow Up")
			self.__Move(ELBOW_R, 150)
		else:
			print("Left Elbow Up")
			self.__Move(ELBOW_L, 150)

	def ElbowDown(self, side):
		if (side == RIGHT):
			print("Right Elbow Down")
			self.__Move(ELBOW_R, 170)
		else:
			print("Left Elbow Down")
			self.__Move(ELBOW_L, 170)


	def __ConvertDegrees(self, degree):
		converter = {
			0: 2,		
			30: 171,
			40:	194,
			45: 206,
			50: 220,
			60: 240,
			70: 263,
			80: 286,
			85: 297,
			90: 310,
			100: 333,
			110: 356,
			120: 379,
			130: 400,
			135: 414,
			140: 430,
			150: 448,
			160: 471,
			170: 480,
			175: 490,
			180: 505,
			190: 528,
			200: 551
		}
		return converter.get(degree, "Invalid")



# Sleep function abstraction
def Sleep():
	time.sleep(0.5)

def CustomTest():
	Move = MoveClass()
	while(1):
		chan = input("Channel? ")
		degree = input("Degree? ")
		Move.CustomMove(chan, degree)

# Test all servos 
def TestAllServos():
	Move = MoveClass()

	Move.FaceReset()

	Move.EyebrowUp(RIGHT)
	Sleep()
	Move.EyebrowDown(RIGHT)
	Sleep()
	Move.EyebrowFlat(RIGHT)
	Sleep()

	Move.EyebrowUp(LEFT)
	Sleep()
	Move.EyebrowDown(LEFT)
	Sleep()
	Move.EyebrowFlat(LEFT)
	Sleep()

	Move.EyeClose(RIGHT)
	Sleep()
	Move.EyeOpen(RIGHT)
	Sleep()

	Move.EyeClose(LEFT)
	Sleep()
	Move.EyeOpen(LEFT)
	Sleep()

	Move.MouthOpen()
	Sleep()
	Move.MouthClose()
	Sleep()

	Move.ShoulderUp(RIGHT)
	Sleep()
	Move.ShoulderDown(RIGHT)
	Sleep()
	Move.ShoulderUp(LEFT)
	Sleep()
	Move.ShoulderDown(LEFT)
	Sleep()

	Move.ArmOut(RIGHT)
	Sleep()
	Move.ArmIn(RIGHT)
	Sleep()
	Move.ArmOut(LEFT)
	Sleep()
	Move.ArmIn(LEFT)
	Sleep()

	Move.ElbowDown(RIGHT)
	Sleep()
	Move.ElbowUp(RIGHT)
	Sleep()
	Move.ElbowDown(LEFT)
	Sleep()
	Move.ElbowUp(LEFT)
	Sleep()


def CustomTest():
	Move = MoveClass()
	while (1):
		chan = input("Channel? ")
		val = input("Degree? ")
		Move.CustomMove(chan, val)
		time.sleep(1)

# ================================================================ #
if __name__ == "__main__":  
    print("Running servo tests...")
    CustomTest()
	TestAllServos()


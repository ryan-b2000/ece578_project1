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

	# ==== Total Face Reset ==== #
	def FaceReset(self):
		Eyebrow_Flat(RIGHT)
		Eyebrow_Flat(LEFT)
		Eye_Open(RIGHT)
		Eye_Open(LEFT)
		Eye_Center()
		Eye_Middle()
		Mouth_Close()
		Shoulder_Down(RIGHT)
		Shoulder_Down(LEFT)
		Arm_In(RIGHT)
		Arm_In(LEFT)
		Elbow_Up(RIGHT)
		Elbow_Up(LEFT)

	# ==== Eyebrow Movement ==== #
	def Eyebrow_Up(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Up")
			self.__Move(EYEBROW_R, 80)
		else:
			print("Left Eyebrow Up")
			self.__Move(EYEBROW_L, 80)

	def Eyebrow_Flat(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Center")
			self.__Move(EYEBROW_R, 120)
		else
			print("Left Eyebrow Center")
			self.__Move(EYEBROW_L, 120)

	def Eyebrow_Down(self, side):
		if (side == RIGHT):
			print("Right Eyebrow Center")
			self.__Move(EYEBROW_R, 140)
		else
			print("Left Eyebrow Center")
			self.__Move(EYEBROW_L, 140)


	# ==== Eyelid Movement ==== #
	def Eye_Open(self, side):
		if (side == RIGHT):
			print("Eyelid Right Open")
			self.__Move(EYELID_R, 90)
		else:
			print("Eyelid Left Open")
			self.__Move(EYEBROW_L, 120)

	def Eye_Close(self, side):
		if (side == RIGHT):
			print("Eyelid Right Close")
			self.__Move(EYELID_R, 150)
		else:
			print("Eyelid Left Close")
			self.__Move(EYELID_L, 60)


	# ==== Eye Horizontal Movement ==== #
	def Eye_Left(self):
		print("Eye Horizontal Left")
		self.__Move(EYE_HORIZONTAL, 80)

	def Eye_Center(self,channel,degree):
		print("Eye Horizontal Center")
		self.__Move(EYE_HORIZONTAL, 110)
	
	def Eye_Right(self):
		print("Eye Horizontal Right")
		self.__Move(EYE_HORIZONTAL, 160)


	# ==== Eye Horizontal Movement ==== #
	def Eye_Up(self):
		print("Eye Vertical Up")
		self.__Move(EYE_VERTICAL, 80)

	def Eye_Middle(self):
		print("Eye Vertical Middle")
		self.__Move(EYE_VERTICAL, 100)

	def Eye_Down(self):
		print("Eye Vertical Down")
		self.__Move(EYE_VERTICAL, 120)


	# ======== Mouth Movement ======== #
	def Mouth_Open(self):
		print("Mouth Open")
		self.__Move(MOUTH, 60)

	def Mouth_Close(self):
		print("Mouth Close")
		self.__Move(MOUTH, 0)


	# ======== Shoulder Movement ======== #
	def Shoulder_Up(self, side):
		if (side == RIGHT):
			print("Right Shoulder Up")
			self.__Move(ARM_ROTATE_R, 100)
		else:
			print("Left Shoulder Up")
			self.__Move(ARM_ROTATE_L, 100)

	def Shoulder_Down(self, side):
		if (side == RIGHT):
			print("Right Shoulder Down")
			self.__Move(ARM_ROTATE_R, 0)
		else:
			print("Left Shoulder Down")
			self.__Move(ARM_ROTATE_L, 0)


	# ======== Arm Movement ======== #
	def Arm_Out(self, side):
		if (side == RIGHT):
			print("Right Arm Out")
			self.__Move(ARM_SIDEWAYS_R, 100)
		else:
			print("Left Arm Out")
			self.__Move(ARM_SIDEWAYS_L, 100)

	def Arm_In(self, side):
		if (side == RIGHT):
			print("Right Arm In")
			self.__Move(ARM_SIDEWAYS_R, 0)
		else:
			print("Left Arm In")
			self.__Move(ARM_SIDEWAYS_L, 0)


	# ======== Elbow Movement ======== #
	def Elbow_Up(self, side):
		if (side == RIGHT):
			print("Right Elbow Up")
			self.__Move(ELBOW_R, 150)
		else:
			print("Left Elbow Up")
			self.__Move(ELBOW_L, 150)

	def Elbow_Down(self, side):
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
	while(1):
		chan = input("Channel? ")
		degree = 

# Test all servos 
def TestAllServos():
	Move = MoveClass()

	Move.FaceReset()

	Move.Eyebrow_Up(RIGHT)
	Sleep()
	Move.Eyebrow_Down(RIGHT)
	Sleep()
	Move.Eyebrow_Flat(RIGHT)
	Sleep()

	Move.Eyebrow_Up(LEFT)
	Sleep()
	Move.Eyebrow_Down(LEFT)
	Sleep()
	Move.Eyebrow_Flat(LEFT)
	Sleep()

	Move.Eye_Close(RIGHT)
	Sleep()
	Move.Eye_Open(RIGHT)
	Sleep()

	Move.Eye_Close(LEFT)
	Sleep()
	Move.Eye_Open(LEFT)
	Sleep()

	Move.Mouth_Open()
	Sleep()
	Move.Mouth_Close()
	Sleep()

	Move.Shoulder_Up(RIGHT)
	Sleep()
	Move.Shoulder_Down(RIGHT)
	Sleep()
	Move.Shoulder_Up(LEFT)
	Sleep()
	Move.Shoulder_Down(LEFT)
	Sleep()

	Move.Arm_Out(RIGHT)
	Sleep()
	Move.Arm_In(RIGHT)
	Sleep()
	Move.Arm_Out(LEFT)
	Sleep()
	Move.Arm_In(LEFT)
	Sleep()

	Move.Elbow_Down(RIGHT)
	Sleep()
	Move.Elbow_Up(RIGHT)
	Sleep()
	Move.Elbow_Down(LEFT)
	Sleep()
	Move.Elbow_Up(LEFT)
	Sleep()


# ================================================================ #
if __name__ == "__main__":  
    print("Running servo tests...")

	TestAllServos()
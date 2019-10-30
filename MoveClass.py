#! /usr/bin/env python3

'''	#################################################################################################

	DimBot Movement Class

	This class provides the methods for moving various parts of the DimBot.


''' 

#import Adafruit_PCA9685

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


	def Left_Eyebrow(self,channel,degree):
		# 80 \  | 140 /  | 120 flat -
		PCA9685.set_pwm(channel,0,degree)

	def Eyebrow_Up(self, side):
		if (side == 'Right'):
			print("Right Eyebrow Up")
			self.__Move(EYEBROW_R, 80)
		else:
			print("Left Eyebrow Up")
			self.__Move(EYEBROW_L, 80)


	def Right_Eyebrow(self,channel,degree):
		# 80 \  | 140 /  | 120 flat -
		PCA9685.set_pwm(channel,0,degree)

	def Eye_Left(self):
		print("eye left")

	def Eye_Center(self,channel,degree):
		# 110
		PCA9685.set_pwm(channel,0,degree)
	

	def Mouth(self,channel,degree):
		#60 open | 0 close
		PCA9685.set_pwm(channel,0,degree)
	
	def Right_Eye_Lid(self,channel,degree):
		#150 close | 90 open
		PCA9685.set_pwm(channel,0,degree)
	
	def Left_Eye_Lid(self,channel,degree):
		#60 close | 120 open
		PCA9685.set_pwm(channel,0,degree)

	def Eye_Vertical(self,channel,degree):
		#80 up | 120 down | 100 center
		PCA9685.set_pwm(channel,0,degree)
	
	def Eye_Horizontal(self,channel,degree):
		#160 left | 80 Right | 110 center
		PCA9685.set_pwm(channel,0,degree)

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



# ================================================================ #
if __name__ == "__main__":  
    print("Running servo tests...")

    Move = MoveClass()
    Move.Eyebrow_Up(RIGHT)
    Move.Eyebrow_Up(LEFT)

import Adafruit_PCA9685
import time

########################################################################################
# pwm channel number on PWM Driver
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

########################################################################################
# Min-Max angle settings
EYEBROW_R_MAX = 100
EYEBROW_R_MIN = 50

EYEBROW_L_MAX = 100
EYEBROW_L_MIN = 50

EYELID_R_MAX = 150
EYELID_R_MIN = 90

EYELID_L_MAX = 120
EYELID_L_MIN = 60

EYE_HORIZ_MAX = 100
EYE_HORIZ_MIN = 70

EYE_VERT_MAX = 80
EYE_VERT_MIN = 50

MOUTH_MAX = 50
MOUTH_MIN = 30

ARM_ROTATE_R_MAX = 100
ARM_ROTATE_R_MIN = 50

ARM_ROTATE_L_MAX = 100
ARM_ROTATE_L_MIN = 50

ARM_UPDOWN_R_MAX = 60
ARM_UPDOWN_R_MIN = 40

ARM_UPDOWN_L_MAX = 60
ARM_UPDOWN_L_MIN = 40

ELBOW_R_MAX = 100
ELBOW_R_MIN = 60

ELBOW_L_MAX = 90
ELBOW_L_MIN = 40



class ServoClass:

    def __init__(self, name):
        # Set the servo channel number
        self.__chan = name

        # Set safety checking parameters so servos dont stall out
        if self.__chan == EYEBROW_R:            # RIGHT EYEBROW
            self.__name = "Eyebrow R"
            self.__max = EYEBROW_R_MAX
            self.__min = EYEBROW_R_MIN

        elif self.__chan == EYEBROW_L:          # LEFT EYEBROW
            self.__name = "Eyebrow L"
            self.__max = EYEBROW_L_MAX
            self.__min = EYEBROW_L_MIN

        elif self.__chan == EYELID_R:           # RIGHT EYELID
            self.__name = "Eyelid R"
            self.__max = EYELID_R_MAX
            self.__min = EYELID_R_MIN

        elif self.__chan == EYELID_L:           # LEFT EYELID
            self.__name = "Eyelid L"
            self.__max = EYELID_L_MAX
            self.__min = EYELID_L_MIN

        elif self.__chan == EYE_HORIZONTAL:     # EYE HORIZONTAL
            self.__name = "Eye Horizontal"
            self.__max = EYE_HORIZ_MAX
            self.__min = EYE_HORIZ_MIN

        elif self.__chan == EYE_VERTICAL:       # EYE VERTICAL
            self.__name = "Eye Vertical"
            self.__max = EYE_VERT_MAX
            self.__min = EYE_VERT_MIN

        elif self.__chan == MOUTH:              # MOUTH
            self.__name = "Mouth"
            self.__max = MOUTH_MAX
            self.__min = MOUTH_MIN

        elif self.__chan == ARM_ROTATE_R:       # RIGHT SHOULDER ROTATE
            self.__name = "Arm Rotate R"
            self.__max = ARM_ROTATE_R_MAX
            self.__min = ARM_ROTATE_R_MIN

        elif self.__chan == ARM_ROTATE_L:       # LEFT SHOULDER ROTATE
            self.__name = "Arm Rotate L"
            self.__max = ARM_ROTATE_L_MAX
            self.__min = ARM_ROTATE_L_MIN

        elif self.__chan == ARM_UPDOWN_R:       # RIGHT ARM UP/DOWN
            self.__name = "Arm UpDown R"
            self.__max = ARM_UPDOWN_R_MAX
            self.__min = ARM_UPDOWN_R_MIN

        elif self.__chan == ARM_UPDOWN_L:       # LEFT ARM UP/DOWN
            self.__name = "Arm UpDown L"
            self.__max = ARM_UPDOWN_L_MAX
            self.__min = ARM_UPDOWN_L_MIN

        elif self.__chan == ELBOW_R:            # RIGHT ELBOW
            self.__name = "Elbow R"
            self.__max = ELBOW_R_MAX
            self.__min = ELBOW_R_MIN

        elif self.__chan == ELBOW_L:            # LEFT ELBOW
            self.__name = "Elbow L"
            self.__max = ELBOW_L_MAX
            self.__min = ELBOW_L_MIN

        else:
            print("Servo not recognized")
            self.__name = "Invalid"
            self.__max = 0
            self.__min = 0

        # Set the position to the minimum position
        self.__position = self.__min
        
        # Init an instance of the the PCA9685
        #self.__pca = Adafruit_PCA9685.PCA9685()  # Sets up the global member for the driver object
        #self.__pca.set_pwm_freq(40)              # set the frequency of the system as 50Hz
        print("PCA9685 initialized")


    #######################################################################################################
    def move(self, deg):
        # Safety check
        if deg == 0:
            deg = 0
        elif deg > self.__max:
            deg = self.__max
        elif deg < self.__min:
            deg = self.__min

        # Set position
        self.__position = deg

        # Convert degrees
        degree = int(deg)
        if degree > 0:
            degree = 2.75 * float(degree) + 40
        else:
            degree = 0
        degree = round(degree, 0)

        # Do the servo move
        #self.__pca.set_pwm(int(self.__chan), 0, int(degree))


    def getName(self):
        return self.__name


    def getPosition(self):
        return self.__position
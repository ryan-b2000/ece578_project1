#! /usr/bin/env python3

import Adafruit_PCA9685

pca = Adafruit_PCA9685.PCA9685()  # Sets up the global member for the driver object
pca.set_pwm_freq(40)              # set the frequency of the system as 50Hz
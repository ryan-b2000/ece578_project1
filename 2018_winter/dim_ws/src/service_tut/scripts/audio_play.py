#!/usr/bin/env python

#import cv as cv2
from std_msgs.msg import String
from std_msgs.msg import Int32
from service_tut.srv import *
import rospy
import time
import sys
import os
import Adafruit_PCA9685

def handle_service(data):
    a = str(data.req) + "1234"
    return a

def add_numbers():
    rospy.init_node("service_server")
    s = rospy.Service("add_numbers",myservice,handle_service)
    rospy.spin()

if __name__ == "__main__":
    add_numbers()


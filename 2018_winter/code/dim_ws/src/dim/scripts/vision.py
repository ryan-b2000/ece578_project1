#!/usr/bin/env python
#import cv as cv2
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import time
import sys
import os
import Adafruit_PCA9685

turn = 0

# Create a publisher of type Int32
pubVision = rospy.Publisher("vision_topic", Int32, queue_size = 1)

tempData = 0;

def callvision(data): 
        global turn
        turn = (turn+1)
        print(turn)
        tempData = turn
       # tempData = data
       # print(tempData)
        pubVision.publish(tempData)
        time.sleep(5)    

def test():    
    # Create Vision node
    rospy.init_node('vision_node', anonymous = True)
    rate = rospy.Rate(10)
    rospy.Subscriber("vision_topic", Int32, callvision)
    while not rospy.is_shutdown():
        pubVision.publish(0)
        rate.sleep()
     
if __name__ == '__main__':
    try:
        test()
    except rospy.ROSInterruptException:
        pass


#!/usr/bin/env python

'''
says a line if the line exists for the robot.
Then publishes increment to indicate its done.
If line is shared then don't publish
'''


import rospy
import wave
import time
import os
import sys
from subprocess import Popen

from std_msgs.msg import Int32
from std_msgs.msg import String


def lineCallback(data):
	line = data.data
	if(os.path.isfile("/home/lauren/turtle_ws/src/project2_play/scripts/dim/script1_line"+ str(line) +".wav")):
		pros = Popen("ffplay -autoexit -nodisp /home/lauren/turtle_ws/src/project2_play/scripts/dim/script1_line"+ str(line) +".wav", shell=True);
		pros.wait()
		increment.publish(line)
	return

rospy.init_node("Dim")
increment = rospy.Publisher('/increment', Int32, queue_size=1)
rospy.Subscriber("/lines",Int32,lineCallback)
rospy.spin()


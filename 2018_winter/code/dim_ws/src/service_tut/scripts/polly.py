#!/usr/bin/env python
import boto3
import rospy

#import actionlib
from std_msgs.msg import String, Bool
import time
from pygame import mixer
Text_Input="" 
p=""
end = rospy.Publisher('end',String,queue_size = 10)

def Speak_callback(data):
	global Text
	print("Session Created")
	polly_client = boto3.Session(
		        aws_access_key_id="AKIAIYIA4XOXYYJNSJLA",                     
	    aws_secret_access_key="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",
	    region_name='us-west-2').client('polly')
	print("Waiting for Callback")	
	
	Text_Input=data.data
	response = polly_client.synthesize_speech(VoiceId='Matthew',
		        OutputFormat='mp3', 
		        #Text = 'Robotics Sample Text.')
			Text = Text_Input)

	file = open('speech.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()
	
	time.sleep(2)
	mixer.init()
	mixer.music.load('/home/pi/dim_ws/speech.mp3')
	mixer.music.play()
	print("File Played")
	time.sleep(2)
	end.publish("end")
        print("end publish")


def polly():
	global Text	
	# Initializing the ROS node "polly_speech"	
	rospy.init_node("polly", anonymous=True)
	print("polly node init")
	# Creating Subscriber topics for Listen
	rospy.Subscriber("polly_listen",String,Speak_callback)
	
	rospy.spin()
if __name__ == '__main__':
	try:
		polly()
	except rospy.ROSInterruptexception:
		pass



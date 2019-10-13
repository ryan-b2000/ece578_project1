#!/usr/bin/env python

import pyaudio
import wave
import sys
import os
import rospy
from std_msgs.msg import String
from service_tut.srv import *

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def handle_request(data):
    a = str(data.req) + "1234"
    return a

# file path for the .wav file
homedir = os.environ['HOME']
filepath = homedir + "/dim_ws/src/service_tut/scripts"
user_input = os.path.join(filepath, WAVE_OUTPUT_FILENAME)

def record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    #rospy.spin()

if __name__ == '__main__':
    rospy.init_node("record_node")
    s = rospy.Service("request",myservice,handle_request)
    try:
        while True: 
            record()
    except KeyboardInterrupt:
        pass
        

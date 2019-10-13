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

# file path for the .wav file
homedir = os.environ['HOME']
filepath = homedir + "/dim_ws/src/service_tut/scripts"
user_input = os.path.join(filepath, WAVE_OUTPUT_FILENAME)

start = rospy.Publisher('start',String,queue_size = 10)

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
    start.publish("start")

def init_record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

    print("*init recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done init recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    start.publish("start")
    

def end_callback(data):
    record()

def recorder():
    rospy.init_node("record",anonymous = True)
    print("Record node init")
    init_record()
    rospy.Subscriber('end',String,end_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        recorder()
    except KeyboardInterrupt:
        pass
        

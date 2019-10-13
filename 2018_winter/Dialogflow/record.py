#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import pyaudio
import wave
from ctypes import *
import sys
import os

# some values for the recorder
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = user_input
RECORD_SECONDS = 5

# pyaudio objects
p = None
stream = None
frames = []
rec_data = None

# file path for the .wav file
homedir = os.environ['HOME']
filepath = homedir + "/recordings/"

#user_input = os.path.join(filepath, 'user_input.wav')
	


# this part rids of unnessary recorder error messages
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
	return
	
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

def record():
	global rec_data
	global frames
	global p
	global stream
	global flag
	
	user_input = os.path.join(filepath, 'user_input.wav')
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=CHANNELS, input_device_index=None, rate=RATE, input=True, frames_per_buffer=CHUNK)	

	print("recording")
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		rec_data = stream.read(CHUNK)
		frames.append(rec_data)

	stream.stop_stream()
	stream.close()
	p.terminate()
	asound.snd_lib_error_set_handler(None)
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	rec_data = None
	frames = []
	print ("stoped")
	flag = 0

if __name__ == '__main__':
    record()

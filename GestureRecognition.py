import os
import cv2
from aip import AipBodyAnalysis
from threading import Thread
import base64
import requests

""" 你的 APPID AK SK """
APP_ID = '17857142'
API_KEY = 'iCVVTjwfZKPG6xNaGe6RiwNy'
SECRET_KEY =  'vR56VlAj86Ge5DxRWc3r7tebnIBKgrSD'
access_token = '24.81f7c15d29c61166d891fd05519bf326.2592000.1577321280.282335-17857142'

#gesture_client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

#capture = cv2.VideoCapture(0)#0为默认摄像头
#s, image = capture.read()
#cv2.imwrite('/home/zhe/Desktop/ece578_project1/images/3.jpg', image)
def get_gesture():
    APP_ID = '17857142'
    API_KEY = 'iCVVTjwfZKPG6xNaGe6RiwNy'
    SECRET_KEY = 'vR56VlAj86Ge5DxRWc3r7tebnIBKgrSD'
    access_token = '24.81f7c15d29c61166d891fd05519bf326.2592000.1577321280.282335-17857142'
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture"
    f = open('/home/zhe/Desktop/ece578_project1/images/3.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        result = response.json()
        print(result)
        for res in result['result']:
            if res['classname'] == 'Two':
                final_result = 'scissors'
            elif res['classname'] == 'Five':
                final_result = 'paper'
            elif res['classname'] == 'Fist':
                final_result = 'rock'
    return final_result

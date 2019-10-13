#!/bin/bash

cd dim_ws
echo $PWD
source devel/setup.bash
export GOOGLE_APPLICATION_CREDENTIALS='/home/pi/dim_ws/src/service_tut/scripts/Dimbot-f9e25ceb61ad.json'
roscore > /dev/stdout &
sleep 7 && echo Roscore running in background......
rosrun service_tut polly.py > /dev/stdout &
sleep 3 && echo polly.py running in background...... 
rosrun service_tut dialogflow.py > /dev/null &
sleep 3 && echo dialogflow.py running in background...... 
rosrun service_tut record.py > /dev/null &
sleep 3 && echo record.py running in background...... 
rosrun service_tut body.py > /dev/null &
echo body.py running in background...... 



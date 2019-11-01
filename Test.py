#! /usr/bin/env python3

# Handles the main testing for the robot

def main_test():
    time.sleep(0.8)
    Robo_face = Face()
    Robo_face.Face_Reset()
    print("I am working on test my body! If my movement is not matched to my words, it means something is broken!")
    speaking_main('I am working on test my body! If my movement is not matched to my words, it means something is broken!')
    time.sleep(0.8)
    
    #test eyebrows
    #Right Eyebrow   channel_0   |   80 \  | 140 /  | 120 flat -
    speaking_main('I am testing my eyebrows')
    time.sleep(1)
    speaking_main('I am testing my right eyebrow')
    pwm.set_pwm(pwm_channel_0,0,degree_80)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_120)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_140)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_120)
    time.sleep(0.8)

    #Left Eyebrow   channel_1   |   80 \  | 140 /  | 120 flat -
    speaking_main('I am testing my left eyebrow')
    pwm.set_pwm(pwm_channel_1,0,degree_80)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_1,0,degree_120)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_1,0,degree_140)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_1,0,degree_120)
    time.sleep(0.8)

    speaking_main('I am testing my both eyebrows')
    pwm.set_pwm(pwm_channel_0,0,degree_80)
    pwm.set_pwm(pwm_channel_1,0,degree_80)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_120)
    pwm.set_pwm(pwm_channel_1,0,degree_120)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_140)
    pwm.set_pwm(pwm_channel_1,0,degree_140)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_0,0,degree_120)
    pwm.set_pwm(pwm_channel_1,0,degree_120)
    time.sleep(0.8)

    speaking_main('I am testing my eyes')    

    #Left and Right Horizontal  channel_4 | 160 left | 80 Right | 110 center
    speaking_main('I am rotating my eyes Horizontally')
    pwm.set_pwm(pwm_channel_4,0,degree_160)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_4,0,degree_110)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_4,0,degree_80)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_4,0,degree_110)
    time.sleep(0.8)
    #Left and Right Vertical  channel_5 |  80 up | 120 down | 100 center
    speaking_main('I am rotating my eyes vertically')
    pwm.set_pwm(pwm_channel_5,0,degree_80)
    time.sleep(0.8)   
    pwm.set_pwm(pwm_channel_5,0,degree_100)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_5,0,degree_120)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_5,0,degree_100)
    time.sleep(0.8)

    #Test Lid
    #Right Eye Lid  channel_2   |   150 close | 90 open
    #Left Eye Lid  channel_3   |   60 close | 120 open
    speaking_main('I am winking my right eye')
    pwm.set_pwm(pwm_channel_2,0,degree_150)
    time.sleep(0.8)   
    pwm.set_pwm(pwm_channel_2,0,degree_90)
    time.sleep(0.8)
    speaking_main('I am winking my left eye')
    pwm.set_pwm(pwm_channel_3,0,degree_60)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_3,0,degree_120)
    time.sleep(0.8)
    speaking_main('I am winking my both eyes')   
    pwm.set_pwm(pwm_channel_2,0,degree_150)
    pwm.set_pwm(pwm_channel_3,0,degree_60)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_2,0,degree_90)
    pwm.set_pwm(pwm_channel_3,0,degree_120)
    time.sleep(0.8)

    #mouth
    speaking_main('I am testing my mou... Oh! It is working!')

    #Right Shoulder joint   channel_7
    #Left Shoulder joint    channel_8
    #Right Arm_side ways    channel_9   |   outside 90 | inside 120 
    #Left Arm_side ways     channel_10
    #Right Elbow            channel_11  |   High   150 | Low 170 
    #Left Elbow             channel_12
    speaking_main('I am testing my shoulders')

    speaking_main('I am rotating my right shoulder')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_7,0,degree_90)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_7,0,degree_120)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_7,0,degree_90)
    
    speaking_main('I am rotating my left shoulder')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_8,0,degree_0)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_8,0,degree_30)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_8,0,degree_0)

    speaking_main('I am testing my elbow')
    speaking_main('I am moving my right arm down and up')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_11,0,degree_150)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_11,0,degree_170)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_11,0,degree_150)

    speaking_main('I am moving my left arm down and up')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_12,0,degree_60)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_12,0,degree_90)
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_12,0,degree_60)

    speaking_main('I am turning my right arm right')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_9,0,degree_90)
    time.sleep(0.8)
    
    speaking_main('I am turning my right arm left')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_9,0,degree_120)
    time.sleep(0.8)

    speaking_main('I am turning my left arm left')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_8,0,degree_0)
    time.sleep(0.8)
    
    speaking_main('I am turning my left arm right')
    time.sleep(0.8)
    pwm.set_pwm(pwm_channel_8,0,degree_30)
    time.sleep(0.8)
    speaking_main('I have done!')
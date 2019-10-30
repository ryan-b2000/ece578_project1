#! /usr/bin/env python3

# ======================= ROBOT SPEAKING ======================= #    
#
# The function makes robot speak like a human. Say the words and move the
# mouth at the same time 

import time
import MoveClass

Flag = 1    # Keep mouth moving as long as audio is being produced

def Speak(content):
    def speech_ouput(content):
        Flag = 1
        #os.system('flite -t "%s"'%content)
        os.system('flite -voice rms -t "%s"'%content)
        Flag = 0

    def move_mouth():
        Move = MoveClass()
        while Flag:
            Move.MouthOpen()
            time.sleep(0.6)
            Move.MouthClose()
            time.sleep(0.6)

    # Use multithreading library named threading
    thread1 = threading.Thread(target=lambda: speak(content))
    thread2 = threading.Thread(target=mouth)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Finished speaking function")


# ================================================================ #
if __name__ == "__main__":  
    print("Running speech testing")

    Speak("Hello this is a test")

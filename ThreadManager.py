#! /usr/bin/env python3

import time
import threading

Flag = True
lock = threading.Condition()

def ThreadB():
    print("Thread B")
    global Flag
    while (True):
        print("Mouth open")
        time.sleep(0.5)
        print("Mouth close")
        time.sleep(0.5)
        
        lock.acquire()
        if (Flag == False):
            print("B: Flag is false")
            break
        lock.release()

def ThreadA():
    print("Thread A")
    global Flag

    time.sleep(3)
    lock.acquire()
    Flag = False
    print("A: Flag is false")
    lock.release()


def TestThreading():
    print("Testing Multithreading")
    mouth = threading.Thread(target=ThreadA)
    voice = threading.Thread(target=ThreadB)
    mouth.start()
    voice.start()
    mouth.join()
    voice.join()

# ================================================================ #
if __name__ == "__main__": 
    TestThreading()
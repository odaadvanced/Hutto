import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import RPi.GPIO as GPIO
import asyncio

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
import time

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

GPIO.setmode(GPIO.BCM)

right_trigger = 20
right_echo = 21
left_trigger = 27
left_echo = 24
GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

def distance_left():
    GPIO.output(left_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(left_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(left_echo) == 0:
        start_time = time.time()
        
    while GPIO.input(left_echo) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance
        
def distance_right():
    GPIO.output(right_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(right_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(right_echo) == 0:
        start_time = time.time()
        
    while GPIO.input(right_echo) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance
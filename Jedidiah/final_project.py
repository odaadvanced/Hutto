import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from oled_io import Oled_io
import photoresistor
import color_detection
import RPi.GPIO as GPIO
import asyncio
import random

display = Oled_io()
rvr = SpheroRvrObserver()

def display_speed():
    speed = random.randint(0,30)    
    return speed

rvr.wake()
time.sleep(2)
rvr.reset_yaw()
    
while True:
    try:        
        time.sleep(2)
        display.print(str(display_speed()))
        rvr.drive_with_heading(
            speed=display_speed(),  # Valid speed values are 0-255
            heading=90,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )
    
    except KeyboardInterrupt:
        print('Program terminated by keyboard interrupt.')
        
   # finally:
    #    rvr.close()
    
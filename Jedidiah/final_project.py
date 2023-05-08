import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from oled_io import Oled_io
#import photoresistor
#import color_detection
#import RPi.GPIO as GPIO
import asyncio
import random

display = Oled_io()
#rvr = SpheroRvrObserver()
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

def display_speed():
    speed2 = random.randint(0,30)    
    return speed2

async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)   
    while True:            
        new_speed = display_speed()
        display.print(str(new_speed))
        await rvr.drive_with_heading(new_speed,0,0)
        await asyncio.sleep(2)
        
try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
    
except KeyboardInterrupt:
    print('Program terminated by keyboard interrupt.')
    GPIO.cleanup()    
   # finally:
    #    rvr.close()
    
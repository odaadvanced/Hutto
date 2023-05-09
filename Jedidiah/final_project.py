import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from oled_io import Oled_io
import RPi.GPIO as GPIO
import asyncio
import random
from ultrasonic_sensor import distance_left, distance_right
from PiAnalog import *
from light_sensor import light_from_r

display = Oled_io()
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
p = PiAnalog()
multiplier = 2000

GPIO.setmode(GPIO.BCM)

right_trigger = 20
right_echo = 21
left_trigger = 27
left_echo = 24
GPIO.setwarnings(False)
GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

def display_speed():
    speed2 = random.randint(10,30)    
    return speed2

def detect_light():
    light = light_from_r(p.read_resistance())
    reading_str = "{:.0f}".format(light)
    return reading_str
    
async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)  
    while True:        
        new_speed = display_speed()
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        print('Measurements are {0:.2f} cm right and {1:.2f} cm left'.format(dist_r, dist_l))
        light_amount = detect_light()
        print(f"The light reading is {light_amount}.")
        if dist_r < 50:
            while dist_r < 50:
                await rvr.raw_motors(2, 255, 1, 255)
                dist_r = distance_right()
                await asyncio.sleep(.05)
                print('turning right')
                await rvr.reset_yaw()
        elif dist_l < 50:
            while dist_l < 50:
                await rvr.raw_motors(1, 255, 2, 255)
                dist_l = distance_left()
                await asyncio.sleep(.05)
                print('turning left')
                await rvr.reset_yaw()
        elif dist_l >= 50 and dist_r >= 50:
            display.print(str(new_speed))        
            await rvr.drive_with_heading(new_speed,0,2)
            await asyncio.sleep(5)
        
try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
    
except KeyboardInterrupt:
    print('Program terminated by keyboard interrupt.')
    GPIO.cleanup()    

finally:
    rvr.close()
    
import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from gpiozero import DigitalOutputDevice

import RPi.GPIO as GPIO
import asyncio
from PiAnalog import *
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
import time
pin1 = DigitalOutputDevice(26)
pin2 = DigitalOutputDevice(25)
p = PiAnalog()

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups


rvr2 = SpheroRvrObserver()

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal = SerialAsyncDal(
        loop
    )
)
GPIO.setmode(GPIO.BCM)

right_trigger = 23
right_echo = 24
left_trigger = 20
left_echo = 21

GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

def color():
    rvr2.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in [255, 255, 0]]
    )

def set():
    rvr2.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in [255, 0, 0]]
    )

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

async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)
    while True: 
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        print('Measurements are {0} cm right and {1} cm left'.format(dist_r, dist_l))
        if dist_r < 35:
            while dist_r < 35:
                await rvr.raw_motors(2, 255, 1, 255)
                dist_r =  distance_right()
                await asyncio.sleep(.05)
                print('turning right')
                buzz(2000, 1)
                set()
            await rvr.reset_yaw()
        elif dist_l < 35:
            while dist_l < 35:
                await rvr.raw_motors(1, 255, 2, 255)
                dist_l =   distance_left()
                await asyncio.sleep(.05)
                print('turning left')
                buzz(2000, 1)
                set()
            await rvr.reset_yaw()
        elif dist_l >= 35 and dist_r >= 35:
            current_speed = random.randint(0, 30)
            rvr.drive_with_heading(current_speed, 0, 0)	
            display.print(current_speed)
            time.sleep(2) 
            reset()

try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
except KeyboardInterrupt:
    print('Program ended by KeyboardInterrupt')
    GPIO.cleanup()
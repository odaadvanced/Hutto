import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import RPi.GPIO as GPIO
import asyncio

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
import time
from PiAnalog import *
from gpiozero import DigitalOutputDevice

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
rvr2 = SpheroRvrObserver()
GPIO.setmode(GPIO.BCM)

right_trigger = 20
right_echo = 21
left_trigger = 23
left_echo = 24
pin1 = DigitalOutputDevice(17)
pin2 = DigitalOutputDevice(27)
p = PiAnalog()

GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

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

def rvr_set_color(num1, num2, num3):
    rvr2.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in [num1, num2, num3]]
    )
    
def rvr_reset_color():
    rvr2.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
    )
async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)    
    while True:
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        print('Measurements are {0} cm right and {1} cm left'.format(dist_r, dist_l))
        if dist_r < 80:
            rvr_set_color(255, 0, 0)
            buzz(2000, 0.5)
            if dist_r < 70:
                rvr_set_color(255, 140, 0)
            if dist_r < 60:
                rvr_set_color(255, 255, 0)
            if dist_r < 50:
                rvr_set_color(0, 255, 0)
                while dist_r < 50:
                    await rvr.raw_motors(2, 255, 1, 255)
                    dist_r = distance_right()
                    await asyncio.sleep(.05)
                    print('turning right')
                await rvr.reset_yaw()
        elif dist_l < 80:
            rvr_set_color(128, 0, 128)
            buzz(2000, 0.5)
            if dist_r < 70:
                rvr_set_color(75, 0, 130)
            if dist_r < 60:
                rvr_set_color(0, 0, 255)
            if dist_l < 50:
                rvr_set_color(173, 255, 47)            
                while dist_l < 50:
                    await rvr.raw_motors(1, 255, 2, 255)
                    dist_l = distance_left()
                    await asyncio.sleep(.05)
                    print('turning left')
                await rvr.reset_yaw()
        elif dist_l >= 80 and dist_r >= 80:
            rvr_reset_color()
            await rvr.drive_with_heading(40, 0, 0)

try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )

except KeyboardInterrupt:
    print("Program ended by KeyboardInterrupt")
    GPIO.cleanup()
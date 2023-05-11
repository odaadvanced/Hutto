import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RvrStreamingServices
from oled_io import Oled_io
import RPi.GPIO as GPIO
import asyncio
import random
from ultrasonic_sensor import distance_left, distance_right
from PiAnalog import *
from PiAnalogThermistor import *
from light_sensor import light_from_r
from thermometer_plus import buzz
from rgb_led import color_changed
from pathlib import Path
from color_detection import color_detected_handler

display = Oled_io()
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
p = PiAnalog()
p2 = PiAnalogThermistor()
multiplier = 2000                     #Used for phototransistor: increase to make detections more sensitive
detection_file_path = Path.home()/'color_data.txt'
other_detection_file_path = Path.home()/'immediate_color_data.txt'

GPIO.setmode(GPIO.BCM)              #Broadcom mode

right_trigger = 20     #Setting up GPIO pins for the ultrasonic sensors.
right_echo = 21
left_trigger = 27
left_echo = 24
GPIO.setwarnings(False)
GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

def display_speed():
    speed2 = random.randint(10,30)    #Speed of rover is number between 10 and 30 (possible range is 0-255).
    return speed2

def detect_light():
    light = light_from_r(p.read_resistance())
    reading_str = "{:.0f}".format(light)
    return reading_str
   
def detect_temp():
    temp = p2.read_temp_f()
    temperature = "%.2f" % temp
    return temp

def detect_color():
    global other_detection_file_path
    with open(other_detection_file_path, mode= 'r', encoding = 'utf-8') as file:
        text = file.read()            #Reads information about color detection from immediate_color_data.txt
        list_text = text.split(", ")
    return list_text
            
async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)  
    while True:        
        global detection_file_path
        await rvr.wake()

    # Give RVR time to wake up
        await asyncio.sleep(2)
        with detection_file_path.open(mode = 'w', encoding = 'utf-8') as file:
            file.write('')                                #Writes information from color_data.txt
        await rvr.enable_color_detection(is_enabled=True)
        await rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.color_detection,
            handler=color_detected_handler
        )
        await rvr.sensor_control.start(interval=250)
        color_changed(detect_color()[0], detect_color()[1], detect_color()[2])
        await asyncio.sleep(1)
        new_speed = display_speed()
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        print('Measurements are {0:.2f} cm right and {1:.2f} cm left'.format(dist_r, dist_l))
        light_amount = detect_light()
        print(f"The light reading is {light_amount}.")
        temperature_outside = detect_temp()
        print(f'The temperature is {temperature_outside} F.')
        if dist_r < 50:
            buzz(2000, 0.5)
            while dist_r < 50:
                await rvr.raw_motors(2, 255, 1, 255)
                dist_r = distance_right()
                await asyncio.sleep(.05)
                print('turning right')
                await rvr.reset_yaw()
        elif dist_l < 50:
            buzz(2000, 0.5)
            while dist_l < 50:
                await rvr.raw_motors(1, 255, 2, 255)
                dist_l = distance_left()
                await asyncio.sleep(.05)
                print('turning left')
                await rvr.reset_yaw()
        elif dist_l >= 50 and dist_r >= 50:
            display.print(str(new_speed))        
            await rvr.drive_with_heading(new_speed,0,2)
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

finally:    
    time.sleep(.5)    
    rvr.close()    
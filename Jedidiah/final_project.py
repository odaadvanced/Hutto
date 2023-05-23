import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RvrStreamingServices
from sphero_sdk import RvrLedGroups
from sphero_sdk import Colors
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
from picamera import PiCamera
import subprocess

display = Oled_io()
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
display_camera = PiCamera()
directory_location = '/home/pi/dev/hutto/Jedidiah/photos_directory'
directory_path = Path(directory_location)
directory_path.mkdir(exist_ok = True)
for file in os.scandir(directory_location):
    os.remove(file.path)
p = PiAnalog()
p2 = PiAnalogThermistor()
picture_number = 0
sound_file = '/home/pi/dev/hutto/Jedidiah/output.mp3'
shourt_sound_file = '/home/pi/dev/hutto/Jedidiah/short_poem.mp3'
multiplier = 2000                     #Used for phototransistor: increase to make detections more sensitive
color_data = Path.home()/'dev'/'hutto'/'Jedidiah'/'color_data.txt'
color_data.touch()
immediate_color_data = Path.home()/'dev'/'hutto'/'Jedidiah'/'immediate_color_data.txt'
immediate_color_data.touch()
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
    slow_speed = random.randint(10, 16)
    fast_speed = random.randint(24, 30)
    speed2 = random.choice([slow_speed, fast_speed])    
    return speed2

def detect_light():
    light = light_from_r(p.read_resistance())
    reading_str = "{:.0f}".format(light)
    return reading_str
   
def detect_temp():
    temp = p2.read_temp_f()
    temperature = "{:.2f}".format(temp)
    return temperature

def detect_color():
    global immediate_color_data
    with open(immediate_color_data, mode= 'r', encoding = 'utf-8') as file:
        text = file.read()            #Reads information about color detection from immediate_color_data.txt
        list_text = text.split(", ")
    return list_text

async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)
    display_camera.start_preview(alpha=200)
    await rvr.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
    )
    global color_data
    global picture_number
    global sound_file
    with color_data.open(mode = 'w', encoding = 'utf-8') as file:
        file.write('')
    subprocess.call(['xdg-open', sound_file])
    while True:
        await rvr.wake()    # Give RVR time to wake up
        await asyncio.sleep(.05)                                        #Writes information from color_data.txt
        await rvr.enable_color_detection(is_enabled=True)
        await rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.color_detection,
            handler=color_detected_handler
        )
        await rvr.sensor_control.start(interval=250)
        await asyncio.sleep(.05)
        color_changed(detect_color()[0], detect_color()[1], detect_color()[2])
        await asyncio.sleep(2)
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
            picture_number += 1
            while dist_r < 50:
                await rvr.raw_motors(2, 150, 1, 150)
                dist_r = distance_right()
                await asyncio.sleep(.05)
                print('turning right')
                await rvr.reset_yaw()
        elif dist_l < 50:
            buzz(2000, 0.5)
            picture_number += 1
            while dist_l < 50:
                await rvr.raw_motors(1, 150, 2, 150)
                dist_l = distance_left()
                await asyncio.sleep(.05)
                print('turning left')
                await rvr.reset_yaw()
        elif dist_l >= 50 and dist_r >= 50:
            display.print(str(new_speed))
            display_camera.capture('/home/pi/dev/hutto/Jedidiah/photos_directory/my_photo%s.jpg' % picture_number)
            if new_speed >= 24:                
                await rvr.drive_with_heading(new_speed,0,2)                
                for blink in range(7):
                    await rvr.set_all_leds(
                        led_group=RvrLedGroups.all_lights.value,
                        led_brightness_values=[color for x in range(10) for color in [255, 0, 0]]
                    )
                    await asyncio.sleep(0.1)
                    await rvr.set_all_leds(
                        led_group=RvrLedGroups.all_lights.value,
                        led_brightness_values=[color for x in range(10) for color in [255, 255, 255]]
                    )
                    await asyncio.sleep(0.1)
                    await rvr.set_all_leds(
                        led_group=RvrLedGroups.all_lights.value,
                        led_brightness_values=[color for x in range(10) for color in [0, 0, 255]]
                    )
                    await asyncio.sleep(0.1)                
            else:
                await rvr.drive_with_heading(new_speed,0,2)
                await asyncio.sleep(1.95)
    await rvr.close()
 
try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
    
except KeyboardInterrupt:
    print('Program terminated by keyboard interrupt.')
    subprocess.call(['xdg-open', short_sound_file])
    display_camera.stop_preview()
    display_camera.close()
    GPIO.cleanup()

finally:    
    time.sleep(.5)    
    rvr.close()    
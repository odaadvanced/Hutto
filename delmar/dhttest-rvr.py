import os
import sys
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from guizero import *

import RPi.GPIO as GPIO
import dht11python as dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
count = 0


rvr = SpheroRvrObserver()

rvr.wake()

# Give RVR time to wake up
time.sleep(2)

rvr.reset_yaw()


# read data using gpio 4

def update_temp():
    global count
 #   while True: 
    instance = dht11.DHT11(pin = 4)
    temperature = instance.read()
    temperature = temperature.temperature;


    temperature = "%.2f" % temperature # Round the temperature to 2 d.p.
    temp_text.value = temperature
    count = count + 1
    print (f'temperature = {temperature} count = {count}')
    
    result = instance.read()

    if result.is_valid():
        temp_text.value = result.temperature

        if result.temperature <= 17.8 :
            rvr.drive_with_heading(
                speed=10,  # Valid speed values are 0-255
                heading=0,  # Valid heading values are 0-359
                flags=DriveFlagsBitmask.none.value
            )
        else :
           rvr.drive_with_heading(
                speed=10,  # Valid speed values are 0-255
                heading=0,  # Valid heading values are 0-359
                flags=DriveFlagsBitmask.drive_reverse.value
            )
      
    temp_text.after(1000, update_temp)
    

app = App(title = "Thermometer", width="400", height="300")
Text(app, text="Temp F", size=32)
temp_text = Text(app, text="0.00", size=110)
temp_text.after(1, update_temp) # Used to update the temperature reading

app.display()       






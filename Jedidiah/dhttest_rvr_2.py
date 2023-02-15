import os
import sys
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
import RPi.GPIO as GPIO
import dht11python as dht11
from PiAnalog import *
from guizero import App, Text
from gpiozero import DigitalOutputDevice
p = PiAnalog()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #Broadcom mode
GPIO.cleanup()
rvr = SpheroRvrObserver()

# read data using pin 14
def update_temp():
    temperature = p.read_temp_f()
    temperature = "%.2f" % temperature # Round the temperature to 2 d.p.
    temp_text.value = temperature
    temp_text.after(1000, update_temp)

# Create the GUI

def main ():
    rvr.wake()
    
    #Give RVR time to wake up
    time.sleep(2)
    rvr.reset_yaw()
    
    while True:
        instance = dht11.DHT11(pin = 7)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            app = App(title = "Thermometer", width="400", height="300")
            Text(app, text="Temp F", size=32)
            temp_text = Text(app, text="0.00", size=110)
            temp_text.after(1000, update_temp) # Used to update the temperature reading
            app.display()
#    else:
#        print("Error: %d" % result.error_code)
        
        if result.temperature <= 22.7:
            rvr.drive_with_heading(
                speed = 10, #Valid speed values are 0-255
                heading = 0, #Valid heading values are 0-359
                flags=DriveFlagsBitmask.none.value
                )
        else:
            rvr.drive_with_heading(
                speed = 10,
                heading = 0,
                flags = DriveFlagsBitmask.drive_reverse.value
                )               
        
        if result.humidity <= 47.0:
            rvr.drive_with_heading(
                speed = 10,
                heading = 90,
                flags=DriveFlagsBitmask.none.value
                )
            
        time.sleep(2)

if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        rvr.close()
        GPIO.cleanup()

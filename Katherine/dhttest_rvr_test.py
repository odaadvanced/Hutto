import os
import sys
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
import RPi.GPIO as GPIO
import dht11python as dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Broadcom mode
GPIO.cleanup()

rvr = SpheroRvrObserver()
# read data using pin 14
def main():
    rvr.wake()
    time.sleep(2)
    rvr.reset_yaw()

    while True:
        instance = dht11.DHT11(pin = 7)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
    #    else:
    #        print("Error: %d" % result.error_code)
        if result.temperature <= 24.1:
            time.sleep(2)
            rvr.drive_with_heading(
                speed = 10,
                heading = 0,
                flags = DriveFlagsBitmask.none.value
                )
        else:
            rvr.drive_with_heading(
                speed = 10,
                heading = 0,
                flags = DriveFlagsBitmask.drive_reverse.value
                )
        if result.temperature <= 36:
            time.sleep(2)
            rvr.drive_with_heading(
                speed = 10,
                heading = 90,
                flags = DriveFlagsBitmask.none.value
                )
        else:
            rvr.drive_with_heading(
                speed = 10,
                heading = 270,
                flags = DriveFlagsBitmask.drive_reverse.value
                )
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        rvr.close()
        GIPIO.cleanup()
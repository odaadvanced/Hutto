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
GPIO.setmode(GPIO.BOARD)
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
        if result.temperature <= 23.3:
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
    temp_text.after(1000, update_temp)
    
        if result.humidity <= 50.0:
            rvr.drive_with_heading(
                speed = 10,
                heading = 90,
                flags = DriveFlagsBitmask.none.value
                    )
        else:
            rvr.drive_with_heading(
                speed = 10,
                heading = 270,
                flags = DriveFlagsBitmask.none.value
                    )
 
        time.sleep(2)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program ended by KeyboardInterupt")
        rvr.close()
        GPIO.cleanup()
app = App(title = "Thermometer", width = "400", height = "300")
Text(app, text = "Temp F", size = 32)
temp_text = Text(app, text = "0.00", size = 110)

app.display()
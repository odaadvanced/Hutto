import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from oled_io import Oled_io
import photoresistor
import color_detection
import ultrasonic_sensor
import time

display = Oled_io()
rvr = SpheroRvrObserver()
#
#def display_speed():
 #   speed = random.randint(0,30)
  #  display.print(speed)
   # time.sleep(10)
    #return speed
rvr.wake()
time.sleep(2)

while True:    
    rvr.reset_yaw()
    #display_speed()
    rvr.drive_with_heading(30, 10, 10)
    
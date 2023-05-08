from oled_io import Oled_io
import photoresistor
import color_detection
import ultrasonic_sensor
import time

display = Oled_io()

def display_speed():
    speed = random.randint(0,30)
    rvr.drive_with_heading(speed, 0, 0)
    display.print(speed)
    time.sleep(10)
    
while True:
    rvr.wake()
    display_speed()
    
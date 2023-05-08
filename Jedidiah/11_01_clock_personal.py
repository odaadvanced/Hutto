# 11_01_clock.py

import time
from datetime import datetime
from oled_io import Oled_io

display = Oled_io()

show_colon = True

while True:
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print(type(current_time))
        display.print(current_time)
        if show_colon:
            display.colon = True
            show_colon = False
        else:
            display.colon = False
            show_colon = True
        time.sleep(0.5)
    except:
        print("Didn't work.")
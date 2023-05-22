import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from pathlib import Path

loop = asyncio.get_event_loop()
detect_file_path = Path.home()/'dev'/'hutto'/'Jedidiah'/'color_data.txt'
detect_file_path.touch()
local_detection_file_path = Path.home()/'dev'/'hutto'/'Jedidiah'/'immediate_color_data.txt'
local_detection_file_path.touch()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
with detect_file_path.open(mode = 'w', encoding = 'utf-8') as file:
    file.write('')
    
async def color_detected_handler(color_detected_data):   
    global detect_file_path
    global local_detection_file_path
    with detect_file_path.open(mode = 'a', encoding  = 'utf-8') as file:
        file.write(str(color_detected_data["ColorDetection"]["R"]) + ', ')
        file.write(str(color_detected_data["ColorDetection"]["G"]) + ', ')
        file.write(str(color_detected_data["ColorDetection"]["B"]) + '\n')
    with local_detection_file_path.open(mode = 'w', encoding = 'utf-8') as file_2:
        file_2.write(str(color_detected_data["ColorDetection"]["R"]) + ', ')
        file_2.write(str(color_detected_data["ColorDetection"]["G"]) + ', ')
        file_2.write(str(color_detected_data["ColorDetection"]["B"]))
        
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from pathlib import Path

loop = asyncio.get_event_loop()
detection_file_path = Path.home()/'dev'/'hutto'/'Jedidiah'/'color_data.txt'
detection_file_path.touch()
other_detection_file_path = Path.home()/'dev'/'hutto'/'Jedidiah'/'immediate_color_data.txt'
other_detection_file_path.touch()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

async def color_detected_handler(color_detected_data):   
    global detection_file_path
    global other_detection_file_path
    with detection_file_path.open(mode = 'a', encoding  = 'utf-8') as file:
        file.write(str(color_detected_data["ColorDetection"]["R"]) + ', ')
        file.write(str(color_detected_data["ColorDetection"]["G"]) + ', ')
        file.write(str(color_detected_data["ColorDetection"]["B"]) + '\n')
    with other_detection_file_path.open(mode = 'w', encoding = 'utf-8') as file_2:
        file_2.write(str(color_detected_data["ColorDetection"]["R"]) + ', ')
        file_2.write(str(color_detected_data["ColorDetection"]["G"]) + ', ')
        file_2.write(str(color_detected_data["ColorDetection"]["B"]))
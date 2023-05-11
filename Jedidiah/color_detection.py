import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
#from sphero_sdk import RvrStreamingServices
from pathlib import Path

loop = asyncio.get_event_loop()
detection_file_path = Path.home() / "color_data.txt"
other_detection_file_path = Path.home() / 'immediate_color_data.txt'
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

# async def main():
#     """ This program demonstrates how to use the color sensor on RVR (located on the down side of RVR, facing the floor)
#         to report colors detected. To exit program, press <CTRL-C>
#     """
#     global detection_file_path
#     await rvr.wake()
# 
#     # Give RVR time to wake up
#     await asyncio.sleep(2)
#     with detection_file_path.open(mode = 'w', encoding = 'utf-8') as file:
#         file.write('')
# 
#     await rvr.enable_color_detection(is_enabled=True)
#     await rvr.sensor_control.add_sensor_data_handler(
#         service=RvrStreamingServices.color_detection,
#         handler=color_detected_handler
#     )
#     await rvr.sensor_control.start(interval=250)
# 
#     while True:
#         await asyncio.sleep(1)
# 
# 
# if __name__ == '__main__':
#     try:
#         asyncio.ensure_future(
#             main()
#         )
#         loop.run_forever()
# 
#     except KeyboardInterrupt:
#         print('\nProgram terminated with keyboard interrupt.')
# 
#         loop.run_until_complete(
#             asyncio.gather(
#                 rvr.enable_color_detection(is_enabled=False),
#                 rvr.close()
#             )
#         )
# 
#     finally:
#         if loop.is_running():
#             loop.close()

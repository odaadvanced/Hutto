import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RvrStreamingServices


loop = asyncio.get_event_loop()

rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

async def color_detected_handler(color_detected_data):
    global color_data_red
    global color_data_green
    global color_data_blue
    color_data_red = (color_detected_data['ColorDetection']["R"])
    color_data_green = (color_detected_data['ColorDetection']['G'])
    color_data_blue = (color_detected_data['ColorDetection']['B'])
    return(color_data_red, color_data_green, color_data_blue)
    
async def color_main():
    """ This program demonstrates how to use the color sensor on RVR (located on the down side of RVR, facing the floor)
        to report colors detected. To exit program, press <CTRL-C>
    """

    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)

    await rvr.enable_color_detection(is_enabled=True)
    await rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.color_detection,
        handler=color_detected_handler
    )
    await rvr.sensor_control.start(interval=250)
    test_function()

    while True:
        await asyncio.sleep(1)
async def test_function():
    color_detected_data = await rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.color_detection,
            handler=color_detected_handler)
    result = color_detected_handler(color_detected_data)
    print(result)

if __name__ == '__color_detected_main__':
    try:
        
        asyncio.ensure_future(
            color_main()
        )
        loop.run_forever()
        print(color_detected_data)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            asyncio.gather(
                rvr.enable_color_detection(is_enabled=False),
                rvr.close()
            )
        )

    finally:
        if loop.is_running():
            loop.close()

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal

import asyncio

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

async def main():
    await rvr.wake()
    await rvr.drive_with_heading(30,0,2)

try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
except:
    print("error")
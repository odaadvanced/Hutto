from gpiozero import LED
import time
from signal import pause
def speed():
    speed = random.randint(0, 30)
    rvr.drive_with_heading(
        speed,
        heading = 0,
        flags = DriveFlagsBitmask.none.value)

    while speed > 20:
        # From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

        red_led1 = LED(18)
        red_led2 = LED(23)

        # The first number in blink() is the on time and the second is the off time (both in seconds)
        red_led1.blink(0.5, 0.5)
        time.sleep(0.5)
        red_led2.blink(0.5, 0.5)

        pause()

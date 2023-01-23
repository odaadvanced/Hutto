import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

rvr = SpheroRvrObserver()

def main():
    """ This progran demonstrates how to set all the LEDs
of RVR using the LED control helper.
    """
    try:
        rvr.wake()
        
        # Give RVR time to wake up
        time.sleep(2)
        
        rvr.led_control.turn_leds_off()
        
        # Delay to show LEDs change
        time.sleep(2)
        
        rvr.led_control.set_all_leds_color(color=Colors.yellow)
        
        #Delay to show LEDs change
        
        time.sleep(10)
        
    
        rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)
        
        time.sleep(10)
        
        rvr.led_control.turn_leds_off()
    except KeyboardInterrupt:
        
        print('\nProgram terminated with keyboard interrupt.')
    
    finally:
        
        rvr.close()
        
if __name__ == '__main__':
    main()


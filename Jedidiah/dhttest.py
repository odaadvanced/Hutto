import RPi.GPIO as GPIO
import dht11python as dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #Broadcom mode
GPIO.cleanup()
# read data using pin 14
def check_temp_and_humidity():
    instance = dht11.DHT11(pin = 16)
    result = instance.read()

    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    
    time.sleep(.05)
    
   # time.sleep(4)
#    else:
#        print("Error: %d" % result.error_code)
        
 #   time.sleep(2)

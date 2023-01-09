from PiAnalog import *
from gpiozero import DigitalOutputDevice, LED, Button
from oled_io import Oled_io
import time

red_led = LED(18)
green_led = LED(23)
yellow_led = LED(24)
switch = Button(25)

pin1 = DigitalOutputDevice(16)
pin2 = DigitalOutputDevice(20)
p = PiAnalog()
display = Oled_io()
check_button_pressed = 0

def button_pressed():
   if switch.is_pressed:
    return 1

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for j in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass
    
while True:
    if button_pressed() !=1:
        red_led.on()
        display.print("DO NOT CROSS")
    if button_pressed() == 1:
        for j in range(0,16):
            display.print(str(15-j))
            buzz(2000, 0.5)
            time.sleep(0.5)
        red_led.off()
        green_led.on()
        display.print("MAY CROSS")
        time.sleep(1)
        for k in range(0,16):
            display.print(str(15-k))
            time.sleep(1)
        green_led.off()
        yellow_led.on()
        display.print("DO NOT CROSS")
        time.sleep(1)
        for l in range(0,4):
            display.print(str(3-l))
            time.sleep(1)       
        yellow_led.off()  
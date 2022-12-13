from PiAnalog import *
from gpiozero import DigitalOutputDevice, LED, Button
from oled_io import Oled_io
import time

red_led = LED(18)
green_led = LED(23)
yellow_led = LED(24)
switch = Button(25)

p1 = DigitalOutputDevice(16)
p2 = DigitalOutputDevice(20)
p = PiAnalog()
display = Oled_io()
check_button_pressed = 0

def button_pressed():
   switch.is_pressed
   check_button_pressed = global check_button_pressed + 1

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

def display_time_remaining_and_buzz():
    for i in range(0,16):
        display.print(15-i)
        buzz(1000, 0.5)
        break

while True:
    while not button_pressed:
       red_led.on()
       display.print("DO NOT CROSS")
    if global check_button_pressed = 1:
        display.print(display_time_remaining_and_buzz)
        red_led.off()
        green_led.on()
        display.print("MAY CROSS")
        for k in range(0,16):
            display.print(15-k)
        green_led.off()
        yellow_led.on()
        for l in range(0,4):
            display.print(4-k)
        display.print("DO NOT CROSS")
        yellow_led.off()
        red_led.on()
        check_button_pressed = 0
        
    
    

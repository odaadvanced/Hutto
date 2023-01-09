from PiAnalog import *
from gpiozero import DigitalOutputDevice, LED, Button
from oled_io import Oled_io
import board, time, gpiozero

red_led = gpiozero.LED(18)
green_led = gpiozero.LED(23)
yellow_led = gpiozero.LED(24)
switch = gpiozero.Button(25, pull_up=True)
show_colon = True

display = Oled_io()

def button_pressed():
    switch.is_pressed

p1 = DigitalOutputDevice(16)
p2 = DigitalOutputDevice(20)
p = PiAnalog()
display = Oled_io()

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0,cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.off()
        delay(p2)
def countdown():
    for i in range(0,16):
        global show_colon
        current_seconds = now.strftime("  %S")
        display.print(current_seconds)
        time.sleep(0.5)
        #display.print(16-i)
        #buzz(1000, 1)
        #time.sleep(15)
while True:
    while button_pressed != 1:
        red_led.on()
        display.print("DO NOT CROSS")
    if switch.is_pressed == 1:
        display_countdown()
        red_led.off()
        green_led.on()
        display.print("MAY CROSS")
        green_led.off()
        yellow_led.on()
        for j in range(0,4):
            display.print("DO NOT CROSS")
            time.sleep(1)
        yellow_led.off()
        red_led.on()
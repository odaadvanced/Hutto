from PiAnalog import *
from gpiozero import DigitalOutputDevice, LED, Button
from oled_io import Oled_io
import board, gpiozero

red_led = gpiozero.LED(24)
green_led = gpiozero.LED(23)
yellow_led = gpiozero.LED(18)
switch = gpiozero.Button(25, pull_up=True)
show_colon = True

display = Oled_io()

def button_pressed():
    if switch.is_pressed:
        return 1

pin1 = DigitalOutputDevice(16)
pin2 = DigitalOutputDevice(20)
p = PiAnalog()
display = Oled_io()

def buzz(pitch, duration):
    period = .8 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0,cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.off()
        delay(p2)

def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass

def message1a():
    return("DO NOT")

def message1b():
    return("CROSS")
    time.sleep(0.8)

def message1c():
    return("MAY")
    time.sleep(0.8)

while True:
    if button_pressed() != 1:
        red_led.on()
        display.print(str(message1a()))
        time.sleep(0.8)
        display.print(str(message1b()))
        time.sleep(0.8)
    else:
        for a in range (0,16):
            a = 15-a
            buzz(1000, 0.2)
            display.print(str(a))
            time.sleep(0.8)
            a=a-1
        red_led.off()
        green_led.on()
        display.print(str(message1c()))
        time.sleep(0.8)
        display.print(str(message1b()))
        time.sleep(1)
        for a in range (0,16):
            a = 15-a
            display.print(str(a))
            time.sleep (1)
        green_led.off()
        yellow_led.on()
        for j in range(0,3):
            display.print(str(message1a()))
            time.sleep(0.5)
            display.print(str(message1b()))
            time.sleep(0.5)
        yellow_led.off()
        red_led.on()
# 11_02_fancy_clock.py

import time, gpiozero
from PiAnalog import *
from oled_io import Oled_io
from gpiozero import DigitalOutputDevice, LED
display = Oled_io()
switch = gpiozero.Button(19, pull_up=True)
show_colon = True
no_cross, countdown_mode, date_mode, slow_mode, sleeper = range(5)
disp_mode = no_cross

red_led = LED(22)
yellow_led = LED(20)
green_led = LED(17)

pin1 = DigitalOutputDevice(5)
pin2 = DigitalOutputDevice(6)
p = PiAnalog()

slowv = True

canpress = True

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

def delay(xp):
    t0 = time.time()
    while time.time() < t0 + xp:
        pass

def display_cross_f():
    yellow_led.off()
    mes = "DO NOT CROSS"
    red_led.on()
    canpress = True
    display.print(mes)

def countdown():
    global disp_mode
    canpress = False
    tim = 15
    while tim > 0:
        display.print(str(tim))
        buzz(450, 0.3)
        tim = tim - 1
        time.sleep(0.7)
    disp_mode = disp_mode + 1

def countdown2():
    global disp_mode
    canpress = False
    ti = 15
    while ti > 0:
        display.print(str(ti))
        buzz(450, 0.3)
        ti = ti - 1
        time.sleep(0.7)
    disp_mode = disp_mode + 1
        
        
def display_cross():
    red_led.off()
    green_led.on()
    mes2 = "May Cross"
    display.print(mes2)
    time.sleep(1)
    disp_mode = 5
    countdown2()

def display_slow():
    green_led.off()
    yellow_led.on()
    mes3 = "DO NOT CROSS"
    display.print(mes3)
    time.sleep(3)
    display_cross_f()
    disp_mode = no_cross

while True:
    if switch.is_pressed:
        if canpress == True:
            disp_mode = 2
    if disp_mode == no_cross:
        display_cross_f()
    elif disp_mode == countdown_mode:
        countdown()
    elif disp_mode == date_mode:
        display_cross()
    elif disp_mode == slow_mode:
        display_slow()
        disp_mode = 5
    elif disp_mode == sleeper:
        a = 1

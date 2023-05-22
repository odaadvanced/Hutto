# 03_rgb.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import RGBLED
#from guizero import App, Slider, Text
from colorzero import Color

rgb_led = RGBLED(5, 6, 17)

red = 0
green = 0
blue = 0

def color_changed(value1, value2, value3):
    global red
    global green
    global blue
    red = int(value1)
    green = int(value2)
    blue = int(value3)
    rgb_led.color = Color(red, green, blue)
    
def red_changed(value):
    global red
    red = int(value)
    rgb_led.color = Color(red, green, blue)

def green_changed(value):
    global green
    green = int(value)
    rgb_led.color = Color(red, green, blue)

def blue_changed(value):
    global blue
    blue = int(value)
    rgb_led.color = Color(red, green, blue)

# app = App(title='RGB LED', width=500, height=400, layout="grid")
# 
# Text(app, text="Red", grid=[0, 0])
# Slider(app, command=red_changed, end=255, width=400, height=50, grid=[1, 0]).text_size = 30
# Text(app, text="Green", grid=[0, 1])
# Slider(app, command=green_changed, end=255, width=400, height=50, grid=[1, 1]).text_size = 30
# Text(app, text="Blue", grid=[0, 2])
# Slider(app, command=blue_changed, end=255, width=400, height=50, grid=[1, 2]).text_size = 30
# 
# app.display()

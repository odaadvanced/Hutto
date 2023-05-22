from gpiozero import RGBLED
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
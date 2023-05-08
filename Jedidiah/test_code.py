#test code
import random
from oled_io import Oled_io
display = Oled_io()
def add():
    number = random.randint(1,5)
    return number

#display.print(add())
sum = add() + 3
print(sum)
print(type(add()))
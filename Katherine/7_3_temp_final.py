#07_02_temp_gui.py

from guizero import *

class ScaleConverter:
	
	def __init__(self, units_from, units_to, factor):
		self.units_from = units_from
		self.units_to = units_to
		self.factor = factor
	
	def description(self):
		return 'Convert ' + self.units_from + ' to ' + self.units_to

	def convert(self, value):
		return value * self.factor
class ScaleAndOffsetConverter(ScaleConverter):
	
	def __init__(self, units_from, units_to, factor, offset):
		ScaleConverter.__init__(self, units_from, units_to, factor)
		self.offset = offset
		
	def convert(self, value):
		return value * self.factor + self.offset

c_to_f_conv = ScaleAndOffsetConverter('C', 'F', 1.8, 32)

def convert ():
    c = float(degCfield.value)
    degFfield.value = str(c_to_f_conv.convert(c))

app = App(title="Temp Converter", layout="grid", width=300, height=100)
Text(app, text="degrees C", grid=[0,0])
degCfield = TextBox(app, grid=[1,0], width="fill")

Text(app, text="degrees F", grid=[0,1])
degFfield = Text(app, grid=[1,1])

button = PushButton(app, text="Convert", grid=[0,2], command=convert)

app.display()
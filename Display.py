#!/usr/bin/python


import time
import Adafruit
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate


class Display():

	def __init__(self):
		self.lcd = Adafruit_CharLCDPlate(busnum=1)

	def clear(self):
		self.lcd.clear()

	def start(self):
		self.lcd.begin(16, 2)
		self.lcd.backlight(self.lcd.ON)

	def stop(self):
		self.clear()
		self.lcd.backlight(self.lcd.OFF)

	def message(self, message=""):
		self.start()
		self.lcd.message(message)

	def button_pressed(self, button=None):
		if self.lcd.buttonPressed(button):
			time.sleep(.2)
			return(True)
		else:
			return(False)

	def button_left(self):
		return(self.button_pressed(self.lcd.LEFT))

	def button_right(self):
		return(self.button_pressed(self.lcd.RIGHT))

	def button_up(self):
		return(self.button_pressed(self.lcd.UP))

	def button_down(self):
		return(self.button_pressed(self.lcd.DOWN))

	def button_select(self):
		return(self.button_pressed(self.lcd.SELECT))

	def blink_cursor(self):
		self.lcd.blink()

	def move_cursor(self, col=0, row=0):
		self.lcd.setCursor(col, row)
	

# basic tests
if __name__ == '__main__':
	display = Display()

	display.start()
	time.sleep(1)

	display.stop()
	time.sleep(1)

	display.message("This is a test.")
	time.sleep(1)

	display.clear()
	time.sleep(1)

	display.stop()
	time.sleep(1)


#!/usr/bin/python


import signal
import time
import os
import Adafruit
import Input
from Display import Display
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate


def exit_handler (signum, frame):
	display = Display()
	display.stop()
	exit(0)

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGQUIT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)


display = Display()
timefmt = "%Y/%m/%d\n%H:%M:%S"

old_t = int(time.time())

display.message(time.strftime(timefmt))

while True:
	if display.button_select():
		if Input.yesno(prompt = "Exit?" , value = "no"):
			display.stop()
			exit(0)

		if Input.yesno(prompt = "Reboot?" , value = "no"):
			display.message("Rebooting...")
			os.system("/sbin/shutdown -r now")
			time.sleep(300)
			exit(0)

		if Input.yesno(prompt = "Shutdown?" , value = "no"):
			display.message("Shutting down...")
			os.system("/sbin/shutdown -h -P now")
			time.sleep(300)
			exit(0)

	t = int(time.time())

	if t == old_t:
		time.sleep(.1)
		continue

	old_t = t

	display.message(time.strftime(timefmt))


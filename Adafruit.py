#!/usr/bin/python

import os
if os.geteuid() != 0:
	raise RuntimeError("This script must be run as root. Try sudo.")

import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")

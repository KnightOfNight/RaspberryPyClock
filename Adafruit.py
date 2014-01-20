#!/usr/bin/python

# Make sure this script is run as root. Root is required to access the
# hardware, e.g. the 16x2 LCD display. This should not be changed unless the
# permissions issues are addressed at the OS level.
import os
if os.geteuid() != 0:
	raise RuntimeError("This script must be run as root. Try sudo.")

# Update the include path with the location of the Adafruit libraries. This can
# be changed as needed.
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")

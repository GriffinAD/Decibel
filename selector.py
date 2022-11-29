import time
#from machine import ADC,Pin
from statistics import mean
from array import array
from collections import deque 

import random

class ADC:
	def __init__(self, pin):
		self.pin = pin
	def read(self):
		#return random.uniform(24.0, 101.9)
		return random.uniform(90.0, 532)

class Pin:
	def read(self):
		return


rounding = 0

soundSensorPin = ADC(26)  # this pin read the analog voltage from the sound level meter
vREF = 5.0  # voltage on AREF pin,default:operating voltage
offset = 0  # offset value for calibration


def displayStats():

    print (stats)

# initialize stats
stats = decibelStats()

# main loop
while True:
	decibel = readDecibel()

	processStats(decibel)

	displayStats()

	#print (f"{decibel} db")

import random
import time
from array import array
from collections import deque

# from machine import ADC,Pin
from statistics import mean


class ADC:
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        # return random.uniform(24.0, 101.9)
        return random.uniform(90.0, 532)


class Pin:
    def read(self):
        return


rounding = 0

soundSensorPin = ADC(26)  # this pin read the analog voltage from the sound level meter
vREF = 5.0  # voltage on AREF pin,default:operating voltage
offset = 0  # offset value for calibration
stats = None

class decibelStats:
    def __init__(self):
        self.__storage = deque([], maxlen=25)
        self.__min = 0
        self.__max = 0

    def __str__(self):
        return f"db:{self.decibel} sampleMin:{self.sampleMin()}  sampleMax:{self.sampleMax()}  min:{self.overallMin()}  max:{self.overallMax()}. avg:{self.avg()}"

    def setDecibel(self, decibel):
        self.decibel = decibel

        if self.__min == 0 or self.__min >= decibel:
            self.__min = decibel

        if self.__max == 0 or self.__max <= decibel:
            self.__max = decibel

        self.__storage.appendleft(decibel)

    def overallMin(self):
        return self.__min

    def overallMax(self):
        return self.__max

    def sampleMin(self):
        return round(min(self.__storage), rounding)

    def sampleMax(self):
        return round(max(self.__storage), rounding)

    def avg(self):
        return round(mean(self.__storage), rounding)


def readDecibel():

    readings = []

    # get 10 samples
    for i in range(5):
        # read value from sensor
        voltageValue = soundSensorPin.read() / 1024 * vREF
        decibelValue = voltageValue * 50

        # read value into array
        readings.append(decibelValue + offset)

    # calculate averge
    decibel = round(mean(readings), rounding)

    # time.sleep(0.1)

    return decibel


def processStats(decibel):
    stats.setDecibel(decibel)


def displayStats():
    print(stats)


def run():

    # initialize stats
    global stats
    if stats is None:
        stats = decibelStats()

    if stats is None:
        stats = decibelStats()

    # main loop
    while True:
        decibel = readDecibel()

        processStats(decibel)

        displayStats()

        # print (f"{decibel} db")

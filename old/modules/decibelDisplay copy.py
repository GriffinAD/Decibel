import random
import time
from array import array
from collections import deque

# from machine import ADC,Pin
from statistics import mean

if __name__ != "__main__":
    from modules import commonLib as common
else:
    import commonLib as common

class Decibel:
    
    def __init__(self):
        self.rounding = 0
        self.soundSensorPin = self.ADC(26)  # this pin read the analog voltage from the sound level meter
        self.vREF = 5.0  # voltage on AREF pin,default:operating voltage
        self.offset = 0  # offset value for calibration
        self.stats = None

      
    class ADC:
        def __init__(self, pin):
            self.pin = pin

        def read(self):
            return random.uniform(90.0, 532)


    class Pin:
        def __init__(self, pin):
            self.pin = pin
            
        def read(self):
            return

    class DecibelStats:
        stats = None
        def __init__(self):
            self.__storage = deque([], maxlen=25)
            self.__min = 0
            self.__max = 0
        def __str__(self):
            return f"db:{self.dec} sampleMin:{self.sampleMin()}  sampleMax:{self.sampleMax()}  min:{self.overallMin()}  max:{self.overallMax()}. avg:{self.avg()}"

        def setDecibel(self, dec):
            self.dec = dec

            if self.__min == 0 or self.__min >= dec:
                self.__min = dec

            if self.__max == 0 or self.__max <= dec:
                self.__max = dec

            self.__storage.appendleft(dec)

        def overallMin(self):
            return self.__min

        def overallMax(self):
            return self.__max

        def sampleMin(self):
            return round(min(self.__storage), Decibel.rounding)

        def sampleMax(self):
            return round(max(self.__storage), Decibel.rounding)

        def avg(self):
            return round(mean(self.__storage), Decibel.rounding)


    def readDecibel(self):

        readings = []

        # get 10 samples
        for i in range(5):
            # read value from sensor
            voltageValue = self.soundSensorPin.read() / 1024 * self.vREF
            decibelValue = voltageValue * 50

            # read value into array
            readings.append(decibelValue + self.offset)

        # calculate averge
        decibel = round(mean(readings), self.rounding)

        # time.sleep(0.1)

        return decibel


    def processStats(self, decibel):
        stats.setDecibel(decibel)


    def displayStats(self):
        common.display(self.stats)

    def init(self):
        stats = self.DecibelStats()

    def run(self):

        # initialize stats
        stats = self.DecibelStats()

        # main loop
        while True:
            decibel = self.readDecibel()

            self.processStats(decibel)

            self.displayStats()

            # print (f"{decibel} db")
if __name__ == "__main__":
    dec = Decibel()
    dec.run()
    
#from array import array
#from ulab import numpy as np
import math

#from analogio import AnalogIn
#import board
import asyncio
from deque import deque
from samplestats import SampleStats


if __name__ != "__main__":
    from modules import commonLib as common
else:
    #import commonLib as common
    print ()
 

class ADC:
        def __init__(self, pin, VREF: float = 5.0):
            self.pin = pin
            #self.analog_in = AnalogIn(pin)
            self.VREF=VREF

        def read(self):
            #raw=self.analog_in.value
            raw= 23357
            return raw


class Pin:
    def __init__(self, pin):
        self.pin = pin
        
    def read(self):
        return

   
class SensorStats:
    #rounding = 0
    #stats = 0
    def __init__(self, rounding:int = 0,
    calibrationOffset: int = 0, 
    sampleWindow: int = 0, 
    soundSensorPin: ADC = ADC(1,5.0)):
        self.rounding = rounding
        self.soundSensorPin = soundSensorPin  # this pin reads the analog voltage from the sound level meter
        self.calibrationOffset = calibrationOffset  # offset value for calibration
        self.sampleWindow = sampleWindow
        arr = deque([], self.sampleWindow)
        self.stats = SampleStats(arr)


    def ReadDecibel(self):
    
        voltageValue = self.soundSensorPin.read() 
            #decibelValue = (voltageValue / 1024 * self.vREF) * 50
        decibelValue=((voltageValue / 1024.0) * 2.0) + 10.0
        self.stats.setDecibel(decibelValue)
        
        #decibel = round(decibelValue, self.rounding)

        return decibelValue


    def ProcessStats(self,decibel):
        self.stats.setDecibel(decibel)  # type: ignore


    def DisplayStats(self):
        #decibelDisplay.ShowDecibel(self.avg())
        x=getattr(self.stats,"overallMin")()
        print(x)

    def Init(self):
        self.stats = self.DecibelStats(self)

    async def run(self):

        # initialize stats
        #self.stats = self.DecibelStats(self,[])

        # main loop
        while True:
            decibel = self.ReadDecibel()

            self.ProcessStats(decibel)

            self.DisplayStats()
            
            # so we can cancel
            await asyncio.sleep(0.0)
            
            # print (f"{decibel} db")
            
            
            
if __name__ == "__main__":

    async def main():
        dec = Decibel()
        task = asyncio.create_task(dec.run())

        await asyncio.sleep(3)

        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("main(): cancel_me is cancelled now")

    asyncio.run(main())
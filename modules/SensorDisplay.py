import asyncio
from Deque import Deque
from SampleStats import SampleStats
from SensorStats import SensorStats
from HW import ADC
from modules.Display import Display
from HW import KeyInput

sensor = ADC(pin = board.A2, VREF = 5.0)
pages = ("avg", "min", "max", "datetime")

class SensorDisplay:
    def __init__(self, stats):
        
        self.stats = SensorStats(
            rounding = -1,
            calibrationOffset= 0,
            sampleWindow = 100,
            sensor = sensor)

        self.display = Display()
    
        self.keys = KeyInput()
    
        self.func = pages[0]
        
        self.page = 0
        
    
    async def run(self):

        # initialize stats
        # self.stats = self.DecibelStats(self,[])

        # main loop
        while True:
            decibel = self.stats.readValue()

            self.stats.processStats(decibel)

            await asyncio.sleep(0.0)

            # print (f"{decibel} db")

            
    async def displayValue(self):
        
        while True:
            value = self.stats.calcStats(self.func)
            color = self.processColor(value)
            
            await asyncio.sleep(0.0)
        
    
    async def checkKeys(self):
        while True:
            key = self.keys.getKeyValue()
            
            print (key)
            
            self.page = (self.page + 1) % 3
            func=pages[self.page]
            
            await asyncio.sleep(0.0)
            

    def processColor(self, db):
        dbcolor = 0x00ff00  # default value
        
        if db <= 50:
            dbcolor= 0x12ff00
        elif db <= 60:
            dbcolor=0x48ff00
        elif db <= 70:
            dbcolor=0xb6ff00
        elif db <= 80:
            dbcolor=0xff6d00
        elif db <= 90:
            dbcolor=0xff3600
        elif db <= 100:
            dbcolor=0xff1200
        elif db <= 110:
            dbcolor=0xff0000
        elif db > 110:
            dbcolor=0xff006d
            
        return dbcolor


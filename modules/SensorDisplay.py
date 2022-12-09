import asyncio
from Deque import Deque
from SampleStats import SampleStats
from SensorStats import SensorStats
from HW import ADC
from Display import Display
from HW import KeyInput
from DispalyPages import DisplayPages
import displayio

#sensor = ADC(pin = board.A2, VREF = 5.0)
sensor = ADC(pin = 1, VREF = 5.0)

pages = ("avg", "overallMin", "overallMax", "datetime")

class SensorDisplay:
    def __init__(self, stats):
        
        self.stats = SensorStats(
            rounding = -1,
            calibrationOffset= 0,
            sampleWindow = 100,
            sensor = sensor)

        self.display = Display()
        
        self.displayPages = DisplayPages()
    
        self.keys = KeyInput()
    
        self.func = pages[0]
        
        self.page = 0
        
    
    async def getStats(self):

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
            
            #self.displayPages.dbPage().lin [].line1.Text= value
            
            line1 = Group(2)
            
            
            await asyncio.sleep(0.0)
            
            print (value)
        
    
    async def checkKeys(self):
        while True:
            key = self.keys.getKeyValue()
            
            print (key)
            
            self.page = (self.page + 1) % 3
            self.func = pages[self.page]
            
            displayio.Group().append(self.displayPages.dbPage())
            
            
            print (self.func)
            
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


    async def start(self):
        # Create a "cancel_me" Task
        
        # run all async
        task = asyncio.gather(
            asyncio.create_task(self.getStats()), # get a value
            asyncio.create_task(self.displayValue()), # update display
            asyncio.create_task(self.checkKeys()) # process key press
        )

        # Wait for 1 second
        await asyncio.sleep(3)

        task.cancel()
        try:
            await (task)
        except asyncio.CancelledError:
            print("main(): cancel_me is cancelled now")
            
s = SensorDisplay([])            
asyncio.run(s.start())
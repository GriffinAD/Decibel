import asyncio
import datetime
from Deque import Deque
from SampleStats import SampleStats
from SensorStats import SensorStats
from HW import ADC
from Display import Display
from HW import KeyInput
from DispalyPages import DisplayPages
import displayio
from adafruit_display_text import label
import datetime
from displayio import Group

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
        
        self.selectedMenu = 0
    
        self.groups=displayio.Group()
        self.groups.append(self.displayPages.initPage())
        self.groups.append(self.displayPages.dbPage())
        self.groups.append(self.displayPages.dateTimePage())
        
        self.currentGroup = self.groups[self.selectedMenu]
        
    
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
            
            g = self.groups
            
            if 0 <= self.selectedMenu <= 4:                    
                value = self.stats.calcStats(self.func)
                color = self.processColor(value)
            
                label1:label.Label = g[1].__getitem__(0) 
                label2:label.Label = g[1].__getitem__(1) 
                label3:label.Label = g[1].__getitem__(2) 
                label1.text = "value"
                label2.color = color
                if self.page>0:
                    label3.text = pages[self.page][:2]

                label3.text=""
        
            elif self.selectedMenu == 5:
                label1:label.Label = g[2].__getitem__(0) 
                label2:label.Label = g[2].__getitem__(1) 
                label3:label.Label = g[2].__getitem__(2) 
                
                days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday" )

                # t = tc.datetime  
                # date =  "%04d" % t.tm_year + '-' + "%02d" % t.tm_mon + '-' + "%02d" % t.tm_mday
                # dayOfTime = "%02d" % t.tm_hour + ':' + "%02d" % t.tm_min + ':' + "%02d" % t.tm_sec
                
                t = datetime.datetime.now() #rtc.datetime  
                date =  "%04d" % t.year + '-' + "%02d" % t.month + '-' + "%02d" % t.day
                dayOfTime = "%02d" % t.hour + ':' + "%02d" % t.minute + ':' + "%02d" % t.second
                label1.text = date
                label2.text = dayOfTime
                label3.text = str(t.weekday)
                
            self.display.display.show(self.currentGroup)    
            
            await asyncio.sleep(0.0)
            
        
    
    async def checkKeys(self):
        while True:
            key = self.keys.getKeyValue()
            
            print (key)
            
            self.page = (self.page + 1) % 3
            self.func = pages[self.page]
            
            self.currentGroup=self.groups[]
            #displayio.Group().append(self.displayPages.dbPage())
            
            
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
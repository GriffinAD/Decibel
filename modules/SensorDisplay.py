import asyncio
from Deque import Deque
from SampleStats import SampleStats
from HW import ADC

sensor = ADC(pin = board.A2, VREF = 5.0)

class SensorDisplay:
    def __init__(
        self.stats = SensorStats(
            rounding = -1,
            calibrationOffset= 0,
            sampleWindow = 100,
            sensor = sensor)

      self.display = Display()

      def getValue(self):
            value = self.DisplayStats("avg")
            
      
      async def run(self):

        # initialize stats
        # self.stats = self.DecibelStats(self,[])

        # main loop
        while True:
            decibel = self.stats.readValue()

            self.ProcessStats(decibel)

            #self.DisplayStats()

            # so we can cancel
            await asyncio.sleep(0.0)

            # print (f"{decibel} db")

            
        async def display(self, func):
            value = self.calcStats(func)
            color = ProcessColor()
            
            
     
     
     
    def ProcessColor(db):
        if db <= 40:
            dcolor=0x00ff00
        elif db <= 50:
            dcolor= 0x12ff00
        elif db <= 60:
            dcolor=0x48ff00
        elif db <= 70:
            dcolor=0xb6ff00
        elif db <= 80:
            dcolor=0xff6d00
        elif db <= 90:
            dcolor=0xff3600
        elif db <= 100:
            dcolor=0xff1200
        elif db <= 110:
            dcolor=0xff0000
        elif db > 110:
            dcolor=0xff006d
            
       return dcolor


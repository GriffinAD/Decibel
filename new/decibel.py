from array import array
from ulab.numpy import mean

from analogio import AnalogIn
import board

class decibel:

    analog_in = AnalogIn(board.A2)
    db=None
    VREF=3.3
    dcolor=None
    
    def ProcessColor(self,db):
        dcolor=0x00ff00
        
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


# while True:

#     reading=0

#     m=[]
#     for x in range(10):

#         raw=analog_in.value
#         volt=round((raw / 1024.0) * 2) + 10
#         m.append(volt)

#     #decibel = reading/5
#     decibel = round(mean(m))

#     if db > 125:
#         v=-1
#         time.sleep(0.5)

#     if db < 20:
#         v=1
#         time.sleep(0.5)

#     #time.sleep(0.50)

#     line2.color=ProcessColor(decibel)

#     line1.text = f"{decibel}"
#     line2.text = "dB"

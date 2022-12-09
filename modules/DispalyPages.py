import config
import sys

try:
    from adafruit_bitmap_font import bitmap_font
    from adafruit_display_text import label
    from adafruit_display_text import scrolling_label
    import board
    import displayio
    import framebufferio
    import rgbmatrix
    import terminalio
    import time
    import displaySubsystem
    import keyInput
    from dirver_buzzer import *
    from dirver_lightSensor import *
except NotImplementedError or ImportError or ModuleNotFoundError:
    if not config.Test:
        print("This script can only be run in blabla environment")
        sys.exit(1)
    else:
        print("Test mode...")



fontLarge = "/lib/fonts/Tahoma-bold-32.bdf"
fontMedium = "/lib/fonts/Tahoma-bold-16.bdf"
fontSmall = "/lib/fonts/Tahoma-bold-12.bdf"

FONTlarge = bitmap_font.load_font(fontLarge)
FONTmedium = bitmap_font.load_font(fontMedium)
FONTsmall = bitmap_font.load_font(fontSmall)

        
        
class DisplayPages():

    def __init__(self):
        self.ok=True
        

    def initPage(self):
    
        g = displayio.Group()
        
        line1 = label.Label(FONTmedium, color=0x440000)

        line1.x = 1
        line1.y = 15
        
        g.append(line1)
        
        line1.text="......"
        
        g.hidden = False
        
        return g


    def dbPage(self):
    
        g = displayio.Group()
        
        line1 = label.Label(FONTlarge, color=0x440000)
        line2 = label.Label(FONTsmall, color=0x000044)
        line3 = label.Label(FONTsmall, color=0x000044)

        line1.x = 1
        line1.y = 15
    
        line2.x = 1
        line2.y = 26
        
        line3.x = 1
        line3.y = 5
        
        g.append(line1)
        g.append(line2)
        g.append(line3)
        
        g.hidden = True 
        
        return g
        
        
    def dateTimePage(self,line1,line2,line3):
    
        g = displayio.Group()
          
        line1 = label.Label(FONTlarge, color=0x440000, scale=1)
        line2 = label.Label(FONTsmall, color=0x000044, scale=1)
        line3 = label.Label(FONTsmall, color=0x000044, scale=1)
        
        line1.x = 3
        line1.y = 36
        line2.x = 8
        line2.y = 46
        line3.x = 10
        line3.y = 56
        
        g.append(line1)
        g.append(line2)
        g.append(line3)
        
        g.hidden = True 
        
        return g
        
        

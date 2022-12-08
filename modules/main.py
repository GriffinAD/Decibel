
pages = ("avg", "min", "max", "datetime")



def keyProcessing(keyValue):
    global keyMenuValue, keyDownValue, keyUpValue, beepCount, startBeepFlag
    if keyValue == KEY_MENU:
        keyMenuValue += 1
    if keyValue == KEY_DOWN:
        keyUpValue -= 1
    if keyValue == KEY_UP:
        keyUpValue += 1


while True:
    key_value = keyInput.getKeyValue()
    keyProcessing(key_value)
    
    if keyUpValue < len(groups):
        g = displayio.groups[1]
        
    else:
        g = displayio.groups[2]
    
    if keyUpValue > len(groups):
        keyUpValue = 0
        g = displayio.groups[1]
        
 

     
        
    
    if pageID == 0:
        showSystem.showDateTimePage(line1, line2, line3)
    if pageID == 1:
        line3.text = ""
        showSystem.showSetListPage(line1, line2, selectSettingOptions)
    if pageID == 2 and selectSettingOptions == 0:
        line1.text = ""
        showSystem.timeSettingPage(line2, line3, timeSettingLabel, timeTemp)
        
        

def init:
    d = DisplyPages()
    
    displayio.groups.append(d.initPage))
    displayio.groups.append(d.dbPage())
    displayio.groups.append(d.dateTimePage())

    




fontLarge = "/lib/fonts/Tahoma-bold-32.bdf"
fontMedium = "/lib/fonts/Tahoma-bold-16.bdf"
fontSmall = "/lib/fonts/Tahoma-bold-12.bdf"

FONTlarge = bitmap_font.load_font(fontLarge)
FONTmedium = bitmap_font.load_font(fontMedium)
FONTsmall = bitmap_font.load_font(fontSmall)

        
        
class DisplayPages():

    def initPage:
    
        g = displayio.Group()
        
        line1 = label.Label(FONTmedium, color=0x440000)

        line1.x = 1
        line1.y = 15
        
        g.append(line1)
        
        line1.text="......"
        
        g.hidden = False
        
        return g


    def dbPage:
    
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
        
        


line1 = label.Label(FONTlarge, color=0x440000, scale=1)
line2 = label.Label(FONTlarge, color=0x000044, scale=1)

line1.x = 1
line1.y = 15 #46

line2.x = 1
line2.y = 26 #46


 
    

# Put each line of text into a Group, then show that group.
g = displayio.Group()
g.append(line1)
g.append(line2)
g.append(line3)
display.show(g)

keyInput.keyInit()

showSystem = displaySubsystem.DISPLAYSUBSYSTEM()




days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday" )


t = rtc.datetime  
        date =  "%04d" % t.tm_year + '-' + "%02d" % t.tm_mon + '-' + "%02d" % t.tm_mday
        dayOfTime = "%02d" % t.tm_hour + ':' + "%02d" % t.tm_min + ':' + "%02d" % t.tm_sec
        line1.text = date
        line2.text = dayOfTime
        line3.text=days[int(t.tm_wday)]



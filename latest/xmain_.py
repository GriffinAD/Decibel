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
from adafruit_bitmap_font import bitmap_font
import random

bit_depth_value = 3
base_width = 64
base_height = 32
chain_across = 1
tile_down = 1
serpentine_value = True

width_value = base_width * chain_across
height_value = base_height * tile_down


# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

# send register
R1 = DigitalInOut(board.GP2)
G1 = DigitalInOut(board.GP3)
B1 = DigitalInOut(board.GP4)
R2 = DigitalInOut(board.GP5)
G2 = DigitalInOut(board.GP8)
B2 = DigitalInOut(board.GP9)
CLK = DigitalInOut(board.GP11)
STB = DigitalInOut(board.GP12)
OE = DigitalInOut(board.GP13)

R1.direction = Direction.OUTPUT
G1.direction = Direction.OUTPUT
B1.direction = Direction.OUTPUT
R2.direction = Direction.OUTPUT
G2.direction = Direction.OUTPUT
B2.direction = Direction.OUTPUT
CLK.direction = Direction.OUTPUT
STB.direction = Direction.OUTPUT
OE.direction = Direction.OUTPUT

OE.value = True
STB.value = False
CLK.value = False

MaxLed = 64

c12 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

for l in range(0, MaxLed):
    y = l % 16
    R1.value = False
    G1.value = False
    B1.value = False
    R2.value = False
    G2.value = False
    B2.value = False

    if c12[y] == 1:
        R1.value = True
        G1.value = True
        B1.value = True
        R2.value = True
        G2.value = True
        B2.value = True
    if l > (MaxLed - 12):
        STB.value = True
    else:
        STB.value = False
    CLK.value = True
    # time.sleep(0.000002)
    CLK.value = False
STB.value = False
CLK.value = False

for l in range(0, MaxLed):
    y = l % 16
    R1.value = False
    G1.value = False
    B1.value = False
    R2.value = False
    G2.value = False
    B2.value = False

for l in range(0, MaxLed):
    y = l % 16
    R1.value = False
    G1.value = False
    B1.value = False
    R2.value = False
    G2.value = False
    B2.value = False

    if c12[y] == 1:
        R1.value = True
        G1.value = True
        B1.value = True
        R2.value = True
        G2.value = True
        B2.value = True
    if l > (MaxLed - 12):
        STB.value = True
    else:
        STB.value = False
    CLK.value = True
    # time.sleep(0.000002)
    CLK.value = False
STB.value = False
CLK.value = False

for l in range(0, MaxLed):
    y = l % 16
    R1.value = False
    G1.value = False
    B1.value = False
    R2.value = False
    G2.value = False
    B2.value = False

    if c13[y] == 1:
        R1.value = True
        G1.value = True
        B1.value = True
        R2.value = True
        G2.value = True
        B2.value = True
    if l > (MaxLed - 13):
        STB.value = True
    else:
        STB.value = False
    CLK.value = True
    # time.sleep(0.000002)
    CLK.value = False
STB.value = False
CLK.value = False

R1.deinit()
G1.deinit()
B1.deinit()
R2.deinit()
G2.deinit()
B2.deinit()
CLK.deinit()
STB.deinit()
OE.deinit()

# This next call creates the RGB Matrix object itself. It has the given width
# and height. bit_depth can range from 1 to 6; higher numbers allow more color
# shades to be displayed, but increase memory usage and slow down your Python
# code. If you just want to show primary colors plus black and white, use 1.
# Otherwise, try 3, 4 and 5 to see which effect you like best.
#
# These lines are for the Feather M4 Express. If you're using a different board,
# check the guide to find the pins and wiring diagrams for your board.
# If you have a matrix with a different width or height, change that too.
# If you have a 16x32 display, try with just a single line of text.

matrix = rgbmatrix.RGBMatrix(
    width=width_value,
    height=height_value,
    bit_depth=bit_depth_value,
    rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],
    addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20],
    clock_pin=board.GP11,latch_pin=board.GP12,output_enable_pin=board.GP13,
    tile=tile_down,serpentine=serpentine_value,
    doublebuffer=True,
)


# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
display.rotation = 0
#display.brightness=0.6





# Testing getting back Quotes
#Real Time https://finnhub.io/docs/api#quote
#https://api.iextrading.com/1.0/tops/last?symbols=wso
#Demo link for testing wihtouth a key "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=Demo"
DATA_SOURCE = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=Demo"
DATA_Price = ["Global Quote", "05. price"]
DATA_VOL = ["Global Quote", "06. volume"]
DATA_CHG = ["Global Quote", "10. change percent"]
DATA_CO = ["Global Quote", "01. symbol"]


# the current working directory (where this file is)
#cwd = ("/" + __file__).rsplit("/", 1)[0]

#FONT = "/fonts/IBMPlexMono-Medium-24_jep.bdf"
#FONT2 = "/fonts/helvB12.bdf"
#FONT3 = "/fonts/helvR10.bdf"
#FONT4 = "/fonts/6x10.bdf"

fontLarge = "/lib/fonts/Tahoma-bold-32.bdf"
fontSmall = "/lib/fonts/Tahoma-bold-12.bdf"

FONTlarge = bitmap_font.load_font(fontLarge)
FONTsmall = bitmap_font.load_font(fontSmall)

_, height, _, dy = FONTlarge.get_bounding_box()

#print (height)

#line1 = label.Label(terminalio.FONT, color=0x00DD00, scale=2)
#line1 = scrolling_label.ScrollingLabel(font, text="hello world!          here we go....      ", color=0x00DD00, animate_time=0.2)

line1 = label.Label(FONTlarge, color=0x440000, scale=1)
line2 = label.Label(FONTsmall, color=0x002200, scale=1)
g = displayio.Group()
g.append(line1)
g.append(line2)


display.show(g)
display.brightness=0.6
print (f"Display:{display.brightness}")

#showSystem = displaySubsystem.DISPLAYSUBSYSTEM()

#display.minim


last_check = None

#line1.text = "148" # db .... here we go...."
#line2.text = "dB"

line1.x = 1
line1.y = 15 #46

line2.x=48
line2.y=25 #58

#line2.x=50
#line2.y=58

db=20
v=1

while True:
    #db=round(random.uniform(20.0, 140))

    #display.brightness=0.6

    if db > 145:
        v=-1
        time.sleep(0.5)

    if db < 20:
        v=1
        time.sleep(0.5)

    time.sleep(0.01)

    db += v

    if db <= 50:
        dcolor=0x004400
    elif db<60:
        dcolor=0x006600
    elif db<70:
        dcolor=0x446600
    elif db<80:
        dcolor=0x444400
    elif db<100:
        dcolor=0x440000
    elif db>100:
        dcolor=0x660000

    #print (dcolor)

    line1.color=dcolor

    #showSystem.showDateTimePage(line1, line2, line3)
    line1.text = f"{db}"
    line2.text = "dB"
    #time.sleep(0.01)
    #t = rtc.datetime
    #date =  "%04d" % t.tm_year + '-' + "%02d" % t.tm_mon + '-' + "%02d" % t.tm_mday
    #dayOfTime = "%02d" % t.tm_hour + ':' + "%02d" % t.tm_min + ':' + "%02d" % t.tm_sec
    #line1.update()

    #display.refresh()
    #display.refresh(minimum_frames_per_second=0)
    #display.refresh(minimum_frames_per_second=0)

    #if last_check is None or time.monotonic() > last_check + 340:
    #    try:
    #        value = matrixportal.fetch()
    #        print("Response is", value)
    #        last_check = time.monotonic()
    #    except (ValueError, RuntimeError) as e:
    #        print("Some error occured, retrying! -", e)
    #matrixportal.scroll()
    #time.sleep(.0155)

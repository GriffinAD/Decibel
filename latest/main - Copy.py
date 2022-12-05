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
from array import array
from ulab.numpy import mean

import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A2)

bit_depth_value = 4
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
# and height. bit_depth can range from 1 to 6

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


fontLarge = "/lib/fonts/Tahoma-bold-32.bdf"
fontSmall = "/lib/fonts/Tahoma-bold-12.bdf"

FONTlarge = bitmap_font.load_font(fontLarge)
FONTsmall = bitmap_font.load_font(fontSmall)

_, height, _, dy = FONTlarge.get_bounding_box()

line1 = label.Label(FONTlarge, color=0x00ff00, scale=1)
#line1.x = 1
#line1.y = 14 #46

centered=False

if centered:
    line1.anchor_point = (0.5, 0.5)
    line1.anchored_position = ((display.width // 2) - 2, display.height // 2)
else:
    line1.anchor_point = (0.0, 0.5)
    line1.anchored_position = (2, display.height // 2)


line2 = label.Label(FONTsmall, color=0x00ff00, scale=1)
line2.anchor_point = (0.0, 0.0)
line2.anchored_position = (47,20)
#line2.x=48 #48
#line2.y=26 #58


g = displayio.Group()
g.append(line1)
g.append(line2)

display.show(g)
#display.brightness=0.6
#print (f"Display:{display.brightness}")

db=20
v=1
VREF=3.3

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


while True:

    reading=0

    m=[]
    for x in range(100):

        raw=analog_in.value
        volt=round((raw / 1024.0) * 2) + 10
        m.append(volt)

    #decibel = reading/5
    decibel = round(mean(m))

    if db > 125:
        v=-1
        time.sleep(0.5)

    if db < 20:
        v=1
        time.sleep(0.5)

    time.sleep(0.25)

    line2.color=ProcessColor(decibel)

    line1.text = f"{decibel}"
    line2.text = "dB"


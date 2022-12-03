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
CLK.value = True

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
#display.rotation = 0
#display.brightness=0.6




fontLarge = "/lib/fonts/Tahoma-12.bdf"

FONTlarge = bitmap_font.load_font(fontLarge)

#line1 = label.Label(terminalio.FONT, color=0x00DD00, scale=2)
#line1 = scrolling_label.ScrollingLabel(font, text="hello world!          here we go....      ", color=0x00DD00, animate_time=0.2)

line1 = label.Label(FONTlarge, color=0x440000, scale=1)
line2 = label.Label(FONTlarge, color=0x000044, scale=1)

line1.x = 1
line1.y = 15 #46

line2.x = 1
line2.y = 26 #46

g = displayio.Group()
g.append(line1)
g.append(line2)

display.show(g)

#display.brightness=0.6
#print (f"Display:{display.brightness}")



v="hello"
#time.sleep(2)

while True:


    #v = v + "."
    line1.text=v
    line2.text=v
    #time.sleep(0.1)

    #display.refresh()
    #display.refresh(minimum_frames_per_second=0)
    #display.refresh(minimum_frames_per_second=0)

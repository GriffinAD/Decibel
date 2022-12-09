import config
import sys

try:
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


class Display:
    def __init__(self):
        
        self.bit_depth_value = 4
        self.base_width = 64
        self.base_height = 32
        self.chain_across = 1
        self.tile_down = 1
        self.serpentine_value = True

        self.width_value = self.base_width * self.chain_across
        self.height_value = self.base_height * self.tile_down


    def createDisplay(self):
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
            width=self.width_value,
            height=self.height_value,
            bit_depth=self.bit_depth_value,
            rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],  # type: ignore
            addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20],  # type: ignore
            clock_pin=board.GP11,latch_pin=board.GP12,output_enable_pin=board.GP13,  # type: ignore
            tile=self.tile_down,serpentine=self.serpentine_value,
            doublebuffer=True,
        )

        # Associate the RGB matrix with a Display so that we can use displayio features
        display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
        display.rotation = 0
        #display.brightness=0.6

        g = displayio.Group()
        display.show(g)

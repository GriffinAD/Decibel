import sys
import config

try:
    from analogio import AnalogIn
    import board
    import digitalio
except NotImplementedError or ImportError or ModuleNotFoundError:
    if not config.Test:
        print("This script can only be run in blabla environment")
        sys.exit(1)
    else:
        print("Test mode...")

import random


class ADC:
    """
    Anologue reader
        pin: board.A2
        VREF: voltage
    """

    def __init__(self, pin, VREF: float = 5.0):
        self.pin = pin
        if not config.Test:
            self.analog_in = AnalogIn(pin)
        self.VREF = VREF

    def read(self):
        if config.Test:
            raw = random.uniform(1, 20000)
        else:
            raw = self.analog_in.value
        return raw


class Pin:
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        return


class KeyInput:
    # The pins we'll use, each will have an internal pullup
    #keypress_pins = [board.GP15, board.GP19,board.GP21]
    keypress_pins = [1,2,3]
    # Our array of key objects
    key_pin_array = []
    # The Keycode sent for each button, will be paired with a control key

    def __init__(self):
        
        # Make all pin objects inputs with pullups
        for pin in self.keypress_pins:
            if not config.Test:
                key_pin = digitalio.DigitalInOut(pin)
                key_pin.direction = digitalio.Direction.INPUT
                key_pin.pull = digitalio.Pull.UP
                self.key_pin_array.append(key_pin)
    
    def getKeyValue(self):
        if config.Test:
            return 1
        # Check each pin
        for key_pin in self.key_pin_array:
            if not key_pin.value:  # Is it grounded?
                keyValue = self.key_pin_array.index(key_pin)
                return keyValue


import sys
import config

try:
    from analogio import AnalogIn
    import board
except ImportError or ModuleNotFoundError:
    if not config.Test:
        print('This script can only be run in blabla environment')
        sys.exit(1)
        
import random

class ADC:
        def __init__(self, pin, VREF: float = 5.0):
            self.pin = pin
            if not config.Test:
                  self.analog_in = AnalogIn(pin)
            self.VREF=VREF

        def read(self):
            if config.Test:
                raw = random.uniform(1,20000)
            else:
                raw = self.analog_in.value
            return raw


class Pin:
    def __init__(self, pin):
        self.pin = pin
        
    def read(self):
        return
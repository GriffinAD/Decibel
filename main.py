from time import sleep
from analogio import AnalogIn
from pwmio import PWMOut
import board
from math import log

fan = PWMOut(board.GP13, frequency=25000, duty_cycle=26214)
adc = AnalogIn(board.A2)


maxPercent = 100
minPercent = 40
minTemp = 25
maxTemp = 30

oldTemp = 0

# Thermistor specs: very generic
r25 = 10000  # nominal resistance at 25 °C, ohms
beta = 3950  # β (25/50 °C)

# potential divider resistor, on high side
r_high = 5600  # ohms

cal = -7


def setFanSpeed(percent):
    value = 65535
    if percent > 0:
        value = int(65535 / (100 / percent))
    fan.duty_cycle = value
    print(f"Fan Speed: {percent} ({value})")

    return value


def getTemperature():
    r = r_high / (65535 / float(adc.value) - 1)
    lnr = log(r / r25)
    ts_C = int((-273.15 + 1 / (1 / 298.15 + lnr / beta)) + cal)
    print(f"Temperature: {ts_C} C")
    return ts_C


def calcSpeed(temp):
    if temp < minTemp:
        spd = minPercent
    elif temp > maxTemp:
        spd = maxPercent
    else:
        tPerc = ((temp - minTemp)) / (maxTemp - minTemp)
        spd = ((maxPercent - minPercent) * tPerc) + minPercent
    # print(f"speed set: {spd} for temp: {temp} C")
    return spd


while True:
    temp = getTemperature()

    if oldTemp != temp:
        spd = calcSpeed(temp)
        setFanSpeed(spd)
        oldTemp = temp
    sleep(2)
# for temp in range (0,101):
# spd = calcSpeed(temp)

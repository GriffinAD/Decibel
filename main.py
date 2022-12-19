from math import log
from time import sleep

import board
from analogio import AnalogIn
from pwmio import PWMOut

fan = PWMOut(board.GP13, frequency=25000, duty_cycle=26214)
adc = AnalogIn(board.A2)


min_pwm_percent = 40
max_pwm_percent = 100
min_sensor_temp = 25
max_sensor_temp = 30

prevTemperature = 0

# Thermistor specs: very generic
r25 = 10000  # nominal resistance at 25 °C, ohms
beta = 3950  # β (25/50 °C)

# potential divider resistor, on high side
r_high = 5600  # ohms

cal = -7  # temperature offset


def SetFanSpeed(percent):
    value = 65535
    if percent > 0:
        value = int(65535 / (100 / percent))
    fan.duty_cycle = value
    print(f"Fan Speed: {percent} ({value})")

    return value


def GetTemperature():
    r = r_high / (65535 / float(adc.value) - 1)
    lnr = log(r / r25)
    ts_C = int((-273.15 + 1 / (1 / 298.15 + lnr / beta)) + cal)
    print(f"Temperature: {ts_C} C")
    return ts_C


def CalcSpeed(temperature):
    if temperature <= min_sensor_temp:
        speedVal = min_pwm_percent
    elif temperature >= max_sensor_temp:
        speedVal = max_pwm_percent
    else:
        tPercent = ((temperature - min_sensor_temp)) / (max_sensor_temp - min_sensor_temp)
        speedVal = ((max_pwm_percent - min_pwm_percent) * tPercent) + min_pwm_percent
    # print(f"speed set: {speedVal} for temp: {temperature} C")
    return speedVal


while True:
    temperature = GetTemperature()

    if prevTemperature != temperature:
        speedVal = CalcSpeed(temperature)
        SetFanSpeed(speedVal)
        prevTemperature = temperature
    sleep(2)

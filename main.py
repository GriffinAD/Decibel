from modules import commonLib as common
from modules import decibelDisplay as decibel
from modules import timeDisplay as time

options = {
    "dB Meter": decibel,
    "Time": time,
}

# main loop
while True:
    keys = list(options)
    for x in keys:
        index = keys.index(x)
        print(f"{index}: {x}")

    option = input("select option: ")
    selected = keys[int(option)]
    
    v = options[selected]
    
    v.run()

    print(f"Selected option is: {selected}")
# print (f"{decibel} db")

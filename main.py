from modules import commonLib as common
from modules import decibelLib as decibel
from modules import timeDisplay as time
import asyncio
import keyboard

options = {
    "dB Meter": decibel.Decibel,
    "Time": time,
}


async def main():
    # main loop
    while True:
        keys = list(options)
        for x in keys:
            index = keys.index(x)
            print(f"{index}: {x}")

        option = input("select option: ")
        selected = keys[int(option)]
        
        v = options[selected]()
        
        task = asyncio.create_task(v.run())
        
        while not keyboard.is_pressed('q'):
            await asyncio.sleep(0)
                
            
        task.cancel()
                
        try:
            await task
        except asyncio.CancelledError:
            print("main(): cancel_me is cancelled now")
        
        print(f"Selected option was: {selected}")
# print (f"{decibel} db")


# if __name__ == "__main__":

#     async def main():
#         dec = Decibel()
#         task = asyncio.create_task(dec.run())

#         await asyncio.sleep(3)

#         task.cancel()
#         try:
#             await task
#         except asyncio.CancelledError:
#             print("main(): cancel_me is cancelled now")

asyncio.run(main())
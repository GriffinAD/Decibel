if __name__ != "__main__":
    from modules import commonLib as common
else:
    import commonLib as common

import time

def run():
    while True:
        print (time.localtime())
        time.sleep(0.25)

        
if __name__ == "__main__":
    run()
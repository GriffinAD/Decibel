import asyncio
from Deque import Deque
from SampleStats import SampleStats
from HW import ADC


class SensorStats(SampleStats):
    def __init__(
        self,
        rounding: int = -1,
        calibrationOffset: int = 0,
        sampleWindow: int = 0,
        sensor: ADC = ADC(1, 5.0),
    ):
        self.rounding = rounding
        self.sensor = sensor  # this pin reads the analog voltage from the sound level meter
        self.calibrationOffset = calibrationOffset  # offset value for calibration
        self.sampleWindow = sampleWindow

        super().__init__(
            storage=[], sampleWindow=self.sampleWindow, rounding=self.rounding
        )

    def readValue(self):

        voltageValue = self.sensorPin.read()
        # value = (voltageValue / 1024 * self.vREF) * 50
        value = ((voltageValue / 1024.0) * 2.0) + 10.0

        return value

    def processStats(self, decibel):
        super().setValue(decibel)  # type: ignore

    def calcStats(self, method = "avg"):
        # decibelDisplay.ShowDecibel(self.avg())
        value = getattr(super(), method)()

        return(value)

    def ReInit(self):
        pass
    #    self.stats = self.SensorStats(self)

    async def run(self):

        # initialize stats
        # self.stats = self.DecibelStats(self,[])

        # main loop
        while True:
            decibel = self.ReadValue()

            self.ProcessStats(decibel)

            self.DisplayStats()

            # so we can cancel
            await asyncio.sleep(0.0)

            # print (f"{decibel} db")


if __name__ == "__main__":

    async def main():
        dec = SensorStats(sampleWindow=100)
        task = asyncio.create_task(dec.run())

        await asyncio.sleep(3)

        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("main(): cancel_me is cancelled now")

    asyncio.run(main())

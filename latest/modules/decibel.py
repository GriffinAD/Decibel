from deque import deque 
from statistics import mean

class DecibelStats:
        stats = None
        def __init__(self, outer):
            self.__storage = deque([], maxlen=25)
            self.__min = 0
            self.__max = 0
            self.outer = outer
        def __str__(self):
            return f"db:{self.dec} sampleMin:{self.sampleMin()}  sampleMax:{self.sampleMax()}  min:{self.overallMin()}  max:{self.overallMax()}. avg:{self.avg()}"

        def setDecibel(self, value:float):
            self.dec = value

            if self.__min == 0 or self.__min >= value:
                self.__min = value

            if self.__max == 0 or self.__max <= value:
                self.__max = value

            self.__storage.appendleft(value)

        def overallMin(self):
            return self.__min

        def overallMax(self):
            return self.__max

        def sampleMin(self):
            return round(min(self.__storage), self.outer.rounding)

        def sampleMax(self):
            return round(max(self.__storage), self.outer.rounding)

        def avg(self):
            return round(mean(self.__storage), self.outer.rounding)
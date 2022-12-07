from deque import deque
from statistics import mean


class SampleStats(deque):
    stats = None

    def __init__(self, storage, sampleWindow: int = 100, rounding: int = -1):
        #self.__storage = storage
        self.__min = 0
        self.__max = 0
        self.rounding = rounding
        self.value = 0
        
        super().__init__(storage, sampleWindow)

    def __str__(self):
        return f"value:{self.value}  sampleMin:{self.sampleMin()}  sampleMax:{self.sampleMax()}  min:{self.overallMin()}  max:{self.overallMax()}  avg:{self.avg()}"

    def setValue(self, value: float):
        self.value = value

        if self.__min == 0 or self.__min >= value:
            self.__min = value

        if self.__max == 0 or self.__max <= value:
            self.__max = value

        super().append(value)

    def overallMin(self):
        return self.__min

    def overallMax(self):
        return self.__max

    def sampleMin(self):
        return self.round(min(self.data))

    def sampleMax(self):
        return self.round(max(self.data))

    def avg(self):
        return self.round(mean(self.data))

    def round(self, value):
        if self.rounding == -1:
            return value
        if self.rounding == 0:
            return round(value)
        else:
            return round(value, self.rounding)


# a= deque([],10)
a = [1, 2, 3]
d = SampleStats(a, 4)
d.setValue(6.0)
print(d)
# print (d.sampleMax())

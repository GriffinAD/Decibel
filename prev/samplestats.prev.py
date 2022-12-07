from deque import deque 
from statistics import mean

class SampleStatsPrev:
        stats = None
        def __init__(self, storage, rounding: int = 0):
            self.__storage = storage
            self.__min = 0
            self.__max = 0
            self.rounding = rounding
            self.value = 0
        def __str__(self):
            return f"value:{self.value}  sampleMin:{self.sampleMin()}  sampleMax:{self.sampleMax()}  min:{self.overallMin()}  max:{self.overallMax()}  avg:{self.avg()}"

        def setValue(self, value:float):
            self.value = value

            if self.__min == 0 or self.__min >= value:
                self.__min = value

            if self.__max == 0 or self.__max <= value:
                self.__max = value

            self.__storage.append(value)

        def overallMin(self):
            return self.__min

        def overallMax(self):
            return self.__max

        def sampleMin(self):
            return round(min(self.__storage), self.rounding)

        def sampleMax(self):
            return round(max(self.__storage), self.rounding)

        def avg(self):
            return round(mean(self.__storage), self.rounding)

a= deque([],10)
a=[1,2,3]
d=SampleStatsPrev(a)
d.setValue(6.0)
print(d)
#print (d.sampleMax())
import cProfile
from collections import UserList

class deque(UserList):
    """extended list class that can deque items from left or right end"""

    def __init__(self, iterable=[], maxlen=0):
        """constructor
            iterable: existing list, or will create a new empty list
            maxlen: maximum number of items the list can hold
        """
        super().__init__(item for item in iterable)
        self.maxlen = maxlen
        
        
    def __setitem__(self, index, item):
        """set item at index"""
        if len(self.data) >= index:
            self.data[index] = item
        
    def canpop(self):
        """test list to see if we can pop a value"""
        return self.maxlen > 0 and len(self.data) >= self.maxlen
        
        
    def pop(self):
        """pop item from right side"""
        if any(self.data):
            return self.data.pop()
        
        
    def popleft(self):
        """pop item from left side"""
        if any(self.data):
            value = self.data[0]
            del self.data[0]
            return value
        
        
    def insert(self, i: int, item):
        """insert new item at index
            items will pop off right if more than maxitems
        """
        self.data.insert(i, item)
        if self.canpop():
            return self.pop()
        
        
    def insertleft(self, i: int, item):
        """insert new item at index
            items will pop off left if more than maxitems
        """
        self.data.insert(i, item)
        if self.canpop():
            return self.popleft()
        
        
    def append(self, item):
        """ """
        if self.canpop():
            self.popleft()
        self.data.append(item)
        
        
    def appendleft(self, item):
        """ """
        if self.canpop():
            self.pop()
        self.data=[item, self.data]
        
        
    def extend(self, other):
        """ """
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(item for item in other)
        
         
    def reverse(self):
        """ """
        self.data.reverse()
        
        
    def foreach(self, func):
        """ """
        for item in self:
            func(item)
        




arr=[]

x=deque(arr, maxlen = 100000)

for l in range (0,100000):
    x.append(l)

x.popleft()
x.popleft()

print (len(x))  



def test():
    for t in range(0,100000):
        x.append(2)
        x.pop()
        x.appendleft(9)
        x.popleft()
    #print (len(x))


p = cProfile.Profile()
p.runcall(test)
p.print_stats()
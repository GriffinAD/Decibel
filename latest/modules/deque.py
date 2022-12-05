import cProfile
from collections import UserList

class dequeQ(UserList):
    def __init__(self, iterable, maxlen=0):
        super().__init__(item for item in iterable)
        self.maxlen = maxlen
        
    def __setitem__(self, index, item):
        self.data[index] = item
        
    def insert(self, i: int, item):
        self.data.insert(i, item)
        
    def append(self, item):
        if self.maxlen>0:
            if len(self.data) >= self.maxlen:
                self.popleft()
        self.data.append(item)

    def appendleft(self, item):
        if self.maxlen>0:
            if len(self.data) >= self.maxlen:
                self.pop()
        self.data=[item,self.data]
                
    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(item for item in other)
    
    def reverse(self):
        self.data.reverse() 
        
    def pop(self):
        self.data.pop()
        
    def popleft(self):
        if len(self.data)>0:
            v=self.data[0]
            del self.data[0]
            return v



arr=[]

x=dequeQ(arr, maxlen = 10000)

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
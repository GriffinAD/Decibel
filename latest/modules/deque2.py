
#from collections import *
import cProfile

class deque:

    def __init__(self, iterable = [], maxlen = 0):
        self.iterable = iterable
        self.maxlen = maxlen
        #print (self.iterable)
    
    # def __str__(self):
    #     return self.iterable
    
    # def __iter__(self):
    #     yield self.iterable
    
    def pop(self):
        if any(self.iterable):
            return self.iterable.pop()
        else:
            raise IndexError ("pop from an empty deque")
            return None
        
    def popleft(self):
        if any(self.iterable):
            return self.iterable.pop(0)
        else:
            raise IndexError ("pop from an empty deque")
            return None
        
    def appendleft(self, value):
        if len(self.iterable) >= self.maxlen:
            self.pop()
        self.iterable=[value, self.iterable] #.insert(0, value)
    
    def append(self, value):
        if len(self.iterable) >= self.maxlen:
            self.popleft()
        self.iterable.append(value) 
    
    def clear(self):
        self.iterable.clear()
        
    def reverse(self):
        self.iterable.reverse() 
        
     
x=deque([],maxlen = 100000)

for l in range (0,100000):
    x.append(l)


print (min(x.iterable))  



def test():
    for t in range(0,100000):
        x.append("1")
        x.pop()
        x.appendleft("9")
        x.popleft()

p = cProfile.Profile()
p.runcall(test)
p.print_stats()





# for t in range(0,100000):
#     x.append("1")
#     x.pop()
#     x.appendleft("9")
#     x.popleft()

# x.append(1)

# x.appendleft(9)

# print (x.iterable)

# x.reverse()

# print (x.iterable)

# x.clear()

#print (x.iterable)
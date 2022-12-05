
#from collections import *


class deque:
    def __init__(self, iterable = [], maxlen = 0):
        self.iterable = iterable
        self.maxlen = maxlen
    
    def pop():
        if any(self.iterable)
            return self.iterable.pop()
        else:
            raise IndexError: "pop from an empty deque"
            return None
        
    def popLeft():
        if any(self.iterable)
            return self.iterable.pop(0)
        else:
            raise IndexError: "pop from an empty deque"
            return None
        
    def appendLeft(value):
        if len(self.iterable) >= self.maxlen
            self.pop()
        self.iterable.insert(0, value)
    
    def append(value):
        if len(self.iterable) >= self.maxlen
            self.popLeft()
        self.iterable.append(value) 
    
    def clear():
        self.iterable.clear()
        
    def reverse()
        self.iterable.reverse() 
     

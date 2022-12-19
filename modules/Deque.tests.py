import Deque

test = Deque([],5)

test.append(1)
assert len(test)==1
assert test[0]==1
assert test==[1]

test.insert(0,2)
assert len(test)==1
assert test[0]==2
assert test==[2,1]

test.insertleft(3)
assert len(test)==3
assert test[0]==3
assert test==[3,2,1]

test.reverse()
assert len(test)==3
assert test[0]==1
assert test==[1,2,3]



test.append(4)
test.insert(0)
assert len(test)==5
assert test[0]==0
assert test==[0,1,2,3,4]

test.append(5)
assert len(test)==5
assert test[0]==1
assert test==[1,2,3,4,5]

test.appendleft(0)
assert len(test)==5
assert test[0]==0
assert test==[0,1,2,3,4]

assert test.pop()==4
assert len(test)==4
assert test[0]==0
assert test==[0,1,2,3]

assert test.popleft()==0
assert len(test)==3
assert test[0]==1
assert test==[1,2,3]

test2=[4,5]
test.extend(test2)
assert len(test)==5
assert test==[1,2,3,4,5]

test2.foreach("min")

    

    def dopop(self):
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

    def insert(self, index: int, item):
        """
        insert new item at index
            items will pop off right if more than maxitems
        """
        if len(self.data) > index:
            self.data.insert(index, item)
        if self.dopop():
            return self.pop()

    def insertleft(self, index: int, item):
        """
        insert new item at index
            items will pop off left if more than maxitems
        """
        if len(self.data) > index:
            self.data.insert(index, item)
        if self.dopop():
            return self.popleft()

    def append(self, item):
        """
        append item to end of list
            items will pop off left side if more than maxitems
        """
        if self.dopop():
            self.popleft()
        self.data.append(item)

    def appendleft(self, item):

        """
        append item at start of list
            items will pop off right if more than maxitems
        """
        if self.dopop():
            self.pop()
        self.data = [item, self.data]

    def extend(self, other):
        """extend data set with more data"""
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(item for item in other)

    def reverse(self):
        """ """
        self.data.reverse()

    def foreach(self, func):
        """iterate using a passed in function"""
        for item in self:
            func(item)


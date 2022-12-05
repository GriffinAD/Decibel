from collections import deque
import cProfile

x=deque([],maxlen = 100000)

for l in range (0,100000):
    x.append(l)


def test():
    for t in range(0,100000):
        x.append("1")
        x.pop()
        x.appendleft("9")
        x.popleft()

p = cProfile.Profile()
p.runcall(test)
p.print_stats()

#print (x)

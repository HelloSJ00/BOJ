# 큐 큐2
import sys
import collections

class queue():
    def __init__(self):
        self.myqueue = collections.deque([])
    
    def push(self,data):
        self.myqueue.append(data)

    def _pop(self):
        if len(self.myqueue) != 0:
            print(self.myqueue.popleft())
        else:
            print(-1)

    def size(self):
        print(len(self.myqueue))

    def empty(self):
        if len(self.myqueue) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.myqueue) != 0:
            print(self.myqueue[0])
        else:
            print(-1)
    def back(self):
        if len(self.myqueue) !=0:
            print(self.myqueue[len(self.myqueue)-1])
        else:
            print(-1)

q = queue()

N = int(sys.stdin.readline())

while  N > 0:
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        q.push(int(command[1]))
    elif command[0] == 'pop':
        q._pop()
    elif command[0] == 'size':
        q.size()
    elif command[0] == 'empty':
        q.empty()
    elif command[0] == 'front':
        q.front()
    elif command[0] == 'back':
        q.back()

    N -=1


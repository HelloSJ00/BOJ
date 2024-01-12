# 큐 요세푸스 문제 0

import sys
import collections

queue = []
anwser = []

N, K = map(int,sys.stdin.readline().split())

for i in range(N):
    queue.append(i+1)
    
index = 0

while len(queue) > 0:
    if len(queue) == 1:
        anwser.append(queue.pop())
        break
    
    index += K-1
    while index >= len(queue):
        index = index - (len(queue))
    anwser.append(queue.pop(index))
    
print('<',end='')
for i in range(N):
    print(anwser[i],end='')
    if i != N-1:
        print(',',end=' ')
    else:
        print('>')

    



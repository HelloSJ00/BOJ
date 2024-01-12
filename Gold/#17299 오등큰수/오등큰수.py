# 오등큰수

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numList = list(map(int,input().split()))
numStorage = []
F = {}
result=deque([])

for i in numList: # 등장횟수 
    if i not in F:
        F[i] = 1
    elif i in F:
        F[i] +=1

while numList:
    if len(numList) == N:
        result.append(-1)
        numStorage.append(numList.pop())
        continue

    if F[numStorage[len(numStorage)-1]] > F[numList[len(numList)-1]]:
        result.append(numStorage[len(numStorage)-1])
        numStorage.append(numList.pop())

    elif F[numStorage[len(numStorage)-1]] <= F[numList[len(numList)-1]]:
        if len(numStorage) == 1:
            result.append(-1)
            numStorage.pop()
            numStorage.append(numList.pop())
        else:
            numStorage.pop()
for i in range(N):
    if i != N-1:
        print(result.pop(),end=' ')
    else:
        print(result.pop())
        



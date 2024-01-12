#오큰수

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numList = deque(list(map(int,input().split())))
NGEs = deque([])
numStorage=deque([])

while numList: # 배열뒤부터 순환 하면서 오큰수 저장
    if len(numList) == N :
        NGEs.append(-1)
        numStorage.append(numList.pop())
        continue

    if numList[len(numList)-1] < numStorage[len(numStorage)-1]:
        NGEs.append(numStorage[len(numStorage)-1]) 
        numStorage.append(numList.pop())

    elif numList[len(numList)-1] >= numStorage[len(numStorage)-1]:
        if len(numStorage) == 1:
            NGEs.append(-1)
            numStorage.pop()
            numStorage.append(numList.pop())
        else:
            numStorage.pop()


for i in range(N): # 출력
    if i != N-1:
        print(NGEs.pop(),end=' ')
    else:
        print(NGEs.pop())
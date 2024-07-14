import sys
from collections import deque
input = sys.stdin.readline

# 수빈 위치 n, 동생 위치 k
n,k=map(int,input().split())
arr=[0] * (100001)

queue = deque([n])

while queue:
  d = queue.popleft()
  if k == d:
    print(arr[d])
    break

  for i in (d-1, d+1, d*2):
    if 0 <= i < 100001 and arr[i] == 0 :
      arr[i] = arr[d]+1
      queue.append(i)
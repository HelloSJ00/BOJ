import sys
from collections import deque
input = sys.stdin.readline
# 시간제한 1초 
queue = deque()

def bfs():
  while queue:
    k = queue.popleft()
    for i in range(V):
      if G[k][i] == 1 and visit[i] == 0:
        queue.append(i)
        visit[i] = 1
#입력 
V = int(input().rstrip())

# 그래프
G = []
for i in range(V):
  G.append(list(map(int,input().split())))

#출력
for i in range(V):
  visit = [0 for _ in range(V)]
  queue.append(i)
  bfs()
  print(*visit)
    

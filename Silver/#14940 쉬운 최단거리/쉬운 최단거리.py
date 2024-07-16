import sys
input = sys.stdin.readline
from collections import deque

dy = [0,-1,0,1]
dx = [-1,0,1,0]

def bfs(y,x):
  visit[y][x] = 0
  queue.append((y,x))
  while queue:
    y,x = queue.popleft()
    for i in range(4):
      if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and graph[y + dy[i]][x + dx[i]] ==1 and visit[y + dy[i]][x + dx[i]]==0 :
        visit[y + dy[i]][x + dx[i]] = visit[y][x] +1
        queue.append((y + dy[i],x + dx[i]))

# 입력
N , M = map(int,input().split())
graph = []
visit = [[0]*M for _ in range(N)]
for _ in range(N):
  graph.append(list(map(int,input().split())))

queue = deque()
for y in range(N):
  for x in range(M):
    if graph[y][x] == 2:
      bfs(y,x)

for y in range(N):
  for x in range(M):
    if graph[y][x] == 1 and visit[y][x] == 0:
      visit[y][x] = -1
      
for i in range(N):
  print(*visit[i])
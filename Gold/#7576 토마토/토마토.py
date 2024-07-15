import sys
input = sys.stdin.readline
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs():
  while queue:
    y,x = queue.popleft()
    for i in range(4):
      if 0<= y+dy[i] < M and 0<= x+dx[i] < N and visit[y+dy[i]][x+dx[i]] == 0 and tomato[y+dy[i]][x+dx[i]] == 0:
        visit[y+dy[i]][x+dx[i]] = 1
        tomato[y+dy[i]][x+dx[i]] = tomato[y][x] + 1
        queue.append((y+dy[i],x+dx[i]))

N,M = map(int,input().split())
tomato = []
for i in range(M):
  tomato.append(list(map(int,input().split())))
visit = [[0]*N for _ in range(M)]
queue = deque()

for y in range(M):
  for x in range(N):
    if tomato[y][x] == 1:
      queue.append((y,x))
bfs()
answer = 0
flag = 1
for y in range(M):
  for x in range(N):
    if tomato[y][x] == 0:
      flag = 0
    answer = max(answer,tomato[y][x])
if flag == 1:
  print(answer-1)
else:
  print(-1)
    
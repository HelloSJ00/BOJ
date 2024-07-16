import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

dy = [0,-1,0,1]
dx = [-1,0,1,0]

def bfs(y,x,cnt):
  queue.append((y,x))
  visit[y][x] = 1
  graph[y][x] = cnt
  while queue:
    cur_y,cur_x = queue.popleft()
    for i in range(4):
      if 0 <= cur_y + dy[i] < N and 0 <= cur_x + dx[i] < N and visit[cur_y + dy[i]][cur_x + dx[i]]==0 and graph[cur_y + dy[i]][cur_x + dx[i]]==1:
        visit[cur_y + dy[i]][cur_x + dx[i]] = 1
        graph[cur_y + dy[i]][cur_x + dx[i]] = cnt
        queue.append((cur_y+dy[i],cur_x+dx[i]))


graph = []
for _ in range(N):
  graph.append(list(map(int,input().rstrip())))
queue = deque()
visit = [[0]*N for _ in range(N)]

cnt = 0
for y in range(N):
  for x in range(N):
    if visit[y][x] == 0 and graph[y][x]==1:
      cnt +=1
      bfs(y,x,cnt)

answer_list = [0]*(cnt+1)
for y in range(N):
  for x in range(N):
    answer_list[graph[y][x]] +=1


answer_list = answer_list[1:]
answer_list.sort()
print(cnt)
for i in range(cnt):
  print(answer_list[i])
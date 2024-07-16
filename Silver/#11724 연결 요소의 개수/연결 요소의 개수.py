import sys
input = sys.stdin.readline
from collections import deque

def checkbfs(num):
  global answer
  queue.append(num)
  visit[num] = 1
  while queue:
    s = queue.popleft()
    for i in graph[s]:
      if visit[i] == 0:
        visit[i] = 1
        queue.append(i)
  answer +=1

V ,E = map(int,input().split())
graph = [[] for _ in range(1001)]
for _ in range(E):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0]*1001
answer = 0
queue = deque()
for i in range(1,V+1):
  if visit[i] != 1:
    checkbfs(i)
print(answer)
import sys
from collections import deque
input = sys.stdin.readline

computer = int(input().rstrip())
E = int(input().rstrip())
graph = [[] for _ in range(computer+1)]

for _ in range(E):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0]*(computer+1)

queue =deque([1])
visit[1] = 1

cnt = 0
while queue:
  virus = queue.popleft()
  for i in graph[virus]:
    if visit[i] == 0:
      cnt +=1
      visit[i] = 1
      queue.append(i)
print(cnt)
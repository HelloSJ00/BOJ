import sys
from collections import deque
input = sys.stdin.readline


# 입력
N = int(input().rstrip())
Graph = [[] for _ in range(N+1)]
parent = [0]*(N+1)
parent[1] = -1
queue = deque([1])

# 노드 추가
for _ in range(N-1):
  a,b = map(int,input().split())
  Graph[a].append(b) 
  Graph[b].append(a) 


while queue:
  cur_parent = queue.popleft()
  for child in Graph[cur_parent]:
    if parent[child] == 0:
      parent[child] = cur_parent
      queue.append(child)

# 출력
for i in range(2,N+1):
  print(parent[i])

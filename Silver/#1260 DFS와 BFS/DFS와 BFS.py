import sys
input = sys.stdin.readline
from collections import deque

# 시간제한 2초 , 입력제한 1~20 , |S| <=1,000,000  

def dfs():
  tmp = stack.pop()
  for i in range(len(G[tmp])):
    if G[tmp][i] not in visit_dfs :
      visit_dfs.append(G[tmp][i])
      stack.append(G[tmp][i])
      dfs()

def bfs():
  while True:
    if q:
      tmp = q.popleft()
      for i in range(len(G[tmp])):
        if G[tmp][i] not in visit_bfs :
          visit_bfs.append(G[tmp][i])
          q.append(G[tmp][i])
    else:
      break


# 입력
# bfs
q=deque()
visit_bfs=[]
# dfs
stack=[]
visit_dfs=[]

V,E,start= map(int,(input().split()))
q.append(start-1)
visit_bfs.append(start-1)
stack.append(start-1)
visit_dfs.append(start-1)
G =[[] for _ in range(V)]
for _ in range(E):
  i,j = map(int,input().split())
  G[i-1].append(j-1)
  G[j-1].append(i-1)

for row in G:
  row.sort()
bfs()
dfs()
# 보정
for i in range(len(visit_bfs)):
  visit_bfs[i] +=1
for i in range(len(visit_dfs)):
  visit_dfs[i] +=1

# 출력
print(*visit_dfs)
print(*visit_bfs)

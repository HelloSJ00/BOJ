import sys
input = sys.stdin.readline
from collections import deque

def kevinBacon(num):
  queue.append((num,0))
  # 개인마다
  visit = [0]*(N+1)
  visit[num] = 1
  kevinBaconList = [0]*(N+1)
  while queue:
    s ,cnt = queue.popleft()
    kevinBaconList[s] = cnt
    for friend in graph[s]:
      if visit[friend] == 0 :
        queue.append((friend,cnt+1))
        visit[friend] = 1

  # bfs 끝나고
  sum = 0
  for i in range(1,N+1):
    sum += kevinBaconList[i]
  # print('kevinBaconList',kevinBaconList)
  # print('num',num,'sum',sum)
  return sum

# 입력
N ,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  y,x = map(int,input().split())
  graph[y].append(x)
  graph[x].append(y)

queue = deque()
answer = 0
for human in range(1,N+1):
  if answer == 0 :
    answer = human
    answer_kevin = kevinBacon(human)

  else:
    cur_kevin = kevinBacon(human)
    if cur_kevin < answer_kevin:
      answer = human
      answer_kevin = cur_kevin
    elif cur_kevin == answer_kevin:
      answer = min(human,answer)
print(answer)

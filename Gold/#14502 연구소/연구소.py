import sys
input = sys.stdin.readline
from collections import deque

# 시간제한 2초 , 입력제한 1~1000  
visit1=[[0 for col in range(10)] for row in range(10)]
visit2=[[0 for col in range(10)] for row in range(10)]
dx =[0,-1,0,1]
dy =[-1,0,1,0]


# 출력
def bfs():
  global answer
  # 바이러스 찾기
  for x in range(N):
    for y in range(M):
      # 맵 복사
      visit1[x][y] = Map[x][y]
      if Map[x][y] == 2:
        queue.append([x,y])

  #바이러스 확산시키기
  while queue:
    x,y = queue.popleft()
    visit1[x][y] = 1
    for i in range(4):
      if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and Map[x+dx[i]][y+dy[i]] == 0 and visit1[x+dx[i]][y+dy[i]] == 0:
        visit1[x+dx[i]][y+dy[i]] = 1
        queue.append([x+dx[i],y+dy[i]])

  # 연구실 카운팅
  cnt = 0
  for x in range(N):
    for y in range(M):
      if Map[x][y] == 0 and visit1[x][y] == 0:
        cnt +=1
  answer = max(answer,cnt)

def bt(select):
  if select == 3:
    bfs()
    return
  for x in range(N):
    for y in range(M):
      if not Map[x][y] and not visit2[x][y]:
        visit2[x][y] = 1
        Map[x][y] = 1
        bt(select+1)
        Map[x][y] = 0
        visit2[x][y] = 0


# 입력
N,M = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
answer=0
bt(0)
print(answer)
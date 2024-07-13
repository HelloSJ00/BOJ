import sys
input = sys.stdin.readline
from collections import deque

dy = [0,-1,0,1]
dx = [-1,0,1,0]
def bfs(answer):
  while queue:
    cur_y , cur_x = queue.popleft()
    for i in range(4):
      if 0 < cur_y + dy[i] < M+1 and 0< cur_x + dx[i] < N+1:
        # print('요기 방문 ',cur_y + dy[i],cur_x +dx[i],i)
        if Map[cur_y + dy[i]][cur_x +dx[i]] == 1 and visit[cur_y + dy[i]][cur_x +dx[i]] == 0:
          queue.append((cur_y + dy[i],cur_x + dx[i]))
        
        visit[cur_y + dy[i]][cur_x +dx[i]] = 1
    # print(queue)
  # print('answer 1업!')
  answer += 1
  return answer


# 입력
TestCase = int(input().rstrip())
for _ in range(TestCase):
  M,N,K = map(int,input().split())
  # 지도는 1~50 index 줬음
  visit = [[0]*(N+1) for _ in range(M+1)] 
  Map = [[0]*(N+1) for _ in range(M+1)] 
  for _ in range(K):
    # bfs를 위한 덱
    queue = deque()
    # 좌표는 Y-1,X-1 상태로 입력하기 때문에 지도에서 +1씩 해줌
    y,x = map(int,input().split())
    Map[y+1][x+1] = 1
  # print(Map)
  answer = 0
  for i in range(1,M+1):
    for j in range(1,N+1):
      if visit[i][j] == 0 and Map[i][j] == 1 :
        visit[i][j] = 1
        queue.append((i,j))
        answer = bfs(answer)
      else:
        visit[i][j] = 1
  print(answer)
import sys
from collections import deque
input = sys.stdin.readline

dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]

def bfs():
	while queue:
		cur_z,cur_y,cur_x = queue.popleft()
		for i in range(6):
			if 0 <= cur_z+dz[i] < H and 0 <= cur_y+dy[i] < N and 0 <= cur_x+dx[i] < M and graph[cur_z+dz[i]][cur_y+dy[i]][cur_x+dx[i]] == 0:
				graph[cur_z+dz[i]][cur_y+dy[i]][cur_x+dx[i]] = graph[cur_z][cur_y][cur_x] +1
				queue.append((cur_z+dz[i],cur_y+dy[i],cur_x+dx[i]))
	
M,N,H = map(int,input().split())

graph = []
# 그래프 생성
for _ in range(H):
	tmp = []
	for _ in range(N):
		tmp.append(list(map(int,input().split())))
	graph.append(tmp)

# bfs를 위한 deque 생성
queue = deque()

# bfs
for z in range(H):
	for y in range(N):
		for x in range(M):
			if graph[z][y][x] == 1:
				queue.append((z,y,x))

bfs()

tof = True
answer = 0
# answer 찾기
for z in range(H):
	if tof is True:
		for y in range(N):
			if tof is True:
				for x in range(M):
					if graph[z][y][x] == 0:
						tof = False
						break
					answer = max(answer,graph[z][y][x])

# print(visit)
if tof is True:
	print(answer-1)
else:
	print(-1)


import sys
input = sys.stdin.readline
from collections import deque

dy = [0,-1,0,1]
dx = [-1,0,1,0]

def count_general(y,x):
	queue.append((y,x))
	while queue:
		cur_y,cur_x = queue.popleft()
		for i in range(4):
			if 0<=cur_y + dy[i]< N and 0<=cur_x + dx[i]<N and visit[cur_y + dy[i]][cur_x + dx[i]]==0 and graph[cur_y][cur_x] == graph[cur_y+dy[i]][cur_x + dx[i]]:
				visit[cur_y+dy[i]][cur_x+dx[i]] = 1
				queue.append((cur_y+dy[i],cur_x + dx[i]))
	answer[0] += 1

def count_not_general(y,x):
	queue.append((y,x))
	while queue:
		cur_y,cur_x = queue.popleft()
		for i in range(4):
			# 파랑이면 파랑만 탐색
			if graph[cur_y][cur_x] == 'B':
				if 0<=cur_y + dy[i]< N and 0<=cur_x + dx[i]<N and visit[cur_y + dy[i]][cur_x + dx[i]]==0 and graph[cur_y][cur_x] == graph[cur_y+dy[i]][cur_x + dx[i]]:
					visit[cur_y+dy[i]][cur_x+dx[i]] = 1
					queue.append((cur_y+dy[i],cur_x + dx[i]))
			# 파랑이 아닐경우 파랑이 아니면 탐색
			else:
				if 0<=cur_y + dy[i]< N and 0<=cur_x + dx[i]<N and visit[cur_y + dy[i]][cur_x + dx[i]]==0 and graph[cur_y+dy[i]][cur_x + dx[i]] != 'B':
					visit[cur_y+dy[i]][cur_x+dx[i]] = 1
					queue.append((cur_y+dy[i],cur_x + dx[i]))
	answer[1] += 1

N = int(input().rstrip())
graph = []
for _ in range(N):
	graph.append(list(input().rstrip()))

visit = [[0]*N for _ in range(N)]
queue = deque()

answer = [0,0]
for y in range(N):
	for x in range(N):
		if visit[y][x] == 0:
			count_general(y,x)

visit = [[0]*N for _ in range(N)]
for y in range(N):
	for x in range(N):
		if visit[y][x] == 0:
			count_not_general(y,x)

print(*answer)
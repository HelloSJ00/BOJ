import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(N)]
dy = [0,-1,0,1]
dx = [-1,0,1,0]

def whereAmI():
	for y in range(N):
		for x in range(M):
			if graph[y][x] == 'I':
				return y,x

def bfs():
	global answer 
	y,x = whereAmI()
	graph[y][x] = 'X'
	queue.append((y,x))
	while queue:
		cur_y,cur_x = queue.popleft()
		for i in range(4):
			if 0<=cur_y + dy[i] < N and 0<= cur_x+dx[i] < M and graph[cur_y + dy[i]][cur_x+dx[i]] != 'X':
				if graph[cur_y + dy[i]][cur_x+dx[i]] == 'P':
					answer +=1
				graph[cur_y + dy[i]][cur_x+dx[i]] = 'X'
				queue.append((cur_y + dy[i],cur_x+dx[i]))
	
	if answer == 0:
		print('TT')
	else:
		print(answer)


answer = 0
queue = deque()
bfs()
import sys
input = sys.stdin.readline
from collections import deque

def snake_game(start,cnt):
	global answer

	queue.append((start,cnt))
	while queue:
		cur_v,cur_cnt= queue.popleft()
		# 종료조건
		if cur_v == 100:
			answer = min(answer,cur_cnt)
			continue

		for i in range(1,7):
			if cur_v+i <= 100 and visit[cur_v+i] == 0:
				queue.append((graph[cur_v+i],cur_cnt+1))
				visit[cur_v+i] = 1

N,M = map(int,input().split())
graph = [i for i in range(101)]
visit = [0]*101
answer =100
queue = deque()
for _ in range(N+M):
	a,b = map(int,input().split())
	graph[a] = b

snake_game(1,0)
print(answer)
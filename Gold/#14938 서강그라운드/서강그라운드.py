import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,graph,M):
	visited = [0]*101
	queue = deque([(start,M)])
	answer = 0
	while queue:
		cur_v,move = queue.popleft()
		if move < 0:
			continue
		else:
			if visited[cur_v] != 1:
				visited[cur_v] = 1
			for nv,nd in graph[cur_v]:
				queue.append((nv,move-nd))
	
	for i in range(101):
		if visited[i] == 1:
			answer += arr[i]
	return answer
	
N, M, R = map(int,input().split())
arr=[0]
arr += list(map(int,input().split()))
graph = [[] for _ in range(101)]
for _ in range(R):
	s,e,d = map(int,input().split())
	graph[s].append((e,d))
	graph[e].append((s,d))

answer = 0
for i in range(1,N+1):
	answer = max(answer,bfs(i,graph,M))
print(answer)
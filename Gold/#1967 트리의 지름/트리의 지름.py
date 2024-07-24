import sys
input = sys.stdin.readline
from collections import deque

def dfs(start):
	stack = []
	visit = [0]*10001
	visit[start] = 1
	value = [0,0]
	stack.append((start,0))
	while stack:
		cur_vertex,cur_value = stack.pop()
		if value[1] < cur_value:
			value = [cur_vertex,cur_value]
		for next_vertex in graph[cur_vertex]:
			if visit[next_vertex[0]] == 0:
				visit[next_vertex[0]] = 1
				stack.append((next_vertex[0],cur_value+next_vertex[1]))
	return value

N = int(input().rstrip())
graph = [[] for _ in range(10001)]

for _ in range(N-1):
	node1,node2,weight = map(int,input().split())
	graph[node1].append((node2,weight))
	graph[node2].append((node1,weight))

first_dfs = dfs(1)
print(dfs(first_dfs[0])[1])
import sys,heapq
input = sys.stdin.readline
from collections import deque

def dijkstra(start,graph):
	queue =[]
	visit = [float('inf')]*1001
	heapq.heappush(queue,(0,start))
	while queue:
		cur_distance,cur_vertex = heapq.heappop(queue)

		if cur_distance > visit[cur_vertex]:
			continue

		for next_vertex,next_distance in graph[cur_vertex]:
			distance = cur_distance + next_distance
			if distance < visit[next_vertex]:
				visit[next_vertex] = distance
				heapq.heappush(queue,(distance,next_vertex))

	return visit

N,M,X = map(int,input().split())
graph1 = [[] for _ in range(1001)]
graph2 = [[] for _ in range(1001)]
for _ in range(M):
	s,d,w = map(int,input().split())
	graph1[s].append((d,w))
	graph2[d].append((s,w))

answer = dijkstra(X,graph1)[1:N+1]
tmp = dijkstra(X,graph2)[1:N+1]
for i in range(N):
	answer[i] += tmp[i]
print(max(answer[:X-1]+answer[X:N+1]))
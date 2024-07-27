import sys,heapq
input = sys.stdin.readline

def dijkstra(start,end,graph):
	queue = [(0,start)]
	visit = [float('inf')]*1001
	while queue:
		cur_value,cur_v = heapq.heappop(queue)
		if visit[cur_v] <= cur_value:
			continue
		visit[cur_v] = cur_value
		for next_v,next_value in graph[cur_v]:
			heapq.heappush(queue,(cur_value+next_value,next_v))
	return visit[end]

V = int(input().rstrip())
E = int(input().rstrip())
graph = [[] for _ in range(1001)]
for _ in range(E):
	s,e,value = map(int,input().split())
	graph[s].append((e,value))
start,end = map(int,input().split())
print(dijkstra(start,end,graph))
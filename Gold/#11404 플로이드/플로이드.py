import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
	distance = [float('inf')]*(101)
	queue = [(0,start)]
	while queue:
		cur_distacne, cur_v = heapq.heappop(queue)

		if cur_distacne >= distance[cur_v]:
			continue

		distance[cur_v] = cur_distacne
		for nv,nd in edge[cur_v]:
			heapq.heappush(queue,(cur_distacne+nd,nv))

	return distance

N = int(input().rstrip())
M = int(input().rstrip())
edge = [[] for _ in range(N+1)]
for _ in range(M):
	tof = True
	s,e,d = map(int,input().split())
	for i in range(len(edge[s])):
		if edge[s][i][0] == e:
			edge[s][i][1] = min(edge[s][i][1],d)
			tof = False
			break
	if tof is True:
		edge[s].append([e,d])

for i in range(1,N+1):
	for i in dijkstra(i)[1:N+1]:
		if i == float('inf'):
			print(0,end=' ')
		else:
			print(i,end=' ')
	print()

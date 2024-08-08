import sys,heapq
from collections import deque
input = sys.stdin.readline

def topology_sort(graph,prev_v,timeToBuild,N):
	time = [0]*(N+1)
	queue = deque()

	for v in range(1,len(prev_v)):
		if prev_v[v] == 0:
			queue.append(v)
			time[v] = timeToBuild[v] #[0,10,0,0,0]

	while queue:
		cv = queue.popleft()
		prev_v[cv] = -1

		for nv in graph[cv]:
			prev_v[nv] -= 1
			time[nv] = max(time[nv],time[cv]+timeToBuild[nv])
			if prev_v[nv] == 0:
				queue.append(nv)
		# for v in range(1,len(prev_v)):
		# 	if prev_v[v] == 0:
		# 		queue.append(v)

	return time
TC = int(input().rstrip())
for _ in range(TC):
	N,K = map(int,input().split())
	graph = [[] for _ in range(N+1)]

	# 짓는데 걸리는 시간
	timeToBuild = [0]+list(map(int,input().split()))

	prev_v = [0]*(N+1)
	for i in range(K):
		s,e = map(int,input().split())
		graph[s].append(e)
		prev_v[e] +=1
	
	answer_idx = int(input().rstrip())

	a = topology_sort(graph,prev_v,timeToBuild,N)
	# print(a)
	print(a[answer_idx])




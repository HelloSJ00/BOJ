import sys
input = sys.stdin.readline

def bellman_ford(vertexs, edges):
	distance = [0]*501
	for iter in range(vertexs):
		for cur_vertex, next_vertex, next_distance in edges:
			if distance[cur_vertex] + next_distance < distance[next_vertex]:
				if iter == vertexs-1:
					return True
				distance[next_vertex] = distance[cur_vertex] + next_distance
	return False

TC = int(input().rstrip())
for _ in range(TC):
	edges=[]
	N, M, W = map(int,input().split())
	for _ in range(M):
		s,e,t = map(int,input().split())
		edges.append((s,e,t))
		edges.append((e,s,t))
	for _ in range(W):
		s,e,t = map(int,input().split())
		edges.append((s,e,-t))
	if bellman_ford(N,edges) is True:
		print('YES')
	else:
		print('NO')
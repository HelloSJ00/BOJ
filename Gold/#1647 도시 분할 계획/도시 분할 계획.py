import sys
input = sys.stdin.readline

def get_parent(x):
	if parent[x] == x:
		return x
	else:
		parent[x] = get_parent(parent[x])
		return parent[x]

def union_parent(a,b):
	a = get_parent(a)
	b = get_parent(b)
	if a < b :
		parent[b] = a
	else:
		parent[a] = b

def same_parent(a,b):
		return get_parent(a) == get_parent(b)

def city_break(edges):
	answer = []
	for a,b,cost in edges:
		if not same_parent(a,b):
			union_parent(a,b)
			answer.append(cost)
	return print(sum(answer)-max(answer))

# 입력
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
edges = []
for i in range(M):
	s,e,v = map(int,input().split())
	edges.append((s,e,v))
edges.sort(key = lambda x : x[2])
# print(edges)
city_break(edges)
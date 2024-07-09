import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
def dijkstra(start, vertex, graph):
  distances = [INF for _ in range(vertex+1)]
  distances[start] = 0
  queue = [(0,start)]
  while queue:
    cur_dis,cur_vertex = heapq.heappop(queue)
    if distances[cur_vertex] < cur_dis:
      continue
    for neighbor,weight in graph[cur_vertex]:
      distance = cur_dis + weight
      if distances[neighbor] > distance:
        distances[neighbor] = distance
        heapq.heappush(queue,(distance,neighbor))
  return distances


# 첫쨰줄
V,E = map(int,input().split())
# 시작점
start = int(input().rstrip())
graph = [[] for _ in range(V+1)]

# 간선
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
answer = dijkstra(start,V,graph)
for i in answer[1:]:
  if i == float('inf'):
    print('INF')
  else:
    print(i)
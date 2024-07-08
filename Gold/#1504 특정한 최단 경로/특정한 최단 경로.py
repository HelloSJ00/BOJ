import sys
import heapq

def dijkstra(start, V, graph):
    distances = [float('inf')] * (V + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

input = sys.stdin.readline

# 첫쨰줄
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

# 간선
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

# 마지막줄
V1, V2 = map(int, input().split())

# 1번 정점에서 모든 정점까지의 최단 거리
dist_from_1 = dijkstra(1, V, graph)
# V1 정점에서 모든 정점까지의 최단 거리
dist_from_V1 = dijkstra(V1, V, graph)
# V2 정점에서 모든 정점까지의 최단 거리
dist_from_V2 = dijkstra(V2, V, graph)

# 가능한 두 경로 중 최소 경로 선택
path1 = dist_from_1[V1] + dist_from_V1[V2] + dist_from_V2[V]
path2 = dist_from_1[V2] + dist_from_V2[V1] + dist_from_V1[V]

result = min(path1, path2)

if result < float('inf'):
    print(result)
else:
    print(-1)

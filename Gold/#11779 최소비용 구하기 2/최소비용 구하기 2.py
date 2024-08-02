import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = [(0, start)]
    distance = [(float('inf'), 0)] * (N + 1)
    distance[start] = (0, start)
    
    while queue:
        cur_d, cur_v = heapq.heappop(queue)
        if distance[cur_v][0] < cur_d:
            continue
        
        for nv, nd in graph[cur_v]:
            cost = cur_d + nd
            if cost < distance[nv][0]:
                distance[nv] = (cost, cur_v)
                heapq.heappush(queue, (cost, nv))
    
    return distance

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
sv, ev = map(int, input().split())

# 다익스트라 알고리즘을 수행하고 결과를 받는다.
arr = dijkstra(sv)

# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
print(arr[ev][0])

# 최소 비용을 갖는 경로를 찾는다.
route = []
tmp = ev
while tmp != sv:
    route.append(tmp)
    tmp = arr[tmp][1]
route.append(sv)
route.reverse()

# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다.
print(len(route))

# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.
print(' '.join(map(str, route)))

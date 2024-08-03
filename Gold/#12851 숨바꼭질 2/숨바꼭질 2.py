import sys ,heapq
input = sys.stdin.readline

def dijkstra(start):
  distance = [[float('inf'),0] for _ in range(100001)]
  queue= [(0,start)]
  while queue:
    cur_d,cur_v = heapq.heappop(queue)
    if cur_v < 0 or cur_v >100000:
      continue

    if cur_d > distance[cur_v][0]:
      continue
    elif cur_d == distance[cur_v][0]:
      distance[cur_v][1] += 1
    else:
      distance[cur_v]= [cur_d,0]
    
    heapq.heappush(queue,(cur_d+1,cur_v+1))
    heapq.heappush(queue,(cur_d+1,cur_v-1))
    heapq.heappush(queue,(cur_d+1,2*cur_v))
  return distance

subin,sister = map(int,input().split())
print(dijkstra(subin)[sister][0])
print(dijkstra(subin)[sister][1]+1)
import sys ,heapq
input = sys.stdin.readline

def dijkstra(start):
  distance = [[float('inf'),0]]*100001
  queue= [(0,start,0)]
  while queue:
    cur_d,cur_v,prev_v = heapq.heappop(queue)
    if cur_v < 0 or cur_v >100000:
      continue

    if cur_d >= distance[cur_v][0]:
      continue
    else:
      distance[cur_v]= [cur_d,prev_v]
      heapq.heappush(queue,(cur_d+1,cur_v+1,cur_v))
      heapq.heappush(queue,(cur_d+1,cur_v-1,cur_v))
      heapq.heappush(queue,(cur_d+1,2*cur_v,cur_v))
  return distance

subin,sister = map(int,input().split())
if subin == sister:
  print(0)
  print(subin)
else:
  answer = dijkstra(subin)
  print(answer[sister][0])
  tmp = answer[sister][1]
  stack = [sister]
  while tmp != subin: 
    stack.append(tmp)
    tmp = answer[tmp][1]
  stack.append(subin)
  while stack:
    print(stack.pop(),end=' ')
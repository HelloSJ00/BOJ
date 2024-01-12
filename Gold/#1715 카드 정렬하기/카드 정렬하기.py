import sys , heapq
input = sys.stdin.readline

N = int(input())
heap = []
anwser = 0
compare = 0
for _ in range(N):
    heapq.heappush(heap,int(input()))

while heap:
    if len(heap) == 1:
        anwser+heapq.heappop(heap)
    else:
        compare = heapq.heappop(heap) + heapq.heappop(heap)
        anwser += compare
        heapq.heappush(heap,compare)

print(anwser)
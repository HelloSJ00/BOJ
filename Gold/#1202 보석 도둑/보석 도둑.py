import sys,heapq
input = sys.stdin.readline

N,K = map(int,input().split())

items = []
for _ in range(N):
	weight,value = map(int,input().split())
	heapq.heappush(items,(weight,-value))

bags = []
for _ in range(K):
	bags.append(int(input().rstrip()))
bags.sort()
answer = 0

tmp_items = []
for bag in bags:
	while items and items[0][0] <= bag :
		heapq.heappush(tmp_items,heapq.heappop(items)[1])

	if tmp_items:
		answer -= heapq.heappop(tmp_items)

print(answer)
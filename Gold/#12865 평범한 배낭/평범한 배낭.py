import sys,heapq
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
items = []
for _ in range(N):
	items.append(tuple(map(int,input().split())))

DP = [[0]*(K+1) for _ in range(N+1)]

for y in range(1,N+1):
	for x in range(1,K+1):
		if items[y-1][0] <= x:
				DP[y][x] = max(DP[y-1][x],items[y-1][1]+DP[y-1][x-items[y-1][0]])
		else:
			DP[y][x] = max(DP[y][x-1],DP[y-1][x])
# print(DP)
answer = 0
for i in range(1,N+1):
	answer = max(answer,DP[i][K])
print(answer)
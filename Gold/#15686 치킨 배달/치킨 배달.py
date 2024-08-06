import sys,heapq
from collections import deque
import itertools
input = sys.stdin.readline

def chicken_delivery(y,x,arr):
	dy=[0,-1,0,1]
	dx=[-1,0,1,0]
	visit = [[0]*N for _ in range(N)]
	queue = deque([(y,x,0)])
	while queue:
		cy,cx,cnt = queue.popleft()
		if (arr[cy][cx] > cnt and graph[cy][cx] == 1) or (arr[cy][cx] == 0 and graph[cy][cx]==1):
			arr[cy][cx] = cnt

		for i in range(4):
			ny,nx = cy+dy[i],cx+dx[i]
			if 0<= ny < N and 0 <= nx < N and visit[ny][nx]==0:
				visit[ny][nx] = 1
				queue.append((ny,nx,cnt+1))

N, M = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
chicken_house = []

for y in range(N):
	for x in range(N):
		if graph[y][x] == 2:
			chicken_house.append((y,x))

all_case = list(itertools.combinations(chicken_house,M))
# print(all_case)
final_sum = float('inf')
for i in all_case:
	answer = [[0]*N for _ in range(N)]
	sum = 0
	for j in i:
		chicken_delivery(j[0],j[1],answer)
		# print(answer)
	for y in range(N):
		for x in range(N):
			if answer[y][x] != 0:
				sum += answer[y][x]

	final_sum = min(final_sum,sum)
print(final_sum)
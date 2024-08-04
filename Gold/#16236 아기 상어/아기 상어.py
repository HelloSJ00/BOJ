import sys,heapq
from collections import deque
input = sys.stdin.readline

def baby_shark(y,x):
	dy = [0,-1,0,1]
	dx = [-1,0,1,0]
	toMove=[21,21,float('inf')]
	visit = [[0]*N for _ in range(N)]
	queue = deque([(y,x,0)])
	while queue:
		# print(queue)
		cy,cx,cur_cnt = queue.popleft()
		for i in range(4):
			ny,nx = cy+dy[i],cx+dx[i]
			if 0<= ny < N and 0<= nx < N:
				if graph[ny][nx] > graph[y][x] or visit[ny][nx]==1:
					continue

				elif (graph[ny][nx] == graph[y][x]) or graph[ny][nx] == 0 :
					visit[ny][nx] = 1
					queue.append((ny,nx,cur_cnt+1))
				
				elif graph[ny][nx] < graph[y][x]:
					if toMove[2] > cur_cnt+1:
						toMove = [ny,nx,cur_cnt+1]
					elif toMove[2] == cur_cnt+1:
						if toMove[0] > ny:
							toMove = [ny,nx,cur_cnt+1]
						elif toMove[0] == ny:
							if toMove[1] > nx:
								toMove = [ny,nx,cur_cnt+1]
	return toMove
	
N = int(input().rstrip())
graph = [list(map(int,input().split())) for _ in range(N)]
shark = [0,0]
# 상어를 2로 
for y in range(N):
	for x in range(N):
		if graph[y][x] == 9:
			graph[y][x] = 2
			shark = [y,x]
answer = 0
shark_size = 2
shark_eating = 2
while True:
	nextMoveAndCnt = baby_shark(shark[0],shark[1])
	# print('y->',nextMoveAndCnt[0],'x->',nextMoveAndCnt[1])
	# 종료조건 (엄마상어 호출)
	if nextMoveAndCnt[2] == float('inf'):
		break
	graph[shark[0]][shark[1]] = 0
	shark = [nextMoveAndCnt[0],nextMoveAndCnt[1]]
	answer += nextMoveAndCnt[2]
	shark_eating -=1
	if shark_eating == 0:
		shark_size +=1
		shark_eating = shark_size
	graph[nextMoveAndCnt[0]][nextMoveAndCnt[1]] = shark_size

print(answer)
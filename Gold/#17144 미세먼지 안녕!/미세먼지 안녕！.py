import sys,heapq
from collections import deque
input = sys.stdin.readline

def  spread(y,x,arr):
	dy = [0,-1,0,1]
	dx = [-1,0,1,0]

	tmp = arr[y][x][0]//5

	for i in range(4):
		ny,nx = y+dy[i],x+dx[i]
		if (0<= ny < R and 0<= nx < C) and origin_map[ny][nx][0] != -1 :
			arr[y][x][0] -= tmp
			arr[ny][nx][1] += tmp

def transaction(arr):
	new_map = [[[0,0] for _ in range(C)] for _ in range(R)]
	for y in range(R):
		for x in range(C):
			if arr[y][x][0] != 0 and arr[y][x][0] != -1:
				spread(y,x,arr)
	
	for y in range(R):
		for x in range(C):
			arr[y][x][0] += arr[y][x][1]
			arr[y][x][1] = 0

	for y in range(R):
		for x in range(C):
			if arr[y][x][0] != -1:
				if x == 0 and  0 <= y < air_fresher[0]: # 아래로
					if y != air_fresher[0]-1:
						new_map[y+1][x] = arr[y][x]
				elif x != 0 and y == 0 : # 왼쪽으로 
					new_map[y][x-1] = arr[y][x]
				elif 0< y <= air_fresher[0] and x == C-1: # 위로 
					new_map[y-1][x] = arr[y][x] 
				elif y == air_fresher[0] and x != C-1: # 오른쪽으로
					new_map[y][x+1] = arr[y][x]
				elif x == 0 and  air_fresher[1] < y <= R-1: # 위로 
					if y != air_fresher[1] +1 :
						new_map[y-1][x] = arr[y][x]
				elif  x != C-1 and y == air_fresher[1] : #오른쪽으로 
					new_map[y][x+1] = arr[y][x]
				elif air_fresher[1] <= y < R-1 and x == C-1: # 아래로
					new_map[y+1][x] = arr[y][x]
				elif  y == R-1 and x != 0: # 왼쪽으로 
					new_map[y][x-1] = arr[y][x]
				else:
					new_map[y][x]=arr[y][x]
			else:
				new_map[y][x] = arr[y][x]
	return new_map

R,C,T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]

origin_map = [[[0,0] for _ in range(C)] for _ in range(R)]
air_fresher =[]
for y in range(R):
	for x in range(C):
		origin_map[y][x] = [room[y][x],0]
		if origin_map[y][x][0] == -1:
			air_fresher.append(y)
# print(air_fresher)
# for y in range(R):
# 	for x in range(C):
# 		print(origin_map[y][x][0],end=' ')
# 	print()
# new = transaction(origin_map)
# print('-----')
# for y in range(R):
# 	for x in range(C):
# 		print(new[y][x][0],end=' ')
# 	print()

for _ in range(T):
	origin_map = transaction(origin_map)

# for y in range(R):
# 	for x in range(C):
# 		print(origin_map[y][x][0],end=' ')
# 	print()
answer = 0
for y in range(R):
	for x in range(C):	
		if origin_map[y][x][0] != -1:
			answer += origin_map[y][x][0]
print(answer)
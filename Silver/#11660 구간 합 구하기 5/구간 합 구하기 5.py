import sys
input = sys.stdin.readline

arr = [[0]*1025 for _ in range(1025)]

N,M = map(int,input().split())
for y in range(1,N+1):
	tmp= list(map(int,input().split()))
	for x in range(1,N+1):
		arr[y][x] = tmp[x-1]
# for y in range(N+1):
# 	print(arr[y][:5])
for y in range(N+1):
	for x in range(N+1):
		arr[y][x] += arr[y-1][x] + arr[y][x-1] - arr[y-1][x-1]

# for y in range(N+1):
# 	print(arr[y][:N+1])

for _ in range(M):
	x1,y1,x2,y2 = map(int,input().split())
	x_right = max(x1,x2)
	x_left = min(x1,x2)
	y_down = max(y1,y2)
	y_up = min(y1,y2)
	print(arr[x_right][y_down] - arr[x_left-1][y_down] - arr[x_right][y_up-1] + arr[x_left-1][y_up-1])
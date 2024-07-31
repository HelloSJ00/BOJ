import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().split()))
answer = 0

front = [1]*N
back = [1]*N

for i in range(1,len(arr)):
	for prev_idx in range(i):
		if arr[prev_idx] < arr[i]:
			front[i] = max(front[i],front[prev_idx]+1)

for i in range(len(arr)-1,-1,-1):
	for prev_idx in range(len(arr)-1,i,-1):
		if arr[prev_idx] < arr[i]:
			back[i] = max(back[i],back[prev_idx]+1)

for k in range(len(arr)):
	answer = max(answer,front[k]+back[k]-1)
print(answer)
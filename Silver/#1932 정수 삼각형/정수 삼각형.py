import sys
input = sys.stdin.readline

DP = [[] for _ in range(501)]
N = int(input().rstrip())
for i in range(1,N+1):
	DP[i] = list(map(int,input().split()))
for floor in range(2,N+1):
	for idx in range(floor):
		if idx == 0:
			DP[floor][idx] += DP[floor-1][idx]
		elif idx == floor -1:
			DP[floor][idx] += DP[floor-1][idx-1]
		else:
			DP[floor][idx] += max(DP[floor-1][idx-1],DP[floor-1][idx])

print(max(DP[N]))



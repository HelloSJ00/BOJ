import sys
input = sys.stdin.readline

N = int(input().rstrip())
DP= [[0,0],[0,0],[0,0]]
for i in range(N):
	max_prev_a = DP[0][0]
	max_prev_b = DP[1][0]
	max_prev_c = DP[2][0]
	min_prev_a = DP[0][1]
	min_prev_b = DP[1][1]
	min_prev_c = DP[2][1]
	a,b,c= map(int,input().split())
	DP[0][0] = max(max_prev_a,max_prev_b) + a
	DP[1][0] = max(max_prev_a,max_prev_b,max_prev_c) +b
	DP[2][0] = max(max_prev_b,max_prev_c) + c

	DP[0][1] = min(min_prev_a,min_prev_b) + a
	DP[1][1] = min(min_prev_a,min_prev_b,min_prev_c) + b
	DP[2][1] = min(min_prev_b,min_prev_c) + c

print(max(DP,key= lambda x : x[0])[0],end=' ')
print(min(DP,key=lambda x : x[1])[1])
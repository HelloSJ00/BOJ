import sys
input = sys.stdin.readline

N = int(input()) #포도주 잔의 개수
grapes = [0]*10001
dp=[0]*10001

for i in range(N):
    grapes[i+1]=int(input())

dp[1] = grapes[1]
dp[2] = grapes[1]+grapes[2]
for i in range(3,N+1):
    dp[i] = max(dp[i-1],dp[i-2]+grapes[i],dp[i-3]+grapes[i-1]+grapes[i])

print(dp[N])


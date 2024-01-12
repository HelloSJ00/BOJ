# 이친수

import sys
input = sys.stdin.readline

dp = [[0]*2 for i in range(91)]
dp[1] = [0,1]
dp[2] = [1,0]
dp[3] = [1,1]

for i in range(4,91):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][1]+ dp[i-1][0]
N = int(input())

print(dp[N][0]+dp[N][1])
        


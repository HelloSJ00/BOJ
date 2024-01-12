# 1,2,3 더하기

import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    dp = [0]* 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    n = int(input())
    if n>3:
        for i in range(4,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])


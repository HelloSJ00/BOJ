# 카드 구매하기

import sys
input = sys.stdin.readline



N = int(input())
howMuchCard = list(map(int,input().split()))

dp = [0]*(N+1)
dp[1] = howMuchCard[0]
for i in range(2,N+1):
    tmp = howMuchCard[i-1]
    for j in range(1,i//2+1):
        if tmp < dp[i-j]+dp[j]:
            tmp = dp[i-j]+dp[j]
    dp[i]=tmp
print(dp[N])






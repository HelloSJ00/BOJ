# 쉬운계단 수
import sys
input = sys.stdin.readline

dp=[[0]*10 for i in range(102)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,102):
    for j in range(10):
        if j == 0:
            dp[i][j] = (dp[i-1][j+1])%1000000000
        elif j == 9:
            dp[i][j] = (dp[i-1][j-1])%1000000000
        else:
            dp[i][j] = (dp[i-1][j-1]+ dp[i-1][j+1])%1000000000

N = int(input())
anwser = 0
for i in range(10):
    anwser += dp[N][i]

print(anwser%1000000000)
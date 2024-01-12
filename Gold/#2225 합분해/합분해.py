import sys
input = sys.stdin.readline

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num*factorial(num-1)
    
# def combination(num,k):
#     return (factorial(num)//(factorial(num-k)*factorial(k)))
# dp = [0]*200 # K가 1일때부터 천천히 올라간다.

# N,K = map(int,input().split()) 

# dp[1] = 1

# for i in range(2,K+1):
#     dp[i] = combination(N-1,i-1)

# anwser = 0
# for i in range(1,K+1):
#     anwser += (dp[i]*(combination(K,K-i)))

# print(anwser%1000000000)


dp = [[0 for _ in range(201)] for _ in range(201)]
N,K = map(int,input().split()) 
dp[0] = [1 for _ in range(201)]
dp[0][0] = 0

for i in range(1,N+1):
    for j in range(1,K+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000

print(dp[N][K])
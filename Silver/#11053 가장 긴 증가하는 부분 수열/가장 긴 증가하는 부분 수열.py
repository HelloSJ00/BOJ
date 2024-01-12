# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

# N = int(input()) # 수열의 길이
# length = [1]*N
# numList = list(map(int,input().split()))

# for i in range(N):
#     orderNum = numList[i]
#     cnt=1
#     for j in range(i,N):
#         if orderNum < numList[j]:
#             orderNum = numList[j]
#             cnt+=1
#     length[i] = cnt

# for i in range(1,N):
#     for j in range(i):
#         if numList[i] < numList[j]:
#             length[i] = max(length[i],length[j]+1)

# print(max(length))

n = int(input())
arr = list(map(int, input().split()))

# dp 테이블 1로 초기화
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
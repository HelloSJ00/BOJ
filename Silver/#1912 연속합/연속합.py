# 연속합 

import sys
input = sys.stdin.readline

# N = int(input())
# numList = list(map(int,input().split()))

# dp  = [(-1000)*N]*(N+1)

# for i in range(1,N+1):
    
#     for k in range(N-i):
#         sum = 0
#         for q in range(i): 
#             sum += numList[k+q]
        
#         if sum > dp[i]:
#             dp[i] = sum
        
#         k += 1

# print(max(dp))

# def lcs(nums):
#     curr = 0
#     best = -10**8
#     for num in nums:
#         curr = max(curr+num, num)
#         best = max(best, curr)
    
#     return best

# for i in range(N):
#     nums = numList[i:N]
#     dp[i] = lcs(nums)

# print(max(dp))

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] = max(data[i], data[i] + data[i-1])
  
print(max(data))
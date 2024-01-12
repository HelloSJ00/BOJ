import sys
input = sys.stdin.readline

N = int(input()) # 수열의 길이

nums = [0]*1001
dp = [[0, []] for _ in range(1001)]  # 각각 독립적인 리스트 생성
nums[1:N+1] = map(int,input().split())
for i in range(N+1):
    for j in range(i):
      if nums[i] > nums[j]:
         if dp[i][0] <= dp[j][0]+1: # max(dp[i],dp[j]+1) 변형 
            dp[i][0] = dp[j][0] +1 # 가장 긴 증가하는 수열 길이
            dp[i][1] = dp[j][1][:]  # 이전 수열 복사
            dp[i][1].append(i)  # 현재 값 추가

anwser = dp[0]
for i in range(N+1):
   if dp[i][0] > anwser[0]:
      anwser = dp[i]
print(anwser[0])
for i in range(len(anwser[1])):
   print(nums[anwser[1][i]],end=" ")
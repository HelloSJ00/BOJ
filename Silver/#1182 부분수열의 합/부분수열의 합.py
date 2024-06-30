import sys
input = sys.stdin.readline

# 시간제한 2초 , 입력제한 1~20 , |S| <=1,000,000  
def dfs(idx,sum):
  global answer
  if idx >= N : return
  sum += arr[idx]
  if M == sum : answer +=1
  dfs(idx+1,sum-arr[idx])
  dfs(idx+1,sum)

# 입력
N,M = map(int,(input().split()))
arr=list(map(int,input().split()))
answer = 0
dfs(0,0)
print(answer)



import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [0] 
for _ in range(N):
  arr.append(int(input().rstrip()))
DP = [0]*301

def dpToResult(target):
  if target == 1:
    return arr[1]
  elif target == 2:
    return arr[2]+arr[1]
  else:
    DP[1] = arr[1]
    DP[2] = DP[1]+arr[2]
    DP[3] = max(arr[1]+arr[3],arr[2]+arr[3])
    for i in range(3,target+1):
      DP[i] = max(DP[i-3]+arr[i-1]+arr[i],DP[i-2]+arr[i])
  return DP[target]

print(dpToResult(N))
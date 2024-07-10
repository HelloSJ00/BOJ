import sys
input = sys.stdin.readline

# 입력
arr1 = list(input().rstrip())
arr2 = list(input().rstrip())

# print(arr1,arr2)
DP = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1,len(arr1)+1):
  for j in range(1,len(arr2)+1):
    if arr1[i-1] == arr2[j-1]:
      DP[i][j] = DP[i-1][j-1] + 1
    else:
      DP[i][j] = max(DP[i][j-1],DP[i-1][j])
print(DP[len(arr1)][len(arr2)])
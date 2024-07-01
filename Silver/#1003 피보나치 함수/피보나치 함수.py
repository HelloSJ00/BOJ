import sys

input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
    DP = [[1,0],[0,1]]
    num = int(input())
    if num <= 1:
      print(*DP[num])
    else:
      for i in range(num):
          DP.append([DP[i][0]+DP[i+1][0],DP[i][1]+DP[i+1][1]])
      print(*DP[num])
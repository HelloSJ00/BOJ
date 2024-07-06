import sys
input = sys.stdin.readline

arr = [0 for _ in range(20000001)]
# 입력 시간제한 1초 
N = int(input().rstrip())
arr_N = list(map(int,input().split()))
for i in arr_N:
  i += 10000000
  arr[i] +=1

M = int(input().rstrip())
arr_M = list(map(int,input().split()))
for i in arr_M:
  i += 10000000
  print(arr[i],end=' ')
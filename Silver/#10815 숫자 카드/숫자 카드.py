import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
arr1 = list(map(int,input().split()))
M = int(input().rstrip())
arr2 = list(map(int,input().split()))

# 이분 탐색을 위한 소트
arr1.sort()
def search(s,e,d,arr):
  while s <= e:
    m = (s+e)//2
    if arr[m] == d:
      return 1
    if arr[m] > d:
      e = m-1
    elif arr[m] < d:
      s = m+1
  return 0
    
for i in arr2:
  print(search(0,len(arr1)-1,i,arr1),end=' ')
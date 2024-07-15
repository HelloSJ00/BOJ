import sys
input = sys.stdin.readline

def search(s,e):
    mid = (s+e)//2
    if e < s:
      return mid
    sum = 0

    for i in arr:
      if i - mid > 0:
        sum += (i-mid)
    if sum > M:
      s = mid +1
      return search(s,e)
    elif sum < M:
      e = mid -1
      return search(s,e)
    else:
      return mid

# 입력
N , M = map(int,input().split())
arr = list(map(int,input().split()))

print(search(0,max(arr)))



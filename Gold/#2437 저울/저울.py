import sys
input = sys.stdin.readline
# 시간제한 2초 

# 입력
N = int(input().rstrip())
arr = list(map(int,input().split()))
arr.sort() # O(nlogn)

answer = 1
for i in arr:
  if answer < i:
    break
  answer+=i

print(answer)
import sys
input=sys.stdin.readline

# 입력
N, M = map(int,input().split())
arr= list(map(int,input().split()))
num =[0] * 10001
for i in arr:
  num[i] = 1

arr.sort()
answer = []

# 로직
# 출력
def bt(depth):
  if depth == M:
    print(*answer)
  for i in arr:
    if num[i] == 0:
      continue
    
    answer.append(i)
    num[i] = 0
    bt(depth+1)
    answer.pop()
    num[i] = 1

bt(0)





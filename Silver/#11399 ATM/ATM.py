import sys
input = sys.stdin.readline
# 시간제한 1초 
answer = 0
#입력 
people = int(input().rstrip())
wating = list(map(int,input().split()))

wating.sort()
for i in range(people-1):
  wating[i+1] = wating[i] + wating[i+1]
  answer += wating[i]

answer += wating[-1]
print(answer)

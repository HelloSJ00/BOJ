import sys
input = sys.stdin.readline
# 시간제한 2초 N,M 500,000 이하 O(n) 이하로 해결

dic= {}
cnt = 0
answer=[]
#입력 
N,M = map(int,input().split())

#출력
for _ in range(N):
  dic[input().rstrip()] = True

for _ in range(M):
  tmp = input().strip()
  if tmp in dic:
    answer.append(tmp)
    cnt +=1
  
answer.sort()
print(cnt)
for i in range(len(answer)):
  print(answer[i])

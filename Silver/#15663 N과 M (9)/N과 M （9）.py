import sys
input = sys.stdin.readline

def bt(cnt,answer):
  string=''
  for i in answer:
    string += ','
    string += f'{i}'

  if cnt == 0 :
    if string not in dic:
      print(*answer)
      dic[string]=True
    return

  for i in range(N):
    if visit[i] != 1:
      answer.append(arr[i])
      visit[i] = 1
      bt(cnt-1,answer)
      answer.pop()
      visit[i] = 0

# 입력
N,M= map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit = [0]*N
dic = {}
answer=[]

bt(M,answer)

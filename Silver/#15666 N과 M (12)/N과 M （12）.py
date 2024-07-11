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
    if answer and answer[-1] <= arr[i]:
      answer.append(arr[i])
      bt(cnt-1,answer)
      answer.pop()
    elif answer == []:
      answer.append(arr[i])
      bt(cnt-1,answer)
      answer.pop()

# 입력
N,M= map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
dic = {}
answer=[]

bt(M,answer)

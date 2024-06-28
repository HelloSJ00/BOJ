import sys
input = sys.stdin.readline

# 시간제한 1초 , 입력제한 2~100  
# 입력
N,M = map(int,input().split())
miro = []
for _ in range(N):
  miro.append(list(map(int,input().strip())))

answer = [[0 for _ in range(M)] for _ in range(N)]
queue = []

i,j = 0,0
answer[i][j]=1
queue.append([0,0])

while True:
  # 출력
  if answer[N-1][M-1] != 0:
    print(answer[N-1][M-1])
    break

  i = queue[0][0]
  j = queue[0][1]
  queue.pop(0)

  # 상
  if i-1 >= 0 and answer[i-1][j] == 0 and miro[i-1][j] == 1: 
    queue.append([i-1,j])
    answer[i-1][j] = answer[i][j]+1

  # 하
  if i+1 < N and answer[i+1][j] == 0 and miro[i+1][j] == 1:
    queue.append([i+1,j])
    answer[i+1][j] = answer[i][j]+1

  # 좌
  if j-1 >=0 and answer[i][j-1] == 0 and miro[i][j-1] == 1:
    queue.append([i,j-1])
    answer[i][j-1] = answer[i][j]+1

  # 우
  if j+1 <= M-1 and answer[i][j+1] == 0 and miro[i][j+1] == 1:
    queue.append([i,j+1])
    answer[i][j+1] = answer[i][j]+1
import sys
input = sys.stdin.readline

# 시간제한 2초 , 입력제한 4~500 시간복잡도 O(n^3) 까지 가능
#입력
N, M = map(int,input().split())
inputTable = []
for _ in range(N):
  inputTable.append(list(map(int,input().split())))

anwser = []
col = 0
row = 0
for col in range(N):
  for row in range(M):  
    # 시작지점
    start = inputTable[col][row]
    # 1
    if col + 3 < N:
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col+3][row]))
    # 2
    if row + 3 < M:
      anwser.append(start+(inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col][row+3]))

    if (col + 2 < N) and (row +1 < M):
    # 3
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col][row+1]))
    # 4
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col+1][row+1]))
    # 5
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col+2][row+1]))
    # 6
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+1][row+1]+inputTable[col+2][row+1]))
    # 7
      anwser.append(start+(inputTable[col][row+1]+inputTable[col+1][row+1]+inputTable[col+2][row+1]))
    
    if (col + 1 < N) and (row +2 < M):
    # 8
      anwser.append(start+(inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col+1][row]))
    # 9
      anwser.append(start+(inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col+1][row+1]))
    # 10
      anwser.append(start+inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col+1][row+2])
    # 11
      anwser.append(start+(inputTable[col+1][row+1]+inputTable[col+1][row+2]+inputTable[col+1][row]))
    # 12
      anwser.append(start+(inputTable[col][row+1]+inputTable[col+1][row+1]+inputTable[col+1][row+2]))

    # 13
    if (col + 1 < N) and (row + 1 < M):
      anwser.append(start+(inputTable[col][row+1]+inputTable[col+1][row]+inputTable[col+1][row+1]))

    if (col + 2 < N) and (row - 1 >= 0):
      # 14
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col+1][row-1]))
      # 15
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row]+inputTable[col+2][row-1]))
      # 16
      anwser.append(start+(inputTable[col+1][row]+inputTable[col+2][row-1]+inputTable[col+1][row-1]))
    if (col - 1 >= 0) and (row + 2 < M):
      # 17
      anwser.append(start+(inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col-1][row+1]))
      # 18
      anwser.append(start+(inputTable[col][row+1]+inputTable[col][row+2]+inputTable[col-1][row+2]))
      # 19
      anwser.append(start+(inputTable[col][row+1]+inputTable[col-1][row+2]+inputTable[col-1][row+1]))


print(max(anwser))
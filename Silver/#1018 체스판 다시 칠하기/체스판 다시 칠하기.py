import sys
input = sys.stdin.readline

#시간 복잡도를  
#입력
N ,M= map(int,input().split())
inputTable = []
for _ in range(N):
  inputTable.append(input())

#출력
anwser = []

for col in range(N-7):
  for row in range(M-7):
    countW = 0
    countB = 0
    for i in range(col,col+8):
      for j in range(row,row+8):
        if (i+j)%2 == 0:
          if inputTable[i][j] != 'W':
            countW +=1
          if inputTable[i][j] != 'B':
            countB +=1
        else:
          if inputTable[i][j] != 'B':
            countW +=1
          if inputTable[i][j] != 'W':
            countB +=1
    anwser.append(countW)
    anwser.append(countB)
print(min(anwser))
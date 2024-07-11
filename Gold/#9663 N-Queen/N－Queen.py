import sys
input = sys.stdin.readline

def backTracking(y,cnt):
  global answer

  if cnt == 0:
    answer +=1
    return
  
  # 백트래킹
  for i in range(1,N+1):
    if chess_board[y+1][i] == 0:
      # 로직
      for j in range(1,N+1):
        # 가로 세로 +=1
        chess_board[y+1][j]+=1
        chess_board[j][i]+=1
        # 대각선 +=1
        if 0< (y+1+j) <N+1 and 0< (i+j) <N+1:
          chess_board[y+1+j][i+j] += 1
        if 0< (y+1+j) <N+1 and 0< (i-j) <N+1:
          chess_board[y+1+j][i-j] += 1
        if 0< (y+1-j) <N+1 and 0< (i+j) <N+1:
          chess_board[y+1-j][i+j] += 1
        if 0< (y+1-j) <N+1 and 0< (i-j) <N+1:
          chess_board[y+1-j][i-j] += 1
      backTracking(y+1,cnt-1)
      for j in range(1,N+1):
        # 가로 세로 -=1
        chess_board[y+1][j]-=1
        chess_board[j][i]-=1
        # 대각선 -=1
        if 0< (y+1+j) <N+1 and 0< (i+j) <N+1:
          chess_board[y+1+j][i+j] -= 1
        if 0< (y+1+j) <N+1 and 0< (i-j) <N+1:
          chess_board[y+1+j][i-j] -= 1
        if 0< (y+1-j) <N+1 and 0< (i+j) <N+1:
          chess_board[y+1-j][i+j] -= 1
        if 0< (y+1-j) <N+1 and 0< (i-j) <N+1:
          chess_board[y+1-j][i-j] -= 1


# 입력
N = int(input().rstrip())
cnt = N
chess_board = [[0]*(N+1) for _ in range(N+1)]
# print(chess_board)
answer = 0

backTracking(0,N)
print(answer)
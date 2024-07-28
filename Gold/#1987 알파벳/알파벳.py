import sys
input = sys.stdin.readline

alreadyVisit=set()
dy = [0,-1,0,1]
dx = [-1,0,1,0]

def board_game_dfs(board,y,x,cnt):
	global answer
	if board[y][x] in alreadyVisit:
		answer = max(answer,cnt)
	else:
		alreadyVisit.add(board[y][x])
		for i in range(4):
			if 0 <= y+dy[i] < R and 0 <= x + dx[i] < C:
				board_game_dfs(board,y+dy[i],x + dx[i],cnt+1)
		alreadyVisit.remove(board[y][x])

R,C = map(int,input().split())
board = []
for _ in range(R):
	board.append(list(input().rstrip()))
answer = 1
board_game_dfs(board,0,0,0)
print(answer)
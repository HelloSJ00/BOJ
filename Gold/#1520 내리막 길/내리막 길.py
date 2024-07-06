import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    if x == N-1 and y == M-1:  # 목표 지점에 도달한 경우
        return 1
    if dp[x][y] != -1:  # 이미 계산된 경우
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and Map[x][y] > Map[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

# 입력
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

# 결과 출력
print(dfs(0, 0))


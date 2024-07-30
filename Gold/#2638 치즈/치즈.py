import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def update_external_air(y, x, air):
    queue = deque([(y, x)])
    while queue:
        cur_y, cur_x = queue.popleft()
        air[cur_y][cur_x] = 2
        for i in range(4):
            ny, nx = cur_y + dy[i], cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and air[ny][nx] == 0:
                    air[ny][nx] = 2
                    queue.append((ny, nx))

def melt_cheese(air):
    melting_cheese = []
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                air_cnt = 0
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and air[ny][nx] == 2:
                        air_cnt += 1
                if air_cnt >= 2:
                    melting_cheese.append((y, x))
    return melting_cheese

cur_air = [[0] * M for _ in range(N)]
update_external_air(0, 0, cur_air)

while True:
    melting_cheese = melt_cheese(cur_air)
    
    if not melting_cheese:
        break

    for y, x in melting_cheese:
        graph[y][x] = 0
        update_external_air(y, x, cur_air)
    
    answer += 1

print(answer)

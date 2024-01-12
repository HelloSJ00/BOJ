import sys
from collections import deque

N = int(sys.stdin.readline()) # N X N 보드의 크기
K = int(sys.stdin.readline()) # 사과의 개수

apple = {} # 사과의 위치
for i in range(K):
    apple[tuple(map(int,sys.stdin.readline().split()))] = True

direction_change = []
L = int(sys.stdin.readline()) # 방향 변환 횟수
for i in range(L):
    direction_change.append(list(sys.stdin.readline().split()))

body = deque([[1,1]]) # 뱀의 몸통
map = [[0 for _ in range(N+1)] for _ in range(N+1)] # N X N 맵 , 코드를 간결하게 하기위해 N+1 X N+1 맵 만듬.

map[1][1] = 1 # 뱀의 시작위치
head_position = [1,1] # 뱀의 머리위치
STATE = 0 # 0은 Live, 1 = death
direction = 0 # 0 오른쪽 ,1 아래쪽, 2 왼쪽, 3 위쪽
cnt = 0 # 몇초가 지났는지 카운트
direct_cnt = 0 # 방향전환 카운트

while STATE == 0:

    # 첫번째 움직임
    if direction == 0:
        head_position[1] +=1
    elif direction == 1:
        head_position[0] +=1    
    elif direction == 2:
        head_position[1] -=1
    elif direction == 3:
        head_position[0] -=1

    # 사망조건 1
    if head_position[0] > N or head_position[0] < 1 or head_position[1] > N or head_position[1] < 1:
        STATE = 1 # 뱀의 머리가 벽에 부딪친다면 사망
        cnt+=1
        break

    # 사망조건 2
    if map[head_position[0]][head_position[1]] == 1:
        STATE = 1 # 움직인 위치에 몸이 있다면 사망
        cnt +=1
        break

    else: # 머리 위치 큐에 추가
        body.append(list(head_position))
        map[head_position[0]][head_position[1]] = 1 # 맵에 몸 표시.

    tuple = (head_position[0],head_position[1])

    if tuple not in apple : # 움직인 자리에 사과가 없다면.
        trace = body.popleft()
        map[trace[0]][trace[1]] = 0 
        
    else: # 사과치우기
        del apple[tuple]
    
    cnt +=1 # 1초 추가

    if direct_cnt < len(direction_change) and int(direction_change[direct_cnt][0]) == cnt:
        if direction_change[direct_cnt][1] == 'D':
            direction = (direction + 1) % 4
        elif direction_change[direct_cnt][1] == 'L':
            direction = (direction - 1) % 4
        direct_cnt += 1

    # for i in direction_change: # 방향 전환
    #     if int(i[0]) == cnt:
    #         if i[1] == 'D':
    #             direction +=1
    #             if direction == 4:
    #                 direction = 0
    #         if i[1] == 'L':
    #             direction -=1
    #             if direction == -1:
    #                 direction = 4

print(cnt)
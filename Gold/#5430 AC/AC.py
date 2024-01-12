# 큐 AC 

import collections
import sys, copy

TC = int(sys.stdin.readline())

for _ in range(TC):
    command = list(sys.stdin.readline().rstrip()) # 명령어 배열
    N = int(sys.stdin.readline()) # 배열에 들어있는 수의 개수
    K = sys.stdin.readline().rstrip()
    if K != '[]':
        _list = list(map(int,K[1:-1].split(',')))
    else:
        _list = []
    _list = collections.deque(_list)

    Rvalue = 0 # 0은 정방향 1은 역방향
    cmd_cnt = 0 # 명령어 위치

    while(len(command) != cmd_cnt):
        if command[cmd_cnt] == 'R': # Reverse
            if Rvalue == 0:
                Rvalue =1 # 정방향이면 역방향으로
            else:
                Rvalue =0 # 역방향이면 정방향으로
            cmd_cnt +=1
        elif command[cmd_cnt] == 'D': # Pop
            if N == 0:
                print('error')
                break

            if Rvalue ==1 : # 역방향이라면 뒤에서 pop
                _list.pop()
                cmd_cnt +=1
                N-=1
            if Rvalue == 0: #  정방향이라면 앞에서 pop
                _list.popleft()
                cmd_cnt +=1
                N-=1

    anwser = [] # 출력 배열

    if len(command) == cmd_cnt:
        if len(_list) == 0:
            print(anwser)
        else:
            for i in _list:
                anwser.append((i))

            if Rvalue ==1 : # 역방향이면 뒤집어서 출력
                _list.reverse()
                    
            print('[',end='')
            for i in range(len(_list)):
                print(_list[i],end='')
                if i != len(_list)-1:
                    print(',',end='')
            print(']')


# 쇠막대기

import sys
input = sys.stdin.readline
_string = list(input().rstrip())

piece = []
pieceCnt = 0 # 조각 개수
raser = 0 # 레이저 개수
valueConst = 0 # '(' == 1, ')'== -1

for i in _string:
    if len(piece) == 0:
        raser = 0

    if i == '(':
        if valueConst == 1:
            piece.append(1-raser)    

        valueConst = 1

    elif i == ')':
        if valueConst == 1:
            raser +=1
        elif valueConst == -1:
            pieceCnt += (piece.pop()+raser)

        valueConst = -1

print(pieceCnt)
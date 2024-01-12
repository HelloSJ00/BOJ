# 후위표기식 2

import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
_string = deque(list(input()))
operand = deque([])

Eng = {'A': None,
       'B':None,
       'C':None,
       'D':None,
       'E':None,
       'F':None,
       'G':None,
       'H':None,
       'I':None,
       'J':None,
       'K':None,
       'L':None,
       'M':None,
       'N':None,
       'O':None,
       'P':None,
       'Q':None,
       'R':None,
       'S':None,
       'T':None,
       'U':None,
       'V':None,
       'W':None,
       'Y':None,
       'X':None,
       'Z':None,}


while _string:
    if _string[0] in Eng and Eng[_string[0]] is None:
        Eng[_string[0]] = int(input())
        operand.append(Eng[_string.popleft()])
        
    elif _string[0] in Eng and Eng[_string[0]] is not None:
        operand.append(Eng[_string.popleft()])
    else :
        if _string[0] == '*':
            num1 = operand.pop()
            num2 = operand.pop()
            operand.append(num2 * num1)

        elif _string[0] == '+':
            num1 = operand.pop()
            num2 = operand.pop()
            operand.append(num2 + num1)

        elif _string[0] == '-':
            num1 = operand.pop()
            num2 = operand.pop()
            operand.append( num2 - num1)

        elif _string[0] == '/':
            num1 = operand.pop()
            num2 = operand.pop()
            operand.append( num2 / num1)
        _string.popleft()

print('%.2f'%(operand[0]))

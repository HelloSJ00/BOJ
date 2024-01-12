#후위표기식

import sys
from collections import deque
input = sys.stdin.readline
operator = { # 연산자
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':'(',
    ')':')'
}

_string = (list(input().rstrip()))
operation = []
result = []

for i in _string:
    if i not in operator:
        result.append(i)

    else:
        if i == '(':
            operation.append(i)
        elif i == '*' or i == '/':
            while operation and (operation[-1] == '*' or operation[-1] == '/'):
                result.append(operation.pop())
            operation.append(i)
        elif i == '+' or i == '-':
            while operation and (operation[-1] != '('):
                result.append(operation.pop())
            operation.append(i)
        elif i == ')':
            while operation and operation[-1] != '(':
                result.append(operation.pop())
            operation.pop()
while operation:
    result.append(operation.pop())

for i in range(len(result)):
    if i != (len(result)-1):
        print(result[i],end='')
    else: 
        print(result[i])








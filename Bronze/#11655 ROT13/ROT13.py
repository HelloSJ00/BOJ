# ROT13

import sys
input = sys.stdin.readline

_string = list(input())
answer = []

for i in _string:
    temp = ord(i)
    if temp >= 65 and temp <= 90:
        temp += 13
        if temp > 90:
            temp -= 26

    elif temp >= 97 and temp <= 122:
        temp += 13
        if temp > 122:
            temp -= 26
        

    answer.append(chr(temp))


for i in range(len(answer)):
    if i != len(answer):
        print(answer[i],end='')
    else:
        print(answer[i])
    


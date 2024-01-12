# 문자열 분석
import sys

while True:
    try:
        _string = list(input())
        result = [0,0,0,0]
        for i in _string:
            if i.islower():
                result[0]+=1
            elif i.isupper():
                result[1] +=1
            elif i.isnumeric():
                result[2] +=1
            elif i.isspace() :
                result[3] +=1
        print(*result)
    except EOFError :
        break



#단어 뒤집기 2
import sys
input = sys.stdin.readline

_string = list(input().rstrip())
_result = []
_stringStorage=[]
vocaConst = True
cnt = 0

for i in _string:
    if i == '<': # 단어상수 변환
        if len(_stringStorage) != 0:
            for _ in range(len(_stringStorage)):
                _result.append(_stringStorage.pop())
        _result.append(i)
        vocaConst = False
        cnt +=1
        continue
    elif i == '>':
        vocaConst = True
        _result.append(i)
        cnt +=1
        continue
    
    if vocaConst == False:
        _result.append(i)
        cnt +=1

    else: # vocaConst == True:
        if i != ' ': # 단어일 경우
            _stringStorage.append(i)
            cnt +=1
        
        elif i ==  ' ':
            for _ in range(len(_stringStorage)):
                _result.append(_stringStorage.pop())
            _result.append(' ')
            cnt +=1
for _ in range(len(_stringStorage)):
    _result.append(_stringStorage.pop())

for i in range(len(_result)):
    if i != len(_result)-1:
        print(_result[i],end='')
    else:
        print(_result[i])
    

    
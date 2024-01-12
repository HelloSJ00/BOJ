#에디터
import sys
input = sys.stdin.readline

def L():
    if len(_string) !=0:
        _stringStorage.append(_string.pop())
    
def D():
    if len(_stringStorage) !=0:
        _string.append(_stringStorage.pop())

def B():
    if len(_string) != 0:
        _string.pop()
    
def P(x):
    _string.append(x)
    

_string = list(input().rstrip())
_stringStorage= []
M = int(input())

for _ in range(M):
    command = input().split()
    if command[0] == 'L':
        L()
    if command[0] == 'D':
        D()
    if command[0] == 'B':
        B()
    if command[0] == 'P':
        P(command[1])

while (_stringStorage):
    _string.append(_stringStorage.pop())

for i in _string:
    print(i,end='')
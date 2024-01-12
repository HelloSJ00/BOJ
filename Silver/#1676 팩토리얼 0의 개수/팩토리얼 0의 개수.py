# 팩토리얼 0의 개수

import sys,math

input = sys.stdin.readline
N = int(input())

Nfactorial = N
if N == 0:
    Nfactorial = 1
else:
    for i in range(1,N):
        Nfactorial *=i

Nfactorial = list(str(Nfactorial))

cnt = 0
i = len(Nfactorial) -1
while i != -1:
    if Nfactorial[i] == '0':
        cnt+=1
    else:
        break
    i -=1

print(cnt)

    
    

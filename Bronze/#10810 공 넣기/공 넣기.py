# 1차원 배열 공넣기

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

blanket = [0]*(N+1)

for _ in range(M):
    i,j,k = map(int,input().split())
    for i in  range(i,j+1):
        blanket[i] = k

for i in range(N):
    print(blanket[i+1],end=' ')

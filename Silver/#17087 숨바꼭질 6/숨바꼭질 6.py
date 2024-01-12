# 숨바꼭질6

import sys,math
input = sys.stdin.readline

N,S = map(int,input().split())
A = list(map(int,input().split()))

if N == 1 :
    print(abs(A[0] -S))
    
else:
    for i in range(N):
        A[i] = abs(A[i]-S)

    result = A[0]
    for i in range(1,len(A)):
        result = math.gcd(A[i],result)

    print(result)



import sys
input = sys.stdin.readline
N,R,C = map(int,input().split())

def recru(y,x,N,value):
  if N == 0:
    return value
  
  if 0 <= y < 2**(N-1) and 0 <= x < 2**(N-1) :
    return recru(y,x,N-1,value)

  elif 0 <= y < 2**(N-1) and 2**(N-1) <= x < 2**(N) :
    return recru(y,x-(2**(N-1)),N-1,value + (2**(N-1))**2)

  elif 2**(N-1) <= y < 2**(N) and 0 <= x < 2**(N-1) :
    return recru(y-(2**(N-1)),x,N-1,value + 2*((2**(N-1))**2))

  elif 2**(N-1) <= y < 2**(N) and 2**(N-1) <= x < 2**(N) :
    return recru(y-(2**(N-1)),x-(2**(N-1)),N-1,value + 3*((2**(N-1))**2))

print(recru(R,C,N,0))
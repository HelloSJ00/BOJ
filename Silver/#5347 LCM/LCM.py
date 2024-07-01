import sys
input = sys.stdin.readline

# 시간제한 1초 , 입력제한 1 ~ 1,000,000 
def lcm(A,B):
  if A%B == 0:
    return B
  return lcm(B,A%B)
# 입력 
TC = int(input())
for _ in range(TC):
  a,b = map(int,input().split())
  if a > b:
    print((a*b)//lcm(a,b))
  else:
    print((a*b)//lcm(b,a))
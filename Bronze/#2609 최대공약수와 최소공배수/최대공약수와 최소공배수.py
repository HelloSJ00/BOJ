# 최소공배수 최대공약수

import math,sys
input = sys.stdin.readline

a,b = map(int,input().split())
gcd = math.gcd(a,b)
lcm = math.lcm(a,b)

print(gcd)
print(lcm)

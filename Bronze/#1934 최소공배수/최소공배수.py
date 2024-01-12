# 최소공배수 
import sys,math

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    A,B = map(int,input().split())
    print(math.lcm(A,B))
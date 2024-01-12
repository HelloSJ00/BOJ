# 조합 0의 개수

import sys
input = sys.stdin.readline

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five
    
n,m = map(int,input().split())

cnt5 = five_count(n)-five_count(m)-five_count(n-m)
cnt2 = two_count(n)-two_count(m)-two_count(n-m)
if cnt5 > cnt2:
    print(cnt2)
else:
    print(cnt5)



import sys,heapq
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
dic = {}
for _ in range(M):
	web, pw = input().split()
	dic[web] = pw
for _ in range(N):
	findPw = input().rstrip()
	print(dic[findPw])
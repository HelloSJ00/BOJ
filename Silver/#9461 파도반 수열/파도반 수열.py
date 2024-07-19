import sys,heapq,collections
input = sys.stdin.readline

P = [0,1,1,1,2,2,3,4,5,7,9]+[0]*90



for i in range(11,101):
	P[i] = P[i-1] + P[i-5]

test_case = int(input().rstrip())
for _ in range(test_case):
	print(P[int(input().rstrip())])
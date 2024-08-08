import sys,heapq
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int,input().split()))
M = int(input().rstrip())
B = list(map(int,input().split())) 

A_idx = -1
B_idx = -1
answer = []
while A_idx != len(A)-1:
	prev = 0
	# print('a ->',A_idx,'b->',B_idx)
	for a in range(A_idx+1,len(A)):
		for b in range(B_idx+1,len(B)):
			if A[a] == B[b] and A[a] > prev:
				prev = A[a]
				A_tmp_idx = a
				B_tmp_idx = b
	if prev ==0:
		break
	else:
		A_idx = A_tmp_idx
		B_idx = B_tmp_idx
	answer.append(prev)

print(len(answer))
if len(answer) !=0:
	print(*answer)
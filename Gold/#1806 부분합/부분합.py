import sys
input = sys.stdin.readline

def window_sliding(arr,S):
	s = 0
	e = s
	sum = arr[0]
	answer = float('inf')
	while True:


		if sum < S:
			if e != len(arr)-1:
				e += 1
				sum += arr[e]
			else: 
				s += 1
				sum -= arr[s-1]
				
		elif sum >= S:
			answer = min(answer,e-s+1)
			s += 1
			sum -= arr[s-1]

		if s == len(arr)-1 and e == len(arr)-1:
			if sum >= S:
				answer = min(answer,e-s+1)
			if answer == float('inf'):
				return print(0)
			return print(answer)
N,S = map(int,input().split())
arr = list(map(int,input().split()))

window_sliding(arr,S)
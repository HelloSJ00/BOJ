import sys,heapq,collections
input = sys.stdin.readline

N = int(input().rstrip())

# 양수 배열
arr1 = []
# 음수 배열
arr2 = []

for _ in range(N):
	command = int(input().rstrip())
	if command == 0:
		if len(arr1) == 0 and len(arr2) == 0:
			print(0)
		elif len(arr1) == 0 and len(arr2) > 0:
			print(-heapq.heappop(arr2))
		elif len(arr1) > 0 and len(arr2) == 0:
			print(heapq.heappop(arr1))
		elif arr1[0] >= arr2[0]:
			print(-heapq.heappop(arr2))
		elif arr1[0] < arr2[0]:
			print(heapq.heappop(arr1))

	else:
		if command >= 0:
			heapq.heappush(arr1,command)
			# print('arr1->',arr1)
		else:
			heapq.heappush(arr2,-command)
			# print('arr2->',arr2)
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().split()))
lis = [arr[0]]

for i in arr:
	if lis[-1] < i:
		lis.append(i)
	else:
		start = 0
		end = len(lis)-1
		while start < end:
			mid = (start + end)//2
			if lis[mid] >= i:
				end = mid
			else:
				start = mid + 1
		
		lis[end] = i
# print(lis)
print(len(lis))
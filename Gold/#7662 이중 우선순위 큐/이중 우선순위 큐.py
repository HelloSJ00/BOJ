import sys,heapq,collections
input = sys.stdin.readline

TC = int(input().rstrip())

for _ in range(TC):
	N = int(input().rstrip())
	min_heap = []
	max_heap = []
	nums = set()
	id = 0

	for _ in range(N):
		command, num = input().split()
		num = int(num)
		if command == 'I':
			heapq.heappush(min_heap,(num,id))
			heapq.heappush(max_heap,(-num,id))
			nums.add(id)
			id +=1 
		else:
			if num == 1:
				while len(nums) != 0:
					cur_num,cur_id = heapq.heappop(max_heap)
					if cur_id in nums:
						nums.remove(cur_id)
						break
			else:
				while len(nums) != 0:
					cur_num,cur_id = heapq.heappop(min_heap)
					if cur_id in nums:
						nums.remove(cur_id)
						break
		
	# 출력
	if  len(nums) == 0:
		print('EMPTY')
	else:
		while True:
			cur_num,cur_id = heapq.heappop(max_heap)
			if cur_id in nums:
				print(-cur_num,end=' ')
				break
		while True:
			cur_num,cur_id = heapq.heappop(min_heap)
			if cur_id in nums:
				print(cur_num)
				break
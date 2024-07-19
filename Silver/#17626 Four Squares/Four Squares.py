import sys,heapq,collections
input = sys.stdin.readline

# def search(s,e,target,arr):
# 	while s < e:
# 		m = (s+e)//2
# 		if target < arr[m]:
# 			e = m
# 		else:
# 			s = m+1
# 	return e-1
	

N = int(input().rstrip())
squares = [n**2 for n in range(int(N**(1/2))+1)]
total = 0
nums = [N]
while len(nums) > 0:
    total += 1
    temp = set()
    for num in nums:
        for n in squares:
            if n <= num:
                temp.add(num-n)
    #print(temp)
    if 0 in temp:
        break
    nums = list(temp)
print(total)
  



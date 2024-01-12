# GCD합
import sys,math
import collections
input = sys.stdin.readline

TC = int(input())


for _ in range(TC):
    nums = collections.deque(list(map(int,input().split())))
    N = nums.popleft()
    
    i = 1
    sum = 0
    while len(nums) != 1:
        sum += math.gcd(nums[0],nums[i])

        if (i < len(nums)-1):
            i +=1
        elif i == (len(nums) -1):
            nums.popleft()
            i = 1
        
    print(sum)




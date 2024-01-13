import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

# END = True

# while END:
#     idx_list = []
#     for idx in range(N-1):
#         if nums[idx]+1 == nums[idx+1]:
#             idx_list.append(idx)

#     if len(idx_list) == 0:
#         END = False
#         break

#     if len(idx_list) == 3:
#         nums[idx_list[1]],nums[idx_list[1]+1] = nums[idx_list[1]+1],nums[idx_list[1]]
#     else :
#         nums[idx_list[len(idx_list)-1]],nums[idx_list[len(idx_list)-1]+1] =nums[idx_list[len(idx_list)-1]+1],nums[idx_list[len(idx_list)-1]]

# print(*nums)

csort = [0 for _ in range(1002)]
for num in nums:
    csort[num] += 1

anwser = []
while True:
    tof=False
    for i in range(1001):
        if csort[i]:
            tof=True
            if csort[i+1]:
                k = -1
                for j in range(i+2,1001):
                    if csort[j]:
                        k = j
                        break
                if k != -1:
                    while csort[i]:
                        anwser.append(i)
                        csort[i] -=1
                    anwser.append(k)
                    csort[k] -= 1
                    break
                else:
                    anwser.append(i+1)
                    csort[i+1] -= 1
                    break
            else:
                while csort[i]:
                    anwser.append(i)
                    csort[i] -= 1
                break
    if tof == False:
        break
print(*anwser)
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split())) 
S = int(input())

for start in range(N):
    if S == 0:# S 가 0이면 종료
        break

    tmpIdx = start # start와 교환할 num의 index

    #큰 수 찾기
    for idx in range(start+1,N):
        if S < (idx-start):
            break

        if (nums[tmpIdx] < nums[idx]): 
            tmpIdx = idx
            
    #정렬 시작
    if tmpIdx != 0 :

        for i in range(tmpIdx,start,-1):
            nums[i],nums[i-1]= nums[i-1],nums[i]
   
        S -= (tmpIdx - start)
print(*nums)


# end = 1
# ISEND = 1
# ISSORT = 1
# while  ISEND :
#     ISSORT = 1 # 내림차순 정렬되어있는지 확인하는 용도 , 반복문을 도는동안 위치변환이 없다면 정렬되어있으므로 0으로 바꿔서 반복문 종료
#     for i in range(len(nums)-end):
#         if nums[i] < nums[i+1] and S > 0:
#             nums[i],nums[i+1] = nums[i+1],nums[i]
#             S-=1
#             ISSORT = 0

#     if S == 0 or ISSORT == 1 :
#         ISEND = 0
        
#     end +=1

# print(*nums)
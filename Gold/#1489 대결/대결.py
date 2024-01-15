import sys
input = sys.stdin.readline

coA = [0 for _ in range(1002)]
coB = [0 for _ in range(1002)]  

#계수 정렬
N = int(input())
A_team = list(map(int,input().split()))
for num in A_team:
    coA[num] +=1
B_team = list(map(int,input().split()))
for num in B_team:
    coB[num] +=1

anwser = 0

for i in range(1002):
    while coA[i]:
        tof = False
        for j in range(i-1,0,-1):
            if coB[j]:
                tof = True
                anwser +=2
                coA[i] -=1
                coB[j] -=1
                break
        if tof == False:
            break
for i in range(1,1002):
    while coA[i] and coB[i]:
        anwser +=1
        coA[i] -=1
        coB[i] -=1
print(anwser)



    
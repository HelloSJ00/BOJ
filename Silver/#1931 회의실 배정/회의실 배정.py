import sys
input = sys.stdin.readline

N = int(input()) # 회의의 수
meet = [] 
for _ in range(N):
    meet.append(list(map(int,input().split())))

meet.sort(key = lambda x:(x[1],x[0]))
anwser = 0
endTime = 0
for i in range(len(meet)):
    if endTime <= meet[i][0]:
        endTime = meet[i][1]
        anwser +=1
print(anwser)
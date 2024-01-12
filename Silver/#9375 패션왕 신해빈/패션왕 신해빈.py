import sys
input = sys.stdin.readline
TC = int(input()) # 테스트 케이스

for _ in range(TC):
    N = int(input())
    dic = {} # 옷장
    wears = [] # 옷 종류
    for i in range(N):
        wear, kind = input().split()
        if kind not in dic:
            dic[kind] = [wear]
            wears.append(kind)
        else:
            dic[kind].append(wear)
    anwser = 1
    for i in wears:
        anwser *= (len(dic[i])+1)

    print(anwser-1)
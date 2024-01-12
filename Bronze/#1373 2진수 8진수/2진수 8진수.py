# 2진수 8진수
import sys
input = sys.stdin.readline


two = list(input().rstrip())[::-1]
eight =[]
value = 0

for i in range(len(two)):
    if two[i] == '1':
        if (i % 3) == 0:
            value += 1
        elif (i % 3) == 1:
            value += 2
        elif (i % 3) == 2:
            value += 4
            eight.append(value)
            value = 0

    elif two[i] == '0':
        if (i % 3)==2:
            eight.append(value)
            value = 0
    
    if (i%3) != 2 and i == (len(two)-1):
        eight.append(value)


for i in range(len(eight)):
    print(eight.pop(),end='')






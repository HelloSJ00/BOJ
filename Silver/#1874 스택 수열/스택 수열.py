# 스택 스택수열

import sys

N = int(sys.stdin.readline())

stack = []  # 스택
storageStack=[] # push 할 스택
number_list=[] # 입력받을 수열 
pushpop_list=[] # push pop 

for i in range(N):
    storageStack.append(i+1)

storageStack.sort(reverse=True) # [8,7,6,5,4,3,2,1]

for _ in range(N): # 수열 입력받기
    number_list.append(int(sys.stdin.readline()))

cmd_No = 0
for i in number_list:
    while True :
        if len(stack) == 0: # 스택이 비어있다면 # push
            pushpop_list.append('+')
            stack.append(storageStack.pop())

        # len(stack) >= 1
        if stack[len(stack)-1] < i : # push
            pushpop_list.append('+')
            stack.append(storageStack.pop())

        elif stack[len(stack)-1] == i :  # pop
            pushpop_list.append('-')
            stack.pop()
            break


        if stack[len(stack)-1] > i:
            cmd_No  = 1
            print('NO')
            break

    if cmd_No == 1 :
        break

if cmd_No != 1:    
    for i in pushpop_list:
        print(i)


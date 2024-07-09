import sys
input = sys.stdin.readline

while True:
    arr = list(input().rstrip())
    stack = []
    tof = True
    
    # 종료조건
    if len(arr) == 1 and arr[0] == '.':
        break
    
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                tof = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                tof = False
                break
    
    if tof and not stack:
        print('yes')
    elif tof:
        print('no')

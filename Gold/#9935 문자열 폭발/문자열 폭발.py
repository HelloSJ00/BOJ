import sys
input=sys.stdin.readline

# 입력
arr = list(input().rstrip())
target=list(input().rstrip())

# cur = 0
# curarr_length = len(arr)
# while cur + len(target) -1 <= curarr_length-1:
#   # print(arr)
#   if arr[cur:cur+len(target)] == target:
#     if cur == 0:
#       arr = arr[cur+len(target):]
#     else:
#       arr = arr[:cur] + arr[cur+len(target):]

#     if cur >= len(target)-1:
#       cur = cur - len(target)+1
#     else:
#       cur = 0
    
#     curarr_length = len(arr)
  
#     continue
#   cur +=1


# if arr:
#   for i in range(len(arr)):
#     print(arr[i],end='')
# else:
#   print('FRULA')

# 스택을 활용하자
answer = []

for i in arr:
  answer.append(i)
  if len(answer) >= len(target) and answer[len(answer)-len(target):] == target:
    for _ in range(len(target)):
      answer.pop()
if answer:
  for i in answer:
    print(i,end='')
else:
  print('FRULA')
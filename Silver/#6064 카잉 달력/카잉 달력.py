import sys
input = sys.stdin.readline

def answer(x,y,cur_x,cur_y):
  k = cur_x
  if cur_x == cur_y:
    return cur_x
  while k <= x*y:
    if (k-cur_y) % y == 0:
      return k
    k += x
  return -1

test_case = int(input().rstrip())
for _ in range(test_case):
  x,y,cur_x,cur_y = map(int,input().split())
  print(answer(x,y,cur_x,cur_y))
  
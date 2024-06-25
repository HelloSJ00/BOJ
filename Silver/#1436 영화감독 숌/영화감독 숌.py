import sys
input = sys.stdin.readline

#시간 복잡도를 O(N^2) 까지는 가능 
#입력
N = int(input())

#출력
start = 0
find_cnt = 0
while True:
  if '666' in str(start):
    find_cnt +=1
    if find_cnt == N : 
      print(start)
      break
  start+=1
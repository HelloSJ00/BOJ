import sys
input = sys.stdin.readline
import heapq

arr= []
N = int(input().rstrip())

for _ in range(N):
  command = int(input().rstrip())
  if command !=0:
    heapq.heappush(arr,command)
  elif arr and command == 0:
    print(heapq.heappop(arr))
  elif command == 0 and arr == []:
    print(0)
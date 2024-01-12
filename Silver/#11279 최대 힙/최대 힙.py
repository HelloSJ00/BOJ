import sys,heapq
input = sys.stdin.readline

def inputNum(arr,num):
    heapq.heappush(arr,(-num)) # heapq는 최소 힙으로 구성되어 있어서 -를 붙혀서 최대 힙으로 전환

def outputNum(arr):
    if len(arr) == 0:
        print(0)
    else:
        print(-1*heapq.heappop(arr))



N = int(input())
heap = []

for _ in range(N):
    X = int(input())
    if X > 0 :
        inputNum(heap,X)
    elif X == 0:
        outputNum(heap)

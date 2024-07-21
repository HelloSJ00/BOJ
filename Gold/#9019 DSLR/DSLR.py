import sys
from collections import deque

input = sys.stdin.readline

def dslr_d(n):
    return (2 * n) % 10000

def dslr_s(n):
    return (n - 1) % 10000 if n != 0 else 9999

def dslr_l(n):
    return (n % 1000) * 10 + n // 1000

def dslr_r(n):
    return (n % 10) * 1000 + n // 10

def bfs(start, goal):
    visited = [False] * 10000
    queue = deque([(start, '')])
    visited[start] = True
    
    while queue:
        current, operations = queue.popleft()
        
        if current == goal:
            return operations
        
        next_d = dslr_d(current)
        next_s = dslr_s(current)
        next_l = dslr_l(current)
        next_r = dslr_r(current)
        
        if not visited[next_d]:
            visited[next_d] = True
            queue.append((next_d, operations + 'D'))
        
        if not visited[next_s]:
            visited[next_s] = True
            queue.append((next_s, operations + 'S'))
        
        if not visited[next_l]:
            visited[next_l] = True
            queue.append((next_l, operations + 'L'))
        
        if not visited[next_r]:
            visited[next_r] = True
            queue.append((next_r, operations + 'R'))
test_case = int(input().rstrip())
for _ in range(test_case):
    start,goal = map(int,input().split())
    print(bfs(start,goal))
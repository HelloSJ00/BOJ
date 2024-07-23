import sys
input = sys.stdin.readline
from collections import deque

def dfs(start):
    stack = [(start, 0)]
    visit = [0] * (N + 1)
    visit[start] = 1
    farthest_node = start
    max_dist = 0

    while stack:
        cur_v, cur_dist = stack.pop()
        if cur_dist > max_dist:
            max_dist = cur_dist
            farthest_node = cur_v

        for next_vertex, weight in tree[cur_v]:
            if visit[next_vertex] == 0:
                visit[next_vertex] = 1
                stack.append((next_vertex, cur_dist + weight))

    return farthest_node, max_dist

# 트리 초기화
N = int(input().rstrip())
tree = [[] for _ in range(N + 1)]
for _ in range(N):
    tmp_arr = list(map(int, input().split()))
    for i in range(1, len(tmp_arr), 2):
        if tmp_arr[i] == -1:
            break
        tree[tmp_arr[0]].append((tmp_arr[i], tmp_arr[i + 1]))

# 첫 번째 DFS를 이용해 임의의 노드(1번 노드)에서 가장 먼 노드 찾기
farthest_node, _ = dfs(1)

# 두 번째 DFS를 이용해 가장 먼 노드에서 다시 가장 먼 노드 찾기
_, answer = dfs(farthest_node)

print(answer)

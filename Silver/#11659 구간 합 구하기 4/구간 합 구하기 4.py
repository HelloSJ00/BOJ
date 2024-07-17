import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# DP 배열을 초기화하고 누적 합을 계산
DP = [0] * (N + 1)
for i in range(1, N + 1):
    DP[i] = DP[i - 1] + arr[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(DP[j])
    else:
        print(DP[j] - DP[i - 1])

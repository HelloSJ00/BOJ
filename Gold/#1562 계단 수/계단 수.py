import sys
input = sys.stdin.readline

MOD = 1000000000

def count_full_stair_numbers(N):
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]
    
    # 초기화: 1자리 숫자들
    for j in range(1, 10):
        dp[1][j][1 << j] = 1
    
    for i in range(2, N + 1):
        for j in range(10):
            for k in range(1 << 10):
                if j > 0:
                    dp[i][j][k | (1 << j)] += dp[i-1][j-1][k]
                if j < 9:
                    dp[i][j][k | (1 << j)] += dp[i-1][j+1][k]
                dp[i][j][k | (1 << j)] %= MOD
    
    # N자리 숫자에서 0~9까지 모두 포함된 상태를 찾음
    full_mask = (1 << 10) - 1
    result = 0
    for j in range(10):
        result += dp[N][j][full_mask]
        result %= MOD
    
    return result

# 예시 실행
N = int(input())  # 예를 들어 N이 10일 때
print(count_full_stair_numbers(N))

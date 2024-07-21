import sys
input = sys.stdin.readline

def longest_fruit_tanghulu(N, fruits):
    left = 0
    max_length = 0
    fruit_count = {}
    
    for right in range(N):
        if fruits[right] in fruit_count:
            fruit_count[fruits[right]] += 1
        else:
            fruit_count[fruits[right]] = 1
        
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# 입력
N = int(input().strip())
fruits = list(map(int, input().strip().split()))

# 출력
print(longest_fruit_tanghulu(N, fruits))
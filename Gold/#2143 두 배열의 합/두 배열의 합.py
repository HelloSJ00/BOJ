import sys
from collections import defaultdict

input = sys.stdin.readline

# 부분 배열의 모든 합을 구하고 그 개수를 딕셔너리로 반환하는 함수
def get_subarray_sums(arr):
    n = len(arr)
    subarray_sums = defaultdict(int)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            subarray_sums[current_sum] += 1
    
    return subarray_sums

T = int(input().rstrip())
n = int(input().rstrip())
arr1 = list(map(int, input().split()))
m = int(input().rstrip())
arr2 = list(map(int, input().split()))

# arr1과 arr2에서 가능한 모든 부분 배열의 합을 계산
subarray_sums1 = get_subarray_sums(arr1)
subarray_sums2 = get_subarray_sums(arr2)

answer = 0

# arr1의 부분 배열 합과 arr2의 부분 배열 합을 더해 T가 되는 쌍을 계산
for sum1, count1 in subarray_sums1.items():
    target = T - sum1
    if target in subarray_sums2:
        answer += count1 * subarray_sums2[target]

print(answer)

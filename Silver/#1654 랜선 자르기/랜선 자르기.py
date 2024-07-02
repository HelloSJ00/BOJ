import sys
input = sys.stdin.readline
# 시간제한 2초 

# 입력
N, K = map(int,input().split())
arr = []
answer = 0
for _ in range(N):
  arr.append(int(input().rstrip()))
start = 0
end = 10000000000
while start <= end:
  cnt = 0 
  # 이분 탐색 시작
  mid = (start+end)//2
  for i in arr:
    cnt += (i//(mid+1))

  if cnt >= K :
    start = mid + 1
    if mid > answer :
      answer = mid
  else:
    end = mid -1
print(answer+1)
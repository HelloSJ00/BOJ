import sys
input = sys.stdin.readline
# 시간제한 1초 K 10,000,000 이하 O(n) 이하로 해결

coin = []
answer=0
#입력 
N,M = map(int,input().split())
for _ in range(N):
  coin.append(int(input().rstrip()))

#출력
coin = coin[::-1]

for i in range(len(coin)):
  answer += M // coin[i]
  M = M % coin[i]
  if M == 0:
    break
print(answer)


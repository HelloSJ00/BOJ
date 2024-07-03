import sys
input = sys.stdin.readline
# 시간제한 2초 

# 입력
up=[]
down=[]
N , H = map(int,input().split())
for _ in range(N//2):
  down.append(int(input().rstrip()))
  up.append(int(input().rstrip()))
down.sort()
up.sort()

result = [0] * 500001
answer = 0
mx = 2147483647
# 로직
def lower_bound(s,e,d,L):
  while s < e:
    m = (s+e)//2
    if L[m] < d:
      s = m + 1
    else:
      e = m
  return e

for floor in range(1,H+1):
  idx1 = lower_bound(0,len(up),H-floor+1,up)
  idx2 = lower_bound(0,len(down),floor,down)
  result[floor] = N-idx1-idx2
  mx = min(mx,result[floor])

for floor in range(1,H+1):
  if result[floor] == mx : answer +=1
print(mx,answer)
# 출력

# answer = [N,0]

# # 출력
# for floor in range(1,H+1):
#   odd_cnt = 0
#   even_cnt = 0
#   for i in range(N):
#     if i%2 == 0:
#       if suksoon[i] - floor >=0:
#         odd_cnt +=1
#     else :
#       if suksoon[i] + floor > H :
#         even_cnt +=1
#   if answer[0] == (odd_cnt + even_cnt):
#     answer[1] +=1

#   if answer[0] > (odd_cnt + even_cnt):
#     answer[0] = (odd_cnt + even_cnt)
#     answer[1] = 1
#   # print('현재까지 장애물 최소 개수 =>',answer[0])
#   # print('현재까지 최소 장애물 구간 개수 = >', answer[1])


# print(*answer)
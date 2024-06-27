import sys
input = sys.stdin.readline

# 시간제한 2초 , 입력제한 2~11 
#입력
N = int(input())

# 수열
numList = list(map(int,input().split()))

# 차례대로 덧셈 ,뺄셈 ,곱셈 ,나눗셈 개수
mathList = list(map(int,input().split()))

# 결과들
answer = []
sum = numList[0]

def bt(depth,sum):
  if depth == N-1:
    answer.append(sum)
    return
  # 1
  if mathList[0] > 0:
    tmp_sum= sum + numList[depth+1]
    mathList[0] -= 1
    bt(depth+1,tmp_sum)
    mathList[0] += 1
  # 2
  if mathList[1] > 0:
    tmp_sum = sum - numList[depth+1]
    mathList[1] -= 1
    bt(depth+1,tmp_sum)
    mathList[1] += 1
  # 3 
  if mathList[2] > 0:
    tmp_sum = sum*numList[depth+1]
    mathList[2] -= 1
    bt(depth+1,tmp_sum)
    mathList[2] += 1
  # 4
  if mathList[3] > 0:
      mathList[3] -= 1
      # 나눗셈은 정수 나눗셈이어야 하므로 주의
      if sum < 0:
          bt(depth+1, -(-sum // numList[depth+1]))
      else:
          bt(depth+1, sum // numList[depth+1])
      mathList[3] += 1  # 백트래킹

bt(0,sum)
print(max(int(-1e9),max(answer)))
print(min(int(1e10),min(answer)))
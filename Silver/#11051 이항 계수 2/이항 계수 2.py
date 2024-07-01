import sys
input = sys.stdin.readline

# 시간제한 1초 , 입력제한 1~1000 O(n^2)까지 가능
# 입력 
N,K = map(int,input().split())
arr=[[1,1]]

for i in range(N):
  tmp = [1]
  for j in range(len(arr[i])):
    if j == len(arr[i])-1:
      tmp.append(1)
      break
    tmp.append(((arr[i][j]%10007)+(arr[i][j+1]%10007))%10007)
  arr.append(tmp)
print(arr[N-1][K])

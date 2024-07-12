import sys
input = sys.stdin.readline

# 입력
a,b = map(int,input().split())

arr=[]
def countingMin(start,end,cnt):
  if start == end:
    arr.append(cnt)
    return
  if start*2 <= end:
    countingMin(start*2,end,cnt+1)
  if (start*10)+1 <= end:
    countingMin((start*10) +1 ,end, cnt+1)

countingMin(a,b,1)
if arr:
  print(min(arr))
else:
  print(-1)
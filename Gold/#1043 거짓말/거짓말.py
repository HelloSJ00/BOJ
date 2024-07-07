import sys
input = sys.stdin.readline

def find_parent(num):
  if arr[num] != num:
    return find_parent(arr[num])
  return num

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x != root_y:
        arr[root_y] = root_x
  
arr = [i for i in range(51)]
#입력 
N,M = map(int,input().split())
truth_people = list(map(int,input().split()))[1:]
truth_people.sort()

# 진실을 아는 사람 유니온
# 진실을 아는 사람 유니온
for i in range(1, len(truth_people)):
    union(truth_people[i], truth_people[i-1])

parties = []
for i in range(M):
    tmp_list = list(map(int, input().split()))[1:]
    parties.append(tmp_list)
    for j in range(1, len(tmp_list)):
        union(tmp_list[j], tmp_list[j-1])

if truth_people:
  compared = find_parent(truth_people[0])
else:
  compared = 0

answer = 0
for party in parties:
  tof = True
  for j in party:
    if find_parent(j) == compared:
      tof = False
  if tof :
    answer +=1
print(answer)
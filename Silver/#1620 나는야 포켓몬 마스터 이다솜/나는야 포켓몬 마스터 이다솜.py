import sys
input = sys.stdin.readline
N,M = map(int,input().split())

dogam_dic = {}
dogam_list=[]
for i in range(1,N+1):
  pokemon = input().rstrip()
  dogam_dic[pokemon] = i
  dogam_list.append(pokemon)
# print(dogam_dic)
# print(dogam_list)
for _ in range(M):
  command = input().rstrip()
  if command in dogam_dic:
    print(dogam_dic[command])
  else:
    num = int(command)
    print(dogam_list[num-1])
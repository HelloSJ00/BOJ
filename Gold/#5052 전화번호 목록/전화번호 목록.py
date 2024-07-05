import sys
input=sys.stdin.readline

class NODE:
  def __init__(self):
    self.value = False
    self.child={}

class Trie:
  def __init__(self):
    self.root = NODE()
  
  def insert(self,phone_num):
    curNode = self.root
    for i in phone_num:
      if i not in curNode.child :
        curNode.child[i]=NODE()
      curNode = curNode.child[i]
      if curNode.value == True:
        return False
    curNode.value = True
    return True
  
TC = int(input().rstrip())
for _ in range(TC):
  num_of_phone_num = int(input().rstrip())
  arr = [input().rstrip() for _ in range(num_of_phone_num)]
  arr.sort()
  trie = Trie()
  flag = 1
  for phone_num in arr:
    # print(phone_num)
    if trie.insert(phone_num) is False:
      print('NO')
      flag = 0
      break
  if flag == 1:
    print('YES')
    
      





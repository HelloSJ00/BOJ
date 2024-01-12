import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

class Node: # 노드 객체
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree: # 트리 객체
    def __init__(self) -> None:
        self.root = None
    
    def add(self,data):
        if self.root == None : # 루트가 없다면
            self.root = Node(data)
        
        else:
            current = self.root
            while True :
                if current.data > data :
                    if current.left == None:
                        current.left = Node(data)
                        break
                    current = current.left
                if current.data < data :
                    if current.right == None:
                        current.right = Node(data)
                        break
                    current = current.right
    
    def postorder(self,node = None):
        global answer
        if node == None:
            node = self.root
        
        if node.left != None :
            self.postorder(node.left)
        if node.right != None :
            self.postorder(node.right)
        answer.append(node.data)
        
        
answer = []
tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:
        break

tree.postorder()
print('\n'.join(map(str,answer)))
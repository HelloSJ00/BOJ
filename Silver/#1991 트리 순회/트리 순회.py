class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(preorder Traversal)
def pre_order(node):
    print(node, end='')
    if tree[node].left_node != None:
        pre_order(tree[node].left_node)
    if tree[node].right_node != None:
        pre_order(tree[node].right_node)

# 중위 순회(Inorder Traversal)
def in_order(node):
    if tree[node].left_node != None:
        in_order(tree[node].left_node)
    print(node, end='')
    if tree[node].right_node != None:
        in_order(tree[node].right_node)

# 후위 순회(Postorder Traversal)
def post_order(node):
    if tree[node].left_node != None:
        post_order(tree[node].left_node)
    if tree[node].right_node != None:
        post_order(tree[node].right_node)
    print(node, end='')

n = int(input())
tree = {}

for i in range(n): # 입력값 받기
    data, left_node, right_node = map(str, input().split())
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

for i in range(29): # 트리에 없는 알파벳 키값은 좌우에 연결된 노드들이 없는 트리값으로 추가해줌
    if tree.get(chr(ord('A') + i)) == None:
        tree[chr(ord('A') + i)] = Node(chr(ord('A') + i), None, None)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
class Treenode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


node1 = Treenode()
node1.data = "화사"

node2 = Treenode()
node2.data = "솔라"
node1.left = node2

node3 = Treenode()
node3.data = "문별" 
node1.right = node3

node4 = Treenode()
node4.data = "휘인"
node2.left = node4

node5 = Treenode()
node5.data = "쯔위"
node2.right = node5

node6 = Treenode()
node5.data = "선미"
node3.left = node6

print(node1.data)
print(node1.left.data)


# 이진 트리 순회 구현


# 1. 전위 순회 preorder traversal
def preorder(node):
    if node == None:
        return
    print(node.data, end="->")
    preorder(node.left)
    preorder(node.right)


# 2. 중위 순회 inorder traversal
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)


# 3. 후위 순회 postorder traversal
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="->")


if __name__ == "__main__":
    print("전위 순회:", end=" ")
    preorder(node1)
    print("끝")

    print("중위 순회:", end=" ")
    inorder(node1)
    print("끝")

    print("후위 순회:", end=" ")
    postorder(node1)
    print("끝")

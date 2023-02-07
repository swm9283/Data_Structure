# 이진 탐색 트리

# 데이터 크기를 기준으로 일정형태로 구성
# 이진 탐색 트리는 이진 트리의 일종이지만, 완전 이진 트리는 아니다.
# 특징
# 1. 왼쪽 서브 트리는 루트보다 모두 작은 값을 가진다.
# 2. 오른쪽 서브 트리는 루트보다 모두 큰 값을 가진다.
# 3. 각 서브 트리도 1,2번을 만족한다.
# 4. 모든 노드 값은 중복되지 않는다. 즉, 중복된 값은 이진 탐색 트리에 저장할 수 없다.


# Treenode class 생성.
class Treenode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


data_array = ["블랙핑크", "레드벨벳", "마마무", "에이핑크", "걸스데이", "트와이스"]


def preorder(node):
    if node == None:
        return
    print(node.data, end="->")
    preorder(node.left)
    preorder(node.right)


node = Treenode(data_array[0])
root = node


for i in data_array[1:]:
    node = Treenode(i)
    # print(node.data) data가 들어갔는 지 판단.

    current = root
    # print(current.data) 루트에 데이터가 잘 들어있는 지 판단.
    while True:
        if node.data < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

print("전위 순회:", end=" ")
preorder(root)
print("끝")

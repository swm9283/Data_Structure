# 응용 예제1.
import random


class Treenode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def preorder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


data = ["프로틴", "닭가슴살", "커피", "햇반", "삼다수", "복숭아아이스티홍차", "초코마카다미아과자", "연세크림우유빵"]
sell_data = [random.choice(data) for _ in range(20)]
print(f"오늘 판매된 물건(중복O0 --> {sell_data}")

data_array = [None]
# a = data_array[0]   list에 아무 것도 넣지 않고 list[0] 번 방을 참조하면 리스트 인덱스를 벗어낫다고 에러 발생.
# print(a)
for sell in sell_data:
    if data_array[0] == None:
        data_array[0] = sell
        continue
    if sell in data_array:
        continue
    else:
        data_array.append(sell)

node = Treenode(data_array[0])
root = node

for add in data_array[1:]:
    node = Treenode(add)
    current = root

    while True:
        if add < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
print()
print("이진 탐색 트리 구성 완료!")
print("오늘 판매된 종류", end="-->")
preorder(root)

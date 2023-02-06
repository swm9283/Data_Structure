# 단순 연결 리스트 구현

# Node class 생성.
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


# print_nodes함수
def print_nodes(start):
    current = start
    if current.link == None:
        print("현재 노드는 마지막 노드입니다.")
        return
    print(current.data, end=" ")
    while current.link != None:
        current = current.link
        print(current.data, end=" ")
    print()  # 띄어쓰기.

#노드 삽입
def insert_node(find_data,insert_data):
    global memory,head,current,pre

    if find_data == head.data:
        node = Node(insert_data)
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return
    node = Node(insert_data)
    node.link = None
    current.link = node

#노드 삭제
def delete_node(delete_data):
    global memory,head,current,pre

    if delete_data ==head.data:
        print("첫 노드가 삭제됨.")
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print("중간 노드가 삭제됨.")
            pre.link = current.link
            del(current)
            return
    print("아무 노드가 삭제되지 않음.")











# 전역 변수 생성
memory = list()
head, current, pre = None, None, None
data_array = [f"{i}" for i in range(5)]

# main 함수 생성
if __name__ == "__main__":
    # 첫 번쨰 노드 생성
    node = Node(data_array[0])
    head = node
    memory.append(node)

    # 두 번째 노드 생성
    for i in data_array[1:]:
        pre = node
        node = Node(i)
        pre.link = node
        memory.append(node)
    print(data_array)
    print_nodes(head)

    insert_node("2","200")
    print_nodes(head)
    insert_node("0","1000")
    print_nodes(head)

    delete_node("1000")
    print_nodes(head)

    delete_node("4")
    print_nodes(head)

    delete_node("50")
    print_nodes(head)


# 단순 연결 리스트 구현

# Node class 생성.
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


# print_nodes함수
def print_nodes(start):
    current = start
    if current == None:
        print("노드에 아무것도 들어있지 않습니다.")
        return
    print(current.data, end=" ")
    while current.link != None:
        current = current.link
        print(current.data, end=" ")
    print()  # 띄어쓰기.


# 노드 삽입
def insert_node(find_data, insert_data):
    global memory, head, current, pre

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


# 노드 삭제
def delete_node(delete_data):
    global memory, head, current, pre

    if delete_data == head.data:
        print("첫 노드가 삭제됨.")
        current = head
        head = head.link
        del (current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print("중간 노드가 삭제됨.")
            pre.link = current.link
            del (current)
            return
    print("아무 노드가 삭제되지 않음.")


def find_node(find_data):
    global head, current, pre, memory

    current = head
    if find_data == head.data:
        return current.data
    while current is not None:
        current = current.link
        if current.data == find_data:
            return current.data
    return None


#  이름 순으로 전화번호부 정렬
def sort_telephone_book_by_name(namePhone):
    global head, current, pre, memory
    print_nodes(head)

    node = Node(data = namePhone)
    memory.append(node)
    if head is None:  # 첫 번째 노드 삽입.
        head = node
        return
    if head.data[0] > node.data[0]:  # 첫 번째 노드 보다 작을 때.
        node.link = head
        head = node
        return

    #  중간 노드로 삽입하는 경우
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] > node.data[0]:
            pre.link = node
            node.link = current
            return
    current.link = node  # 삽입하는 노드가 가장 큰 경우.


# 전역 변수 생성
memory = list()
head, current, pre = None, None, None
data_array = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"],
              ["진", "010-5555-5555"]]

# main 함수 생성
if __name__ == "__main__":
    for data in data_array:
        sort_telephone_book_by_name(data)
    print_nodes(head)

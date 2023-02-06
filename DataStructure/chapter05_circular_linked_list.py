# 연결리스트의 구현
class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

def print_nodes(start):
    current = start

    if current.link == None:
        # print("원형 연결 리스트의 마지막 노드입니다.")
        return
    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data,end=" ")
    print()

def insert_nodes(find_data,insert_data):
    global memory,head,pre,current

    if find_data == head.data:
        node = Node(insert_data)
        node.link = head

        current = head
        while current.link != head: # current.link = head가 되면 멈춘다.
            current = current.link
        current.link = node
        head = node

def delete_nodes(delete_data):
    global memory,head,current,pre

    if delete_data == head.data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if delete_data == current.data:
            pre.link = current.link
            del(current)
            return
        # print("1")
        # return # 왜 이렇게 하면 안될까? -> 함수라 이렇게 하면 리턴하고 끝내버리네.
        # 함수를 정의할 때. return이 break과 같은 역할이다.
        #  여기서는 반복문을 한번 돌고 끝내버림.

def find_node(find_data):
    global memory, head, pre, current

    if head.data == find_data:
        return head.data
    current = head
    while current.link != head:
        current = current.link
        if find_data == current.data:
            return current.data










memory = [] #  생성할 노드를 넣을 메모리
head, current, pre = None, None, None
data_array = ["다현","정연","쯔위","사나","지효"]
if __name__ == "__main__":
    node = Node(data_array[0])
    head = node
    node.link = head
    memory.append(node)


    for i in data_array[1:]:
        pre = node
        node = Node(i)
        pre.link = node
        node.link = head
        memory.append(node)   #  노드 객체가 5개가 만들어진다.
    print_nodes(head)









class Node():
    def __init__(self,data):
        self.data = data
        self.link = None

node1 = Node("다현")

node2 = Node("정연")
node1.link = node2

node3 = Node("쯔위")
node2.link = node3

node4 = Node("사나")
node3.link = node4

node5 = Node("지효")
node4.link = node5

#node 삽입
new_node = Node("재남")
new_node.link = node3
node2.link = new_node

#node 출력.
current = node1
print(current.data,end=" ")
while current.link != None:
    current = current.link
    print(current.data,end =" ")

#node 삭제.
#화살표를 먼저 수정하고, 노드를 삭제.
node2.link=node3
del(new_node)
current = node1
print(current.data,end=" ")
while current.link != None:
    current = current.link
    print(current.data,end =" ")




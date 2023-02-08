# graph의 일반 구현.


class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def simple_make(self):
        for row in range(self.size):
            data = input(f"{row}에 넣고 싶은 데이터를 넣으세요").split()
            for i in range(len(data)):
                self.graph[row][i] = int(data[i])


def print_graph(graph):
    """
    그래프 인접 행렬을 그려주는 함수다.
    data_array는 global에 먼저 지정해주어야 한다.
    :param graph: 인자로 그래프를 넣어야 한다.
    :return: None
    """
    global data_array

    print(" ##그래프##")
    print(end="  ")
    for data in data_array:
        print(data, end=" ")
    print()

    for row in range(graph.size):
        print(data_array[row], end=" ")
        for col in range(graph.size):
            print(f"{graph.graph[row][col]}", end=" ")
        print()


## 전역 변수 선언 부분 #

g1 = None
stack = []
visit_array = []

##메인 코드 부분 ##
# A, B, C, D = 0, 1, 2, 3
data_array = ["문별", "솔라", "휘인", "쯔위", "선미", "화사"]
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5

g1 = Graph(6)
g1.simple_make()

print_graph(g1)

current = 0  # 시작 정점
stack.append(current)
visit_array.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(6):
        if g1.graph[current][vertex] == 1:  # 방문한 적이 있는 정점이면 탈락
            if vertex in visit_array:
                pass
            else:  # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visit_array.append(current)

    else:
        current = stack.pop()

print("방문 순서 -->", end=" ")
for i in visit_array:
    print(data_array[i], end=" ")


def find_vertex(g, find_vertex):
    stack = []
    visit_array = []

    current = 0
    stack.append(current)
    visit_array.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(g.size):
            if g.graph[current][vertex] == 1:
                if vertex in visit_array:  # 이미 방문한 vertex이면 pass한다.
                    pass
                else:
                    next = vertex  # 방문한 적이 없는 vertext이면 next에 넣는다.
                    break
        if next is not None:  # 다음에 방문할 vertex가 있을 경우 현재 vertex를 current 변수에 저장한다.
            current = vertex
            stack.append(current)
            visit_array.append(current)
        else:
            current = stack.pop()  # 다음에 방문할 정점이 없는 경우

    if find_vertex in visit_array:
        return True
    else:
        return False


if find_vertex(g1, "화사"):
    print("화사가 연락이 됨.")

else:
    print("화사가 연락이 안됨.")

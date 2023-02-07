# 원형 큐의 일반 구현

#front = 0 rear = 0 : 원형 큐에서 한 칸을 비워두기 위함이다.




#  global variable
size = int(input("Please Enter the queue's size : "))
queue = [None for _ in range(size)]
front, rear = 0, 0


def is_queue_full():
    global queue, front, rear
    if rear + 1 % size == front:
        print("큐가 가득 찼습니다.")
        return True
    else:
        return False


def is_queue_empty():
    global queue, front, rear
    if rear == front:
        print("큐가 비었습니다..")
        return True
    else:
        return False


def dequeue():
    global queue, front, rear
    if is_queue_empty():
        print("큐가 비어있습니다.")
        return None
    front = (front + 1) % size #  마지막 칸 다음은 0이 되게 하기 위함이다.
    data = queue[front]
    queue[front] = None
    return data


def enqueue(data):
    global queue, front, rear
    if is_queue_full():
        print("큐가 가득찼습니다.")
        return None
    rear = (rear + 1) % size  #마지막 칸 다음은 0이 되게 하기 위힘이다.
    queue[rear] = data


def peek():
    global queue, front, rear
    if is_queue_empty():
        print("큐가 비어있습니다.")
        return None
    return queue[front+1 % size]


if __name__ == "__main__":

    # for i in range(size):
    #     enqueue(i)
    #     print("큐상태", queue)
    #
    # is_queue_full()
    #
    # for i in range(size):
    #     dequeue()
    #     print()
    #     print("큐상태", queue)
    for i in range(size-1):
        enqueue(1)
    print(queue)

    dequeue()
    print(queue)
    enqueue(1)
    print(queue)
    dequeue()
    print(queue)
    enqueue(100)
    print(queue)

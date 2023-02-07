#  global variable
size = int(input("Please Enter the queue's size : "))
queue = [None for _ in range(size)]
front, rear = -1, -1


def is_queue_empty():
    global queue, front, rear
    if front == rear:
        print("큐가 비었습니다.")
        return True
    else:
        return False


def is_queue_full():
    global queue, front, rear
    if rear == size - 1 and front == -1:
        print("큐가 가득찼습니다.")
        return True
    else:
        return False


def dequeue():
    global queue, front, rear
    if is_queue_empty():
        print("큐가 비어있습니다.")
        return None
    front = front + 1
    data = queue[front]
    queue[front] = None
    return data


def enqueue(data):
    global queue, front, rear
    if is_queue_full():
        print("큐가 가득찼습니다.")
        return None
    rear = rear + 1
    queue[rear] = data


def peek():
    global queue, front, rear
    if is_queue_empty():
        print("큐가 비어있습니다.")
        return None
    front = front + 1
    return queue[front]


if __name__ == "__main__":

    for i in range(size):
        enqueue(i)
        print("큐상태", queue)

    is_queue_full()

    for i in range(size):
        dequeue()
        print()
        print("큐상태", queue)


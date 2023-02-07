# # 응용 예제1.
#
# # global variable
# queue = ["정국", "뷔", "지민", "진", "슈가"]
# front, rear = 1, -4
#
#
# def is_queue_full():
#     """
#     대기 줄이 가득 찼는 지 안찼는지 boolean type으로 반환하고, 몇명의 대기자 수 가있는 지 반환한다.
#     :return: True or False
#     """
#     global queue, front, rear
#
#     if (rear == len(queue) - 1) and front == -1:
#         print("오늘 대기 접수는 마감했습니다.")
#         return True
#     else:
#         # count = 0
#         # if None in queue:
#         #     count = count + 1
#         # print(f"대기 접수 받겠습니다. 대기자 수는 {len(queue)-count}명 입니다.")
#         print("대기 접수 받겠습니다.")
#         return False
#
#
# # def is_queue_empty():
# #     global queue,front,rear
#
#
# def dequeue():
#     global queue, front, rear
#
#     print(f"대기줄 상태 : {queue}")
#     if queue[front] == None:
#         print("식당 영업 종료")
#         return
#     front = 0
#     print(f"{queue[front]} 님 식당에 들어감.")
#     queue[front] = None
#
#     for i in range(front + 1, len(queue)):
#         queue[i - 1] = queue[i]
#         queue[i] = None
#
#
# for _ in range(len(queue) + 1):
#     dequeue()
#


# 응용 예제 2
fix = "고장", 3
use = "사용 문의", 9
refund = "환불 문의", 4
etc = "기타 문의", 1

size = 5
queue = [None for _ in range(size)]
front, rear = 0, 0


def is_full_waiting():
    global queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False


def return_waiting_time(data):
    global queue, front, rear
    if is_full_waiting():
        print("프로그램 종료!")
        return
    rear = (rear + 1) % size
    queue[rear] = data

    waiting_time = 0
    for i in queue:
        if i is not None:
            waiting_time = waiting_time + i[1]
    if rear % size == size - 1:
        print(f"최종 대기 콜 -> {queue}")

    else:
        print(f"귀하의 현재 대기시간은 {waiting_time}입니다.")
        print(f"현재의 대기 콜 -> {queue}")
        print()


if __name__ == "__main__":
    return_waiting_time(fix)
    return_waiting_time(use)
    return_waiting_time(refund)
    return_waiting_time(etc)
    return_waiting_time(fix)

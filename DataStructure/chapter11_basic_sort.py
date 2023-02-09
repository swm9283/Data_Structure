#삽입 정렬 구현 기본 1.
import random
def find_index(array,data):
    find_index = -1 # data를 찾지 못했을 경우

    for i in range(0,len(array)):
        if array[i] > data:
            find_index = i
            break

    if find_index == -1 :
        return -1
    else:
        return find_index

before = [random.randint(0,200) for _ in range(10)]
print(f"정렬 전 : {before}")
after = []

for i in range(len(before)):
    data = before[i]
    inspos = find_index(after,data)
    after.insert(inspos,data)
print(f"정렬 후 : {after}")



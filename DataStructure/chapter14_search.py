# 응용 예제 1.
import random

# 매장 내의 상품 종류
product = ["레쓰비캔커피", "츄파춥스", "바나나맛우유", "도시락", "삼각김밥", "코카콜라"]

# 오늘 판매된 상품.
sell_product = [random.choice(product) for _ in range(21)]

# 중복을 제거한 상품
sell_unique_product = list(set(sell_product))  # 중복제거후 리스트화.


def count_selling_product(array, find_data):
    count = 0
    for i in range(len(array)):
        if array[i] == find_data:
            count += 1

    return [find_data, count]


result = []
for data in sell_unique_product:
    result.append(count_selling_product(sell_product, data))

print(f"오늘 판매된 상품은 {sell_product}입니다.\n")
print(f"오늘 판매된 목록은 {sell_unique_product}입니다.\n")
print(f"오늘 판매된 목록을 정렬한 결과 입니다. {sorted(sell_product)}")
print(f"오늘 판매된 물품 최종 결산입니다\n{result}")


def binary_search(ary, find_data):
    pos = -1
    start = 0
    end = len(ary) - 1
    while start <= end:
        mid = (start + end) // 2
        if ary[mid] == find_data:
            return mid
        elif ary[mid] < find_data:
            start = mid + 1
        else:
            end = mid - 1

    return pos

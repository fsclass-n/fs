# map(함수명, 반복가능객체)
# map은 함수와 반복 가능한 데이터를 입력으로 받는다.
# 입력받은 데이터의 각 요소에 함수를 적용한 결과를 반환
# map 함수는 map 객체를 반환한다.
# 기존 데이터를 새로운 데이터로 변환


# 1. 리스트를 입력받아 각 요소에 2를 곱해 반환하는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result) # [2,4,6,8]


# 2. map 사용
def two(x):
    return x * 2

print('-' * 30)
print(map(two, [1, 2, 3, 4])) # <map object at 0x000001DC0E34BFD0>
print(list(map(two, [1, 2, 3, 4]))) # [2, 4, 6, 8]


# 3. lambda 사용
print(list(map(lambda a: a*2, [1, 2, 3, 4]))) # [2, 4, 6, 8]
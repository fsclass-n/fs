# filter란 '무엇인가를 걸러 낸다'라는 뜻
# filter(함수명, 반복가능객체)
# 반복 가능한 데이터의 요소를 순서대로 함수에 전달하여
# 반환값이 참인 것만 묶어서 반환한다.


# positive는 리스트를 입력받아 각 요소를 판별해서 양수 값만 반환
def positive(lists):
    result = []
    for i in lists:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6])) # [1, 2, 6]


def pos(x):
    return x > 0

# list 함수는 filter 함수의 반환값을 리스트로 출력하기 위해 사용했다.
print(list(filter(pos, [1,-3,2,0,-5,6]))) # [1,2,6]


# lambda 사용
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))
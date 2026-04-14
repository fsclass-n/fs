def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)


# 매개변수가 없다.
def say():
    return "Hi"

a = say()
print(a)


# 반환값이 없는 경우
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))

add(3, 4)

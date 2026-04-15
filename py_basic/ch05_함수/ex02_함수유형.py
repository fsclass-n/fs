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

a = add(3, 4)
print(a)

def say():
    print("Hi")

say()

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)
print(result)


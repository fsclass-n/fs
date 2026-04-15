# 함수 정의
# 1. 매개변수 있고, 반환값도 있는 경우
def add(a, b):
    result = a + b
    print("더하기 완료!")
    return result
    # print("난 리턴 뒤에 기록했는데~") # 실행되지 않음

# 함수 호출
a = add(3, 4)
print(a) # 7


# 2. 매개변수 없고, 반환값이 있는 경우
def say():
    return "Hi"

a = say()
print(a) # Hi


# 3. 매개변수 있고, 반환값이 없는 경우
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    print(f"{a}, {b}의 합은 {a+b}입니다.")

a = add(3, 4)
print(a) # None


# 4. 매개변수 없고, 반환값도 없는 경우
def say():
    print("Hi")

say()


# 5. 매개변수의 순서와 상관없이 매개변수 이름을 지정하여 호출할 수 있다.
def sub(a, b):
    return a - b

result = sub(7, 3)
print(result) # 4

result = sub(a=7, b=3)
print(result) # 4

result = sub(b=3, a=7)
print(result) # 4


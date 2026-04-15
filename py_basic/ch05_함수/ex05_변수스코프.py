# 변수(variable)의 scope(스코프)

a = 1
def vartest(a):
    a += 1
    print(f"함수내의 a출력: {a}") # 2

vartest(a)
print(f"함수밖의 a출력: {a}") # 1


# global 키워드
b = 1
def vartest2():
    global b
    b += 1
    print(f"함수내의 b출력: {b}") # 2

vartest2()
print(f"함수밖의 b출력: {b}") # 2


# 리스트는 item(항목)이 변경 가능한(mutable) 자료형
# 리스트나 딕셔너리를 함수로 전달할 때는 원본이 변경될 수 있다.
def change_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
change_list(a)
print(a) # [1, 2, 3, 4]

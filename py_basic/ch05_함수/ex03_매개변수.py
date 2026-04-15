# 가변 매개변수

# 매개변수 앞에 *를 붙이면 가변 매개변수가 된다.
# 가변 매개변수는 함수에 전달된 인수들을 튜플로 만들어준다.
# *args -> (1, 2, 3)
def add_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add_many(1, 2, 3)) # 6
print(add_many(1, 2, 3, 4, 5)) # 15


# 일반 매개변수와 가변 매개변수를 함께 사용
# 가변 매개변수는 마지막에 사용한다.
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul("add", 1, 2, 3, 4, 5)) # 15
print(add_mul("mul", 1, 2, 3, 4, 5)) # 120


# 키워드(keyword) 매개변수
# 함수 호출 시 key=value 형태로 전달하는 매개변수를 받을 때
# 입력받은 키워드 매개변수들을 딕셔너리 형태로 출력
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a': 1}
print_kwargs(name='foo', age=3) # {'name': 'foo', 'age': 3}
print_kwargs(name='홍길동', age=25, city='서울', job='개발자')
# {'name': '홍길동', 'age': 25, 'city': '서울', 'job': '개발자'}

def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업='개발자')
'''
=== 프로필 정보 ===
이름: 김철수
나이: 30
직업: 개발자
'''



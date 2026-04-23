# 자료형 변환(Type Conversion)

# 자동(암시적) 형변환
num_int = 10
num_float = 1.5
result = num_int + num_float  
print(result) # 11.5 (float로 자동 변환)

# 강제(명시적) 형변환
# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환하는 함수이다.
# 정수가 입력되면 그대로 반환한다.
print(int('3')) # 3
print(int(3.6)) # 3
# int(x, radix)는 radix 진수로 표현된
# 문자열 x를 10진수로 변환하여 반환한다.
print(int('11', 2)) # 2진수 -> 10진수: 3
print(int('1A', 16)) # 16진수 -> 10진수: 26

# str
# str(object)는 객체를 문자열 형태로 변환하여 반환
print(str(3)) # 정수 -> 문자열: 3
print(str('hi')) # 문자열 -> 문자열: hi

# list
# list(iterable)는 반복 가능한 데이터를 입력받아 리스트로 만들어 반환
print(list("python")) # 문자열 -> 리스트: ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3))) # 튜플 -> 리스트: [1, 2, 3]

a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]

# tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 반환하는 함수
# 입력이 튜플인 경우에는 그대로 반환한다.
print(tuple("abc")) # 문자열 -> 튜플: ('a','b','c')
print(tuple([1,2,3])) # 리스트 -> 튜플: (1, 2, 3)
print(tuple((1,2,3))) # 튜플 -> 튜플: (1, 2, 3)

# chr
# character(문자)
# chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환
# 유니코드는 전 세계의 모든 문자를 컴퓨터에서
# 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준 코드이다.
print(chr(65)) # A
print(chr(97)) # a
print(chr(49)) # 1
print(chr(44032)) # 가

# ord
# ordinal(서수)
# ord(c)는 문자의 유니코드 숫자 값을 반환
print(ord('a')) # 97
print(ord('A')) # 65
print(ord('1')) # 49
print(ord('가')) # 44032


# 리스트를 셋으로 변환
my_list = [1, 2, 2, 3, 4, 4, 4]
my_set = set(my_list)
print(my_set)  # 결과: {1, 2, 3, 4}

# 문자열을 셋으로 변환
my_str = "apple"
print(set(my_str))  # 결과: {'a', 'p', 'l', 'e'} (순서는 랜덤)


# (Key, Value) 형태의 튜플들이 담긴 리스트
pair_list = [("name", "홍길동"), ("age", 30)]
my_dict = dict(pair_list)
print(my_dict)  # 결과: {'name': '홍길동', 'age': 30}

# 변수 대입하듯이 생성
my_dict = dict(apple=5, banana=10)
print(my_dict)  # 결과: {'apple': 5, 'banana': 10}
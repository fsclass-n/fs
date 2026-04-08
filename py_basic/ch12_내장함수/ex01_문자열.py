# 문자열 내장함수
# count('문자열'): 문자열의 개수
a = "hobby"
print(a.count('b')) # 2

# find('문자열'): 문자열의 위치
a = "Python is the best of best choice"
print(a.find('b')) # 14
print(a.find('k')) # -1

# index()
a = "Life is too short"
print(a.index('t')) # 8
# print(a.index('k')) # error

# A.join(B): B에 A를 삽입
print(",".join('abcd')) # a,b,c,d

# upper(): 대문자
a = 'Hi'
print(a.upper())
# lower(): 소문자
print(a.lower())

# 공백 제거
a = "   hello   "
# lstrip()
ls = a.lstrip()
print(ls)
print(len(ls))

# rstrip()
rs = a.rstrip()
print(rs)
print(len(rs))

# strip()
ss = a.strip()
print(ss)
print(len(ss))

# replace(old문자열, new문자열): 문자열 바꾸기
a = "Life is too short"
print(a.replace("short", "long"))

# split(['구분자'])
# 구분자 기본값은 공백이며, 리스트로 출력된다.
a = "Life is too short"
print(a.split()) # ['Life', 'is', 'too', 'short'] -> 리스트
b = "a,b,c,d"
print(b.split(",")) # ['a', 'b', 'c', 'd']

# 논리값 출력 함수
# 형태: isXXX()
# isalpha()
a = "Python"
print(a.isalpha()) # True
a = "Python3"
print(a.isalpha()) # False
a = "Hello Python!"
print(a.isalpha()) # False

# isdigit()
a = "12345"
print(a.isdigit()) # True
a = "12삼45"
print(a.isdigit()) # False
a = "12.45"
print(a.isdigit()) # False

a = "Life is too short"
# startwith('문자열'):
# 문자열로 시작하면 True, 아니면 False (대소문자 구별!)
print(a.startswith("Life i")) # True
# endwith()
print(a.endswith("ort")) # True











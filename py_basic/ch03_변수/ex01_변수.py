# 변수
# a, b, c를 변수라고 한다.
a = 1
b = "python"
c = [1, 2, 3]

# 변수 명명 규칙
'''
1. 영문자, 숫자, 언더스코어(_)만 사용!
2. 숫자로 시작x
3. 예약어x
4. 대소문자 구분
'''
# 올바른 예시
name = "홍길동"
user_name = "gil-dong"
userName = 'gilDong'
_private = "비공개"
count1 = 10

# 잘못된 예시
# 1name = "홍길동" # 첫 글자 숫자x
# user-name = '홍길동' # 하이픈x
# if = 10 # 예약어x

# 변수명(권장 사항)
'''
1. 의미가 명확한 이름 사용
2. 너무 짧거나 너무 긴 이름은 피한다.
3. snake_case 권장 (파이썬)
'''
# 예시
student_name = "김철수"
total_score = 95
user_age = 20

# 피해야할 예시
a = 100 # 의미 불명확
studentNameFormKorea = "김철수" # 너무 긴 이름

# 변수란? 객체를 가리키는 것
# 객체란? 자료형의 데이터(값)와 같은 것

# [1, 2, 3] 값을 가지는 리스트 객체가 메모리에 생성되고
# id는 변수가 가리키는 객체의 주소 값을 반환한다.
a = [1, 2, 3]
b = a
print(id(a)) # 2325963968896
print(id(b)) # 2325963968896

# 튜플로 a, b에 값을 대입할 수 있다.
a, b = ('python', 'java')
print(a) # python
print(b) # java

# 튜플은 괄호 생략 가능
a, b = 'python', 'java'
print(a) # python
print(b) # java

# 리스트
[a, b] = ['python', 'java']
print(a) # python
print(b) # java

# 여러 개의 변수에 같은 값 대입
a = b = 'python'
print(a) # python
print(b) # python

# 두 변수의 값 교환
a = 3
b = 5
a, b = b, a
print(a) # 5
print(b) # 3

# temp = a
# a = b
# b = temp
# print(a) # 5
# print(b) # 3







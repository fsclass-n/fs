# 제어문
'''
1. 조건문: 
    if~elif~else
    switch~case(x) -> 3.10+ match~case
2. 반복문: for, while
3. 기타: break, continue
'''

# if문
'''
    if 조건:
        print("택시 탄다.")
    else:
        print("걸어간다.")
'''
# 예) 돈(money)이 있으면 택시를 타고, 없으면 걸어간다.
money = 2000
card = True

# 조건문 다음에 콜론(:)
# 들여쓰기(indent)
if money > 3000 or card:
    print("택시")
    print("타고")
    print("간다.")
else:
    print("걸어간다.")

# in, not in
print(1 in [1, 2, 3]) # True
print(1 not in [1, 2, 3]) # False
print('a' in ['a', 'b', 'c']) # True
print('j' in 'python') # False
print('p' in 'python') # True

pocket = ['paper', 'phone', 'money']
if 'money' in pocket:
    print("택시 탄다")
else:
    print("걸어간다")

print("----------------------")
# pass: 조건문에서 아무 일도 하지 않게 설정(임시 조치)
pocket = ['paper', 'phone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어간다")


pocket = ['paper', 'phone', 'money']
card = True

if 'money' in pocket:
    print("택시 탄다")
else:
    if card:
        print("택시 탄다")
    else:
        print("걸어간다")

# elif
pocket = ['paper', 'phone', 'money']
card = True

if 'money' in pocket:
    print("택시 탄다")
elif card:
    print("택시 탄다")
else:
    print("걸어간다")

if 'money' in pocket: print("택시 탄다")
elif card: print("택시 탄다")
else: print("걸어간다")


# 성적 예시
grade = "B"

if grade == 'A':
    print("탁월함")
elif grade =='B':
    print("우수함")
elif grade == 'C':
    print("보통임")
else:
    print("노력 필요!")

# 파이썬 3.10+
# match~case
grade = 'B'
match grade:
    case 'A':
        print("탁월함")
    case 'B':
        print("우수함")
    case 'C':
        print("보통임")
    case _:
        print("노력 필요!")

# 합격/불합격
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격")
    case _:
        print("불합격")


# 연쇄 비교 연산자
x = 5
# x는 1보다 크고, 10보다 작다.
print(1 < x and x < 10) # True
print(1 < x < 10) # True


score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result) # 합격

# 조건부 표현식: 둘 중 하나
'''
    변수 = 참일때의값 if 조건 else 거짓일때의값
'''
score = 85
result = "합격" if score >= 60 else "불합격"
print(result) # 합격
# 문자열을 만드는 방법
print("Hello")
print('Hello')
print('''Life is too short, You need python''')
print("""Life is too short, You need python""")

# 문자열에 작은 따옴표 포함하기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰 따옴표 포함하기
food = '"Python favorite food" is perl'
print(food)

# 역슬래시(\)
food = '"Python\'s favorite food" is perl'
print(food)

# 줄바꿈(\n)
food = '"Python\'s favorite food"\n is perl'
print(food)

print('''Life is too short, 
      You need python''')
print("""
Life is too short, 
You need python
      """)

# 문자열 연산
head = "Python"
tail = '3.11.2'
# 문자열 연결(문자열 끼리만)
print(head + tail)

# 문자열 반복
print(head * 2)

# 문자열 길이(Length): len()
a = "Life is too short"
print(len(a)) # 17

# 문자열 인덱싱과 슬라이싱
# 인덱싱? ~을 가리킨다.
a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[-0]) # L
print(a[17]) # ,
print(a[-1]) # n
print(a[-2])
print(a[-5])

# 슬라이싱
a = "Life is too short, You need Python"
print(a[0:4]) # 0,1,2,3 -> 4이전, 4는 포함x
print(a[0:5])
print(a[0:2])
print(a[5:7]) # 5,6
print(a[12:17])

print("---------------------")
print(a[19:]) # 19부터 끝까지
print(a[:17]) # 처음부터 17이전
print(a[:]) # 모두 출력
print(a) # 모두 출력
print(a[19:-7])

# 슬라이싱으로 문자열 나누기
a = "20260406Sunny"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20260406Sunny"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year + "년")
print(day)
print(weather)

# 문자열 대체(i -> y)
a = "Pithon"
print(a[1]) # i
# a[1] = 'y'
# TypeError: 'str' object does not support item assignment
print(a[:1] + 'y' + a[2:])

# 문자열 포맷팅
'''
%d    정수(digit)
%f    실수(float)
%s    문자열(string)
'''
print("I eat %d apples." % 3)
print("I eat %s apples." % "three")

number = 3
print("I eat %d apples." % number)

# 두 개이상의 값을 넣으려면?
day = "three"
print("I eat %d apples. so I was sick for %s days" % (number, day))

# 특수문자 %로 지정하려면? %%
print("Error is %f%%." % 3.5)
print("Error is %.")

# 포맷 코드와 숫자 함께 사용하기
print("0123456789")
print("%10s" % "hi")
print("%-10sjane." % "hi")

# 소수점 표현
print("%0.4f" % 3.141542) # 소수점이하 4자리까지 표시(반올림)
print("0123456789")
print("%10.4f" % 3.141542)


### v2.6+ format() 메서드
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 3
day = "five"
print("I eat {0} apples".format(number))
print("I eat {0} apples. so I was sick for {1} days".format(number, day))

print("I eat {0} apples. so I was sick for {1} days".format(day, number))
print("I eat {1} apples. so I was sick for {0} days".format(number, day))

# 이름으로 넣기
print("I eat {number} apples. so I was sick for {day} days".format(number=3, day="five"))
print("I eat {0} apples. so I was sick for {day} days".format(3, day="five"))

# 정렬(왼쪽, 오른쪽, 가운데)
print("0123456789")
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

# 특정 문자로 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현
y = 3.141592
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# 특수 문자 { } 표시하기
print("{{ and }}".format()) # { and }


### v3.6+ f문자열 포맷팅
name = '홍길동'
age = 30
print('나의 이름은 {name}입니다. 나이는 {age}입니다.'.format(name='김길동', age=24))
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

print(f'나는 내년이면 {age+1}살이 된다.')


### 딕셔너리
d = {'name':'홍길동', 'age':30}
print(d)
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")

# 정렬
print(f'{"hi":<10}') # 왼쪽
print(f'{"hi":>10}') # 오른쪽
print(f'{"hi":^10}') # 가운데

# 공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

# 소수점
y = 3.141592
print(f'{y:0.4f}')
print(f'{y:10.4f}')

# { } 표시
print(f'{{ and }}')

# 천단위 표시
print(f"난 {1500000:,}원이 필요해!")

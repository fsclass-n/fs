# 리스트(list, 목록)
odd = [1, 3, 5, 7, 9] # 홀수 목록
a = []
print(a)
a = list()
print(a)
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


### 인덱싱
b = [1, 2, 3]
print(b[0]) # 1
print(b[0] + b[2]) # 1+3 -> 4
print(b[-1]) # 3

e = [1, 2, 3, ['a', 'b', 'c']]
print(e[0]) # 1
print(e[-1]) # ['a', 'b', 'c']
print(e[3]) # ['a', 'b', 'c']

print(e[-1][0]) # a
print(e[3][1]) # b
print(e[-1][2]) # c

e = [1, 2, 3, ['a', 'b', ['Life', 'is']]]
# Life를 출력하려면?
print(e[3][2][0])
print(e[-1][-1][-2])


### 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2]) # [1, 2]
print(a[:2]) # [1, 2]
print(a[2:]) # [3, 4, 5]
print(a[:]) # [1, 2, 3, 4, 5]
print(a) # [1, 2, 3, 4, 5]

e = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(e[2:5]) # [3, ['a', 'b', 'c'], 4]


### 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(a)) # 3

# 숫자끼리는 덧셈, 문자끼리는 연결
# 숫자와 문자를 더하면? error
a = [1, 2, '3']
print(a[2] + 'hi') # 3hi
a = [1, 2, 3]
print(str(a[2]) + 'hi') # 3hi


### 리스트의 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a) # [1, 2, 4]

del a[1]
print(a) # [1, 4]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]


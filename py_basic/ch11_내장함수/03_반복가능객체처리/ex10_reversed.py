# reversed(squence) 함수

# 리스트 뒤집기
numbers = [1, 2, 3, 4, 5]
rev_numbers = reversed(numbers)

print(list(rev_numbers)) 
# 출력: [5, 4, 3, 2, 1]


# 문자열 뒤집기
text = "Python"
rev_text = reversed(text)

print("reversed text:", rev_text)
# <reversed object at 0x00000298F6F6BA60>
# print(list(rev_text))
# ['n', 'o', 'h', 't', 'y', 'P']
a = "".join(rev_text)
print(a) # nohtyP
print(type(a)) # <class 'str'>
print(rev_text) 
# <reversed object at 0x000002ACBAF2BA60>
print(list(rev_text)) # []
b = "-".join(a)
print(b) # n-o-h-t-y-P


# 반복문(for)에서의 활용
fruits = ["사과", "배", "포도"]

for fruit in reversed(fruits):
    print(fruit)

# 출력:
# 포도
# 배
# 사과
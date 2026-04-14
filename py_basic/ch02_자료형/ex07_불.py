# boolean(불)
a = True
b = False

# type(): 타입 확인
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

# 자료형의 False
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))
print(bool(None))

# 자료형의 True
print(bool("Python"))
print(bool([1, 2, 3]))
print(bool(3))
print(bool(-3))
print(bool(3.14))

# 비교 연산의 결과는 True 또는 False
print(1 == 1) # True
print(1 != 1) # False
print(2 < 1) # False
print(2 > 1) # True
print(2 >= 1) # True
print(2 <= 1) # False

# 논리 연산의 결과도 True 또는 False
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True

# 논리/비교 활용 예시
x = 5
y = 10
print(x > 0 and y > 0) # True
print(x > 10 or y > 5) # True
print(not (x > y)) # True


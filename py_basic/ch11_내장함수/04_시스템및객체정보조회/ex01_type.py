# type
# type(object)는 입력값의 자료형이 무엇인지 알려 주는 함수

print(type(123))
print(type(12.3))
print(type("abc"))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({1: 'a', 2: 'b', 3: 'c'}))
print(type(True))
print(type(range(10)))
print(type(open("test", 'w')))

'''
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
<class 'bool'>
<class 'range'>
<class '_io.TextIOWrapper'>
'''
# isinstance(object, class)
# isinstance 함수는
# 입력받은 객체가 해당 클래스의 인스턴스인지 판단하여
# 참이면 True, 거짓이면 False를 반환

class Person: 
    pass

a = Person()
print(isinstance(a, Person)) # True

b = 3
print(isinstance(b, Person)) # False


print(isinstance("123", str)) # True
print(isinstance(123, str)) # False
print(isinstance(123, int)) # True
print(isinstance("123", int)) # False


# calculator.py
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num  # 결괏값(result)에 입력값(num) 더하기
    return result1  # 결괏값 반환

def add2(num):
    global result2
    result2 += num  # 결괏값(result)에 입력값(num) 더하기
    return result2  # 결괏값 반환

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 클래스
# 클래스(class)란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    def add(self, num):
        self.result -= num
        return self.result

# 객체: calc1, calc2
# 객체(object)란 클래스로 만든 피조물(과자 틀로 찍어 낸 과자)을 뜻한다.
# 객체마다 고유한 성격을 가진다.
# 클래스로 만든 객체를 '인스턴스'라고도 한다.
# a = Cookie()
# a는 객체이다.
# a는 Cookie 클래스로 만든 인스턴스이다.

calc1 = Calculator()
calc2 = Calculator()

print(calc1.add(3))
print(calc1.add(4))
print(calc2.add(3))
print(calc2.add(7))


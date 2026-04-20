# 사칙연산 클래스

# 1. 클래스를 어떻게 만들지 먼저 구상하기
'''
1. 클래스명: FourCal
2. 메서드명
    setdata() : 두 개의 수를 지정
    add() : 두 수의 합
    sub() : 두 수의 차
    mul() : 두 수의 곱
    div() : 두 수의 나머지

    a = FourCal()
    a.setdata(4, 2)
    a.add() -> 6
    a.sub() -> 2
    a.mul() -> 8
    a.div() -> 2.0
'''

# 2. 클래스 구조 만들기
# 클래스 안에 구현된 함수는 다른 말로 메서드(method)라고 부른다.
# 메서드의 첫 번째 매개변수 self는 특별한 의미를 가진다. 매개변수 이름은 관례적으로 self를 사용한다. 객체의 메서드를 호출할 때 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용한 것이다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# 3. 객체 만들기
a = FourCal()
b = FourCal()
print(type(a)) # <class '__main__.FourCal'>
# 객체 a가 FourCal 클래스의 인스턴스임을 알 수 있다.

# '객체.메서드' 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
a.setdata(4, 2)
b.setdata(3, 7)
# '클래스명.메서드' 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해야 한다
# FourCal.setdata(a, 4, 2)

# 객체에 생성되는 객체변수를 '인스턴스 변수' 또는 '속성'이라고도 부른다.
print(a.first) # 4
print(a.second) # 2
print(b.first) # 3
print(b.second) # 7

print('-' * 30)
print(a.add()) # 6
print(a.sub()) # 2
print(a.mul()) # 8
print(a.div()) # 2.0

print(b.add()) # 10
print(b.sub()) # -4
print(b.mul()) # 21
print(b.div()) # 0.42857142857142855
class FourCal:
    # 생성자
    def __init__(self, first, second):
        # 인스턴스(객체) 변수
        self.first = first
        self.second = second

    # 메서드(method)
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# 상속(Inheritance)이란 
# '물려받다'라는 뜻
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
'''
    class 클래스_이름(상속할_클래스_이름):
        pass
'''
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add()) # 6
print(a.mul()) # 8
print(a.sub()) # 2
print(a.div()) # 2.0
print(a.pow()) # 16

# 내장 함수
print('-' * 30)
print(pow(2, 3)) # 8
print(2 ** 3) # 8
print(pow(10, -1)) # 0.1
print(pow(2, 10, 7)) # 2**10 % 7 -> 2

# 파이썬은 다중 상속 가능
class Mother:
    def skill(self):
        print('요리 실력')

class Father:
    def hobby(self):
        print('축구 시청')

class Child(Mother, Father):
    def game(self):
        print('게임 시청')

c = Child()
c.skill() # 요리 실력
c.hobby() # 축구 시청
c.game() # 게임 시청
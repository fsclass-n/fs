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

a = FourCal(4, 0)
# a.div() # ZeroDivisionError: division by zero

# 메서드 재정의(overriding)
class SafeFourCal(FourCal):
    def div(self):
        # 나누는 값이 0인 경우 0을 반환
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div()) # 0
b = SafeFourCal(4, 2)
print(b.div()) # 2.0
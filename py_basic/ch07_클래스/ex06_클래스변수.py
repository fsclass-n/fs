# 클래스 변수
class Family:
    # 클래스 변수는 클래스 안에 변수를 선언하여 생성한다.
    lastname = "홍"

# 클래스_이름.클래스변수로 사용
print(Family.lastname) # 홍

# 객체변수
a = Family()
b = Family()
print(a.lastname) # 홍
print(b.lastname) # 홍

# 클래스변수와 객체변수
Family.lastname = "김"
print(a.lastname) # 김
print(b.lastname) # 김

# 객체변수와 클래스변수
# a 객체에 lastname이라는 객체변수가 새롭게 생성된다.
a.lastname = "이"
print(a.lastname) # 이
print(Family.lastname) # 김
print(b.lastname) # 김
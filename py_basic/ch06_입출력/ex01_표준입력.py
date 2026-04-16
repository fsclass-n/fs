# 표준 입력
# input()
# int() : 문자열을 정수로 변환
a = input("나이를 입력하세요: ")
print(type(a))  # <class 'str'>
print("30년 후 나이는 %d입니다" % (int(a) + 30))

# 실수로 변환
# float(): 문자열을 실수로 변환
# 1m = 100cm
height = float(input("키를 입력하세요(cm): "))
height /= 100
print("미터로 환산하면 %0.2f(m)입니다" % height)
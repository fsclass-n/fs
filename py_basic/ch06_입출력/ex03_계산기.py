# 사칙연산 계산기
print("=== 간단한 계산기 ===")

# 사용자로부터 두 숫자 입력받기
num1 = int(input("숫자1: "))
num2 = int(input("숫자2: "))

# 계산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")
    
'''
=== 간단한 계산기 ===
숫자1: 15
숫자2: 25
15 + 25 = 40
15 - 25 = -10
15 * 25 = 375
15 / 25 = 0.6
'''
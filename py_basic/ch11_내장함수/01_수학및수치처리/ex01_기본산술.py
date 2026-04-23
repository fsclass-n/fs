# abs
# abs(x)는 숫자를 입력받아 그 숫자의 절댓값을 반환
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

# divmod
# divmod(a, b)는 2개의 숫자 a, b를 입력으로 받아
# a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7,3)) # (2, 1)
print(7 // 3) # 2 (몫)
print(7 % 3) # 1 (나머지)

# pow
# pow(x, y)는 x를 y제곱한 결괏값을 반환
print(pow(2, 4)) # 16
print(pow(3, 3)) # 27
print(2 ** 4) # 2*2*2*2 -> 16
print(pow(2, 4, 3)) # 2*2*2*2 % 3 -> 1
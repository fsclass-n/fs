# round
# round(number [,ndigits])는 숫자를 입력받아 반올림해 반환
import math


print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(2.5)) # 2
print(round(3.5)) # 4
print(round(5.678, 2)) # 5.68


# ctrl+.
n = 2.556

print(round(n, 2))   # 2.56 (소수점 둘째자리까지 반올림)
print(math.ceil(n))   # 3
print(math.floor(n))  # 2
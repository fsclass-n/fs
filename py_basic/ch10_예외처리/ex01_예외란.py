# 예외 ?
# 프로그램에서 자주 발생하는 오류

# f = open("나없는파일", 'r')

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

# print(4 / 0)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero


a = [1, 2, 3]
print(a[3])

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

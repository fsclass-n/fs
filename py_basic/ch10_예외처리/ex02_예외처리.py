# 오류 예외 처리 기법
'''
try:
    실행 코드
except [발생오류 [as 오류변수]]:
    실행 코드
except [발생오류 [as 오류변수]]:
    실행 코드
    ...
else:
    오류가 없을 경우에만 수행할 코드
finally:
    실행 코드

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
'''

try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # division by zero


# try_finally.py
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    #(... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.

try:
    print("나누기 전")
    4 / 0
    print("나누기 후")
except ZeroDivisionError:
    print("오류가 발생했습니다.")
finally:
    print("finally 실행!")


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


print('-' * 30)
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e) # list index out of range


try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e) # list index out of range


# try ~ else
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

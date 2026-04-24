# eval('expression')
# eval 함수는 문자열로 구성된 표현식을 입력으로 받아
# 해당 문자열을 실행한 결괏값을 반환
# eval은 입력 문자열을 실제로 실행하므로,
# 신뢰할 수 없는 외부 입력에는 사용하면 안 된다.

print(eval('1+2')) # 3
print(type(eval('1+2'))) # <class 'int'>
print(eval("'hi' + 'a'")) # hia
print(eval('divmod(4, 3)')) # (1, 1)
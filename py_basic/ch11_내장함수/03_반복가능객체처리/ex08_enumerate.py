# enumerate
# enumerate는 '열거하다'라는 뜻이다.
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 반환
# 보통 enumerate 함수는 for 문과 함께 사용한다.
# 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

for idx, val in enumerate(['body', 'foo', 'bar']):
    print(idx, val)
'''
0 body
1 foo
2 bar
'''
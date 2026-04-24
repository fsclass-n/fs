# any(iterable)
# any 함수는 반복 가능한 데이터 iterable를 입력으로 받아
# iterable의 요소 중 하나라도 참이 있으면 True를 반환하고,
# iterable가 모두 거짓일 때만 False를 반환한다.

print(any([1, 2, 3, 0])) # True
print(any([0, ""])) # False
print(any([])) # False

print(all([1, 2, 3, 0])) # False
print(all([0, ""])) # False
print(all([])) # True
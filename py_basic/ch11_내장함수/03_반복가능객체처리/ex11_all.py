# all(iterable)
# all() 함수는 반복 가능한 데이터 iterable를 입력값으로 받아
# iterable의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 반환한다.

print(all([1,2,3])) # True

# 요소 0은 거짓
print(all([0,2,3])) # False

print('-' * 30)
# all의 입력 인수가 빈 값인 경우에는 True를 반환한다.
print(all("")) # True
print(all([])) # True
print(all(())) # True
print(all({})) # True
print(all(set())) # True

print('-' * 30)
# False 자료: 0, "", [], (), {}, set(), None
# 나머지는 모두 True
print(all([0])) # False
print(all([""])) # False
print(all([" "])) # True
print(all([[]])) # False
print(all([()])) # False
print(all([{}])) # False
print(all([set()])) # False
print(all([None])) # False

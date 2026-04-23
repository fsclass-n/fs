# set 내장 함수
# add(): 요소 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1) # {1, 2, 3, 4}

# update(): 여러 요소 추가
# s1.add([5, 6, 7]) # TypeError
s1.update([5, 6, 7])
print(s1) # {1, 2, 3, 4, 5, 6, 7}

# remove(): 특정 값 제거
s1 = set([10, 20, 30])
s1.remove(20)
print(s1) # {10, 30}
# s1.remove(40) # KeyError
print(s1)

# discard(): 특정 값 제거
s1 = set([10, 20, 30])
s1.discard(20)
print(s1) # {10, 30}
s1.discard(40)
print(s1) # {10, 30}

# clear(): 모든 값 제거
s1 = set([10, 20, 30])
s1.clear()
print(s1) # set()
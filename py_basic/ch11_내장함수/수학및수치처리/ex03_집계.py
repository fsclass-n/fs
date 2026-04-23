# sum
# sum(iterable)은 입력 데이터의 합을 반환
print(sum([1,2,3])) # 6
print(sum((4,5,6))) # 15
print(sum({4,5,6})) # 15
print(sum({4:"a", 5:"b", 6:"c"})) # 15
print('-'*50)


# max
# max(iterable)는 반복 가능한 데이터를 입력받아 최댓값을 반환
print(max([1,2,3])) # 3
print(max("python")) # y
print(max("파이썬")) # 파

# min
# min(iterable)는 max 함수와 반대로,
# 반복 가능한 데이터를 입력받아 최솟값을 반환
print(min([1,2,3])) # 1
print(min("python")) # h
print(min("파이썬")) # 썬


import numpy as np

data = [10, 20, 20, 30, 1000] # 1000이라는 이상치가 포함됨

print(f"산술 평균: {np.mean(data)}")   # 216.0 (이상치 때문에 높게 나옴)
print(f"중앙값: {np.median(data)}")     # 20.0 (실제 데이터의 중심을 더 잘 반영)
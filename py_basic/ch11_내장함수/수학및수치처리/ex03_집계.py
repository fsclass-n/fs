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

data = [10, 20, 20, 25, 30, 1000] # 1000이라는 이상치가 포함됨

print(f"산술 평균: {np.mean(data)}")   # 216.0 (이상치 때문에 높게 나옴)
print(f"중앙값: {np.median(data)}")     # 22.5 (실제 데이터의 중심을 더 잘 반영)

'''
산술 평균: 184.16666666666666
중앙값: 22.5
'''

from scipy import stats
import numpy as np

data = [10, 30, 30, 20, 20, 1000]
mode_result = stats.mode(data, keepdims=True)

print(f"최빈값: {mode_result.mode}") # [20]
print(f"최빈값: {mode_result.mode[0]}") # 20
print(f"출현 횟수: {mode_result.count[0]}") # 2

'''
최빈값: 20
출현 횟수: 2
'''

import pandas as pd

data = [10, 30, 30, 20, 20, 1000]
series = pd.Series(data)

print(f"최빈값: {series.mode()}")
print(f"최빈값: {series.mode()[0]}")
print(f"최빈값: {series.mode()[1]}")
'''
최빈값: 0    20
1    30
dtype: int64
최빈값: 20
최빈값: 30
'''

import statistics

data = [10, 20, 20, 30, 30, 1000]
print(f"최빈값: {statistics.mode(data)}") # 20

# 모든 최빈값을 리스트로 반환
all_modes = statistics.multimode(data)

print(all_modes)      # [20, 30]
print(all_modes[0])   # 20
print(all_modes[1])   # 30 (이제 [1] 사용 가능!)
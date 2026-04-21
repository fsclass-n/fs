import sys, os

# 1. 현재 파일의 절대 경로
current_dir = os.path.dirname(__file__)
print(current_dir)
# d:\wi\git\fs\py_basic\ch08_모듈\other\ex04_모듈사용.py

# 2. 한 단계 위 폴더 경로 생성
parent_dir= os.path.join(current_dir, '..')
print(parent_dir)
# d:\wi\git\fs\py_basic\ch08_모듈\other\..

# 3. 경로를 절대 경로로 변환하여 추가
sys.path.append(os.path.abspath(parent_dir))

import mod1

print(mod1.add(3, 4)) # 7
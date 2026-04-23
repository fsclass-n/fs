# 오류 회피하기
# 코드를 작성하다 보면 특정 오류가 발생해도 그냥 통과시켜야 할 때
# 여러 파일을 처리하는 중에 일부 파일이 없더라도 프로그램을 계속 실행하고 싶을 때

# import os

# # 현재 실행 중인 파일(ex03_오류회피.py)의 절대 경로를 가져온다.
# current_dir = os.path.dirname(__file__)
# print(current_dir)
# # d:\wi\git\fs\py_basic\ch10_예외처리

# students = ["김철수", "이영희", "박민수", "최유진"]

# for student in students:
#     # 현재 폴더 경로와 파일명을 결합
#     file_path = os.path.join(current_dir, f"{student}_성적.txt")

#     try:
#         with open(file_path, 'r', encoding="utf-8") as f:
#             score = f.read()
#             print(f"{student}의 성적: {score}")
#     except FileNotFoundError:
#         print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
#         continue  # 다음 학생으로 넘어감


# 파이썬 3.4+
from pathlib import Path

students = ["김철수", "이영희", "박민수", "최유진"]

# 현재 파일의 위치를 기준으로 경로 설정
current_dir = Path(__file__).parent
print(current_dir)
# d:\wi\git\fs\py_basic\ch10_예외처리

for student in students:
    # / 연산자를 통해 경로를 합친다.
    file_path = current_dir / f"{student}_성적.txt"

    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue  # 다음 학생으로 넘어감

'''
김철수의 성적: 90점
이영희의 성적 파일이 없습니다. 건너뜁니다.
박민수의 성적: 95점
최유진의 성적 파일이 없습니다. 건너뜁니다.
'''

# 오류를 완전히 무시하고 싶을 때
try:
    # 설정 파일을 읽으려 시도
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass  # 설정 파일이 없어도 계속 진행

# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")

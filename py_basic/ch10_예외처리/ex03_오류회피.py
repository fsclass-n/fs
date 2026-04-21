# # 오류 회피하기
# import os

# # 현재 실행 중인 파일(ex03_오류회피.py)의 절대 폴더 경로를 가져옵니다.
# current_path = os.path.dirname(os.path.abspath(__file__))

# students = ["김철수", "이영희", "박민수", "최유진"]

# for student in students:
#     # 현재 폴더 경로와 파일명을 안전하게 결합
#     file_path = os.path.join(current_path, f"{student}_성적.txt")

#     try:
#         with open(file_path, 'r', encoding="utf-8") as f:
#             score = f.read()
#             print(f"{student}의 성적: {score}")
#     except FileNotFoundError:
#         print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
#         continue  # 다음 학생으로 넘어감


# 파이썬 3.4부터 권장되는 방식
from pathlib import Path
students = ["김철수", "이영희", "박민수", "최유진"]

# 현재 파일의 위치를 기준으로 경로 설정
base_path = Path(__file__).parent

for student in students:
    # / 연산자로 경로를 쉽게 합칠 수 있음
    file_path = base_path / f"{student}_성적.txt"
    
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("파일 없음")
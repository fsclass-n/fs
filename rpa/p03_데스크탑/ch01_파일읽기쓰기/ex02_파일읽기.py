from pathlib import Path


# 홈 디렉토리에 샘플 파일 생성
home_path = Path.home()
todo_file = home_path / "문서" / "할일.txt"
print(todo_file)
# C:\Users\pc06-00\문서\할일.txt

# vscode 작업 영역 폴더 안에 샘플 파일 생성
work_dir = Path.cwd()
todo_file = work_dir / "문서" / "할일.txt"
print(todo_file)
# D:\wi\git\fs\문서\할일.txt

# 현재 코드(py)가 있는 폴더 안에 샘플 파일 생성
cur_dir = Path(__file__).parent
print(cur_dir)
# d:\wi\git\fs\rpa\p03_데스크탑\ch01_파일읽기쓰기
todo_file = cur_dir / "문서" / "할일.txt"

# 디렉토리 생성
# parents=True: 중간 단계의 폴더가 없어도 한꺼번에 모두 생성합니다. (예: A/B/C 경로에서 A, B가 없어도 생성)
# exist_ok=True: 이미 폴더가 존재하더라도 에러를 발생시키지 않고 넘어갑니다.
todo_file.parent.mkdir(parents=True, exist_ok=True)

# 파일 생성
# 파일 쓰기
# open(파일명, "모드", 엔코딩)
with open(todo_file, "w", encoding="utf-8") as f:
    f.write("장보기\n공부하기\n운동하기\n")

# 파일 읽기
with open(todo_file, "r", encoding="utf-8") as f:
    content = f.read()
    print("파일 내용:", content)

'''
파일 내용: 장보기
공부하기
운동하기
'''

with open(todo_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("줄단위 읽기:", lines)

'''
줄단위 읽기: ['장보기\n', '공부하기\n', '운동하기\n']
'''
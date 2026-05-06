'''
윈도우: "c:\\", r"c:\", "c:/"
맥, 리눅스: /users/home/...

내장 모듈: pathlib
1. Path.cwd()
2. Path.home()
3. Path.cwd() / "경로" / "파일"
또는 Path.home() / "경로" / "파일"
4. Path("경로/파일") -> 상대 경로
5. Path("경로/파일").resolve() -> 절대경로
6. 경로 속성: name(파일), stem(파일명), suffix(확장자), parent(경로), drive(드라이브)
7. Path("경로/파일").exists() -> 파일 존재 여부
'''

from pathlib import Path

# vscode의 작업 영역 폴더
# Path.cwd(): Current Working Directory
cur_dir = Path.cwd()
print("작업 영역 폴더: ", cur_dir)
# 작업 영역 폴더:  D:\wi\git

# 홈 디렉토리
home_dir = Path.home()
print("홈 디렉토리: ", home_dir)
# 홈 디렉토리:  C:\Users\pc06-00

# 경로 이어 붙이기
# 폴더와 파일 구분자: /
보고서_dir = cur_dir / "문서" / "보고서.txt"
print("보고서 경로1: ", 보고서_dir)
# 보고서 경로1:  D:\wi\git\문서\보고서.txt
보고서_dir = home_dir / "문서" / "보고서.txt"
print("보고서 경로2: ", 보고서_dir)
# 보고서 경로2:  C:\Users\pc06-00\문서\보고서.txt

# 상대경로 -> 절대 경로
rel_path = Path("data/학생명단.txt")
print("상대 경로: ", rel_path)
# 상대 경로:  data\학생명단.txt
print("절대 경로: ", rel_path.resolve())
# 절대 경로:  D:\wi\git\data\학생명단.txt

# 경로 속성
sample_file = Path("c:/users/홍길동/음악/노래.mp3")
print("파일 이름:", sample_file.name)
# 파일 이름: 노래.mp3
print("확장자:", sample_file.suffix)
# 확장자: .mp3
print("파일명만:", sample_file.stem)
# 파일명만: 노래
print("디렉토리:", sample_file.parent)
# 디렉토리: c:\users\홍길동\음악
print("드라이브:", sample_file.drive)
# 드라이브: c:

# 파일 존재 여부
# 파일이 존재하면 True, 존재하지 않으면 False
print("파일 존재 여부: ", sample_file.exists())
# 파일 존재 여부:  False

'''
중간 파일을 지운 후 새로운 파일이 생길 경우
a_1.txt
a_2.txt
a_3.txt
에서 a_2.txt를 지운 후에 새로운 파일 a_2.txt가 생기면

a_1.txt
a_2.txt -> 최근에 생긴 파일이 중간에 들어감
a_3.txt

새로운 파일 a_2.txt가 생기면
a_3.txt를 a_2.txt로 바꾸고, a_2.txt를 a_3.txt로 지정

파일 정렬 시
a_1.txt
a_2.txt
a_3.txt
a_11.txt 가 생기면

a_1.txt
a_11.txt
a_2.txt
a_3.txt 가 되므로

a_001.txt
a_002.txt
a_003.txt
a_011.txt
'''

# a = 1
# s = str(a).zfill(3)
# print(s) # 001

import shutil
from pathlib import Path

def renumber(folder: Path, prefix: str = "spam", ext: str = ".txt"):
    # folder.mkdir(parents=True, exist_ok=True)

    files = sorted(folder.glob(f"{prefix}[0-9][0-9][0-9]{ext}")) 
    # spam???.txt

    temps = []

    # for f in files:
    for i, f in enumerate(files, start=1):
        print(f"{i}/{f}")
        tmp = folder / f"__tmp_{i}{ext}"
        print(f"{tmp}")
        shutil.move(f, tmp)
        temps.append(tmp)
    
    for i, tmp in enumerate(sorted(temps), start=1):
        new = folder / f"{prefix}{str(i).zfill(3)}{ext}"
        shutil.move(str(tmp), str(new))
        print(f"[이름정리]{new.name}")


if __name__ == "__main__":
    base = Path(__file__).parent / "연습" / "번호정리"
    base.mkdir(parents=True, exist_ok=True)

    renumber(base)
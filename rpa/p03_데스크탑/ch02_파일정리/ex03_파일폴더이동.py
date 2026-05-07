import shutil
from pathlib import Path


def move_to_folder(base:Path):
    src = base / "spam" / "file1.txt"
    dst_folder = base / "spam2"
    dst_folder.mkdir(parents=True, exist_ok=True)

    # 폴더 이동
    new_path = shutil.move(src, dst_folder)
    print("[move-폴더] => ", new_path)
    # [move-폴더] =>  d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam2\file1.txt


def move_to_rename(base:Path):
    src = base / "spam" / "file3.txt"

    dst_path = base / "spam2" / "file3.txt"
    new_path = shutil.move(src, dst_path)
    print("[move-rename] => ", new_path)
    # 이동과 이름바꾸기
    # [move-rename] =>  d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam2\new_name.txt
    
    # 이름바꾸기
    # [move-rename] =>  d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\new_name.txt


# 현재 파일이 실행: __name__ = "__main__"
# 외부에서 현재 파일을 호출: __name__ = "ex03_파일폴더이동"
if __name__ == "__main__":
    base = Path(__file__).parent / "연습"

    # 파일 이동
    # move_to_folder(base)
    # 파일 이동 및 이름 바꾸기
    move_to_rename(base)
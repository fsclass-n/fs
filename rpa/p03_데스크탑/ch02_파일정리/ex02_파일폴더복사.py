# shutil.copy(src, dst)
# shutil.copyfile(src, dst)
# shutil.copytree(src, dst)

import shutil
from pathlib import Path

def copy_file_example(base:Path):
    src_file = base / "spam" / "file1.txt"

    # 디렉토리에 복사 (dst => 디렉토리)
    # shutil.copy(src, dst): src를 dst에 복사
    copied1 = shutil.copy(src_file, base)
    print("결과1:", copied1)
    # 결과1: d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\file1.txt

    # 파일명 지정 복사
    copied2 = shutil.copyfile(src_file, base / "spam" / "file2.txt")
    print("결과2:", copied2)
    # 결과2: d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file2.txt


def copy_tree_example(base:Path):
    # spam 디렉토리 전체를 spam_backup으로 복사
    dst = base / "spam_backup"

    # 만약 폴더가 존재하면 True, 아니면 False
    if dst.exists():
        # 폴더/파일 삭제
        shutil.rmtree(dst)

    copied_tree = shutil.copytree(base / "spam", dst)
    print("copy tree 결과:", copied_tree)
    # copy tree 결과: d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam_backup


if __name__ == "__main__":
    base = Path(__file__).parent / "연습"

    copy_file_example(base)
    copy_tree_example(base)
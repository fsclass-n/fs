'''
객체.메서드()
base.resolve() -> 메서드 -> 이유: base는 객체
os.walk() -> 함수 -> 이유: os.py는 모듈

open() -> 함수

os.path.getsize()
'''
import os
from pathlib import Path

def find_big_files(base: Path, size_kb: int = 100):
    # 절대 경로
    print(base)
    # d:\wi\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습
    base = base.resolve()
    print(base)
    # D:\wi\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습
    
    size_bytes = size_kb * 1024

    for folder, _, files in os.walk(base):
        p = Path(folder)
        for name in files:
            fp = p / name

            try:
                size = fp.stat().st_size
            except OSError:
                continue

            if size > size_bytes:
                mb = round(size / (1024 * 1024), 1)
                print(f"[대용량] {fp} - {mb} MB")


if __name__ == '__main__':
    base = Path(__file__).parent / "연습"

    find_big_files(base, size_kb = 100)
import os
from pathlib import Path

def make_sample(root: Path):
    # 폴더 생성
    (root / 'spam').mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs" / "bacon").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs2").mkdir(parents=True, exist_ok=True)

    for f in ["spam/file1.txt", "spam/file2.txt", "spam/eggs/file3.txt", "spam/eggs/bacon/file4.txt"]:
        (root / f).write_text("Hello", encoding="utf-8")

def show_list_str(root:Path):
    # 첫 번째 방법: os.listdir -> 경로를 문자열로 변환
    full_path = str(root / "spam")
    print(f"{full_path} 목록 :")
    # d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam 목록 :
    for p in os.listdir(full_path):
        print(p)
        '''
            eggs
            eggs2
            file1.txt
            file2.txt
        '''

def show_list_path(root:Path):
    # 두 번째 방법: Path.iterdir() -> 경로 자체(문자열 변환x)
    full_path = root / "spam"
    print("-"*80)
    print(full_path.iterdir())
    # <generator object Path.iterdir at 0x000002229B321460>
    print("-"*80)

    for p in full_path.iterdir():
        # 만약 폴더이면 True, 아니면 False 
        if p.is_dir():
            print(f"[{p}]")
        else:
            print(f"{p}")
        '''
            [d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs]
            [d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs2]
            d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file1.txt
            d:\wi\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file2.txt
        '''

# if __name__ == "__main__":
# - "이 파일이 직접 실행된 것인지, 아니면 다른 파일에 의해 불러와진(import) 것인지 구분하는 역할"을 합니다.
# __name__: 현재 실행 중인 모듈(파일)의 이름

if __name__ == "__main__":
    base = Path(__file__).parent / "연습"

    make_sample(base)
    show_list_str(base)
    show_list_path(base)
# zip 파일 만들기
'''
zipfile.ZipFile('spam.zip', 'w').write('spam.txt')
compresslevel: 압축율
'''
import zipfile
from pathlib import Path

def make_text(base:Path):
    # 압축 대상 파일 만들기
    f = base / "spam" / "file_zip_demo.txt"
    f.write_text("Hello" * 100000, encoding="utf-8")
    return f

def write_zip(file_path:Path):
    zip_path = file_path.parent / "example.zip"

    with zipfile.ZipFile(zip_path, "w") as z:
        z.write(file_path, compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)

    print("zip 생성 완료", zip_path)

if __name__ == '__main__':
    base = Path(__file__).parent / "연습"

    target = make_text(base)
    print(target)

    write_zip(target)
# pip install pytesseract
import pytesseract as tess
from PIL import Image
from pathlib import Path


def read_image(img_path):
    return Image.open(img_path)

def ocr_to_text(img):
    text = tess.image_to_string(img, lang="kor+eng")
    return text

def save_text(out_file, raw):
    p = Path(out_file)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        f.write(raw)


if __name__ == "__main__":
    img_path = Path(__file__).parent / "data/example1.png"

    if not img_path.exists():
        print("이미지 없음: example1.png")
        exit(1)

    print("[1] 이미지 열기:", img_path.as_posix())
    img = read_image(img_path)

    print("[2] 시작")
    raw = ocr_to_text(img)

    print("[3] 결과 미리 보기")
    print(raw[:100])

    print("[4] 저장")
    out_file = Path(__file__).parent / "result/step1_raw.txt"

    save_text(out_file, raw)

    print("[5] 완료!")
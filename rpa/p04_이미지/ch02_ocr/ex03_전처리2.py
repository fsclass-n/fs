# 전처리
import pytesseract as tess
from PIL import Image, ImageOps
from pathlib import Path


def preprocess_plus(img, th=180, border=10):
    g = img.convert("L")
    g2 = ImageOps.autocontrast(g)
    big = g2.resize((g2.width*2, g2.height*2))
    bw = big.point(lambda x:255 if x > th else 0, mode="1").convert("L")
    clean = ImageOps.expand(bw, border=10, fill="white")
    return clean


def run(src, dst_img, dst_txt):
    img = Image.open(src)
    img_rot = img.rotate(-90)
    proc = preprocess_plus(img_rot, th=100)
    Path(dst_img).parent.mkdir(parents=True, exist_ok=True)
    proc.save(dst_img)
    text = tess.image_to_string(proc, lang="kor+eng")
    Path(dst_txt).write_text(text, encoding="utf-8")
    print("저장:", dst_img, "|", dst_txt)

def main():
    cur_dir = Path(__file__).parent
    src = cur_dir / "data/example2.jpg"
    dst_img = cur_dir / "result/example3_proc.png"
    dst_txt = cur_dir / "result/step3_text.txt"

    run(src, dst_img, dst_txt)


if __name__ == "__main__":
    main()
import pytesseract as tess
from PIL import Image, ImageOps
from pathlib import Path
import re

def clean_text(s):
    s = s.replace("\r\n", "\n")
    s = re.sub(r"-\n", "", s)
    s = re.sub(r"[\t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = s.strip()
    return s

def preprocess(img):
    g = img.convert("L")
    g2 = ImageOps.autocontrast(g)
    big = g2.resize((g2.width*2, g2.height*2))
    bw = big.point(lambda x:255 if x > 180 else 0, mode="1").convert("L") # type: ignore
    clean = ImageOps.expand(bw, border=10, fill="white")
    return clean

def main():
    cur_dir = Path(__file__).parent
    src_dir = cur_dir / "data"
    out_dir = cur_dir / "result/batch_txt"
    out_dir.mkdir(parents=True, exist_ok=True)
    exts = (".jpg", ".jpeg", ".png")
    for p in sorted(src_dir.glob("*")):
        if p.suffix.lower() not in exts:
            continue
        img = Image.open(p)
        proc = preprocess(img)
        text = tess.image_to_string(proc, lang="kor+eng")
        print(text)
        neat = clean_text(text)
        (out_dir / f"{p.stem}.txt").write_text(neat, encoding="utf-8")
        print("완료:", p.name)


if __name__ == "__main__":
    main()
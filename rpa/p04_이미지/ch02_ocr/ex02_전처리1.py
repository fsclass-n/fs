# 전처리
import pytesseract as tess
from PIL import Image, ImageOps
from pathlib import Path

# 기본 전처리
def preprocess_basic(img):
    g = img.convert("L") # 그레이스케일
    g2 = ImageOps.autocontrast(g) # 명암 자동 조절
    big = g2.resize((g2.width*2, g2.height*2)) # 확대
    return big


def run(src, dst_img, dst_txt):
    img = Image.open(src)
    img_rot = img.rotate(-90)
    proc = preprocess_basic(img_rot)
    Path(dst_img).parent.mkdir(parents=True, exist_ok=True)
    proc.save(dst_img)

    # 이미지에서 텍스트 추출
    text = tess.image_to_string(proc, lang="kor+eng")
    Path(dst_txt).write_text(text, encoding="utf-8")
    print("저장:", dst_img, "|", dst_txt)

def main():
    cur_dir = Path(__file__).parent
    src = cur_dir / "data/example2.jpg"
    dst_img = cur_dir / "result/example2_proc.png"
    dst_txt = cur_dir / "result/step2_text.txt"

    run(src, dst_img, dst_txt)


if __name__ == "__main__":
    main()
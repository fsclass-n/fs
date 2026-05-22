import re
from pathlib import Path

def load_text(src):
    return Path(src).read_text(encoding="utf-8")

def clean_text(s):
    s = s.replace("\r\n", "\n")
    s = re.sub(r"-\n", "", s)
    s = re.sub(r"[\t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = s.strip()
    return s


def main():
    src = Path(__file__).parent / "result/step3_text.txt"
    raw = load_text(src)
    clean = clean_text(raw)
    out = Path(__file__).parent / "result/step4_text.txt"
    Path(out).write_text(clean, encoding="utf-8")
    print("정리 완료!")


if __name__ == "__main__":
    main()
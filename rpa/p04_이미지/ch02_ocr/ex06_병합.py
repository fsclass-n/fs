from pathlib import Path

def merge_texts(src_dir, out_file):
    src = Path(src_dir)
    files = sorted([p for p in src.glob("*.txt")])
    lines = []
    for p in files:
        title = f"### {p.stem}\n\n"
        body = p.read_text(encoding="utf-8").strip()
        lines.append(title + body + "\n\n")
    out = Path(out_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(lines), encoding="utf-8")
    return len(files), out.as_posix()

def main():
    src_dir = Path(__file__).parent / "result/batch_txt"
    out_file = Path(__file__).parent / "result/merged_clean.txt"
    if not Path(src_dir).exists:
        print("폴더 없음:", src_dir, "(ex05를 먼저 실행하세요)")
        return
    count, path = merge_texts(src_dir, out_file)
    print(f"합치기 완료! {count}개 파일 -> {path}")

if __name__ == "__main__":
    main()
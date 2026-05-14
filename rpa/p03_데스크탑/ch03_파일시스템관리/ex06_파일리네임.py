import os, shutil, re
from pathlib import Path

# 매출보고서2026년01월01일.xlsx
# 매출보고서_2026_01_01.xlsx

DATE_KR = re.compile(r'(.*?)(\d{4})년(\d{2})월(\d{2})일(.*)')
'''
r''	    Raw 문자열 (\를 그대로 사용)

기호	설명
( )	    그룹(캡처 그룹)
.	    아무 문자 1개
*	    0개 이상 반복
+       1개 이상 반복
?	    최소 매칭(Non-Greedy)
.*	    모든 문자 여러 개
.*?	    가능한 최소 문자 매칭

예) (1111) ssdfdfd (2222) sdfdfdfasdf (33333)

\d	    숫자 1개 (0~9)
[0-9]   숫자 1개 (0~9)
{4}	    정확히 4번 반복
{2}	    정확히 2번 반복
Year	문자열 "Year" 그대로
Month	문자열 "Month" 그대로
Day	    문자열 "Day" 그대로
'''


def rename_dates(root: Path):

    for folder, _, files in os.walk(root):
        p = Path(folder)

        for name in files:
            match = DATE_KR.fullmatch(name)

            if not match:
                continue

            pre, yyyy, mm, dd, suf = match.groups()

            new_name = f"{pre}_{yyyy}-{mm}-{dd}{suf}"

            dst = p / new_name

            n = 1
            while dst.exists():
                dst = p / f"{dst.stem}_{n}{dst.suffix}"
                n += 1
            src = p / name

            shutil.move(str(src), str(dst))
            print(f"[리네임] {name} -> {dst.name}")

if __name__ == "__main__":
    base = Path(__file__).parent / "연습" / "날짜정리"
    rename_dates(base)
# 데이터 추출
'''
1. HTML 태그로 추출
2. HTML 속성으로 추출: id, class, href, src, ...
'''
# import bs4
from bs4 import BeautifulSoup

html_example = """
<html>
    <body>
        <h1 id="title">나의 웹사이트</h1>
        <p>이것은 첫 번째 문단입니다.</p>
        <p>이것은 두 번째 문단입니다. 여기에는 <b>굵은 글씨</b>도 있습니다.</p>
        <div>
            <p>이것은 div 태그 안의 세 번째 문단입니다.</p>
        </div>
    </body>
</html>
"""

# soup = bs4.BeautifulSoup(html_example, "html.parser")
soup = BeautifulSoup(html_example, "html.parser")

# HTML 태그와 속성 또는 CSS 선택자(CSS Selector)를 사용하여 HTML 안에서 모든 <p> 태그를 찾아 리스트 형태로 반환합니다.
# soup.select("태그명")
paragraph_elements = soup.select("p")

print("찾은 개수:", len(paragraph_elements)) # 찾은 개수: 3
print(paragraph_elements)
# [<p>이것은 첫 번째 문단입니다.</p>, <p>이것은 두 번째 문단입니다. 여기에는 <b>굵은 글씨</b>도 있습니다.</p>, <p>이것은 div 태그 안의 세 번째 문단입니다.</p>]

for e in paragraph_elements:
    # 요소 출력
    print("\n31:", e)
    # 태그 안의 내용만 출력
    print("32:",e.get_text())
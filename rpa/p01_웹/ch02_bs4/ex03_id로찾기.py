import bs4

html_example = """
<html>
    <body>
        <div id="header">
            <h1>블로그 제목</h1>
        </div>
        <div id="content">
            <p>이것은 본문 내용입니다.</p>
            <p>스크래핑은 <b>재미있습니다.</b></p>
        </div>
        <div id="footer">
            <p>Copyright 2026. All Rights Reserved.</p>
        </div>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

content_div = soup.select("#content")
print(content_div)
# print(content_div.get_text()) => AttributeError
print("-" * 20)

# content_div 있으면 True 없으면 False
if content_div:
    for ele in content_div:
        print(ele.get_text())
else:
    print("없음")
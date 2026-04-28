import bs4

html_example = """
<html>
    <body>
        <h1>오늘의 메뉴</h1>
        <ul>
            <li class="menu-item">김치찌개</li>
            <li class="menu-item">된장찌개 (추천)</li>
            <li class="menu-item">비빔밥</li>
            <li class="side-dish">계란찜</li>
        </ul>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

menu_items = soup.select(".menu-item")

for item in menu_items:
    print(item.get_text())
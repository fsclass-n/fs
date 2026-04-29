# '이전' 버튼 링크 찾기
'''
<a rel="prev" href="/3237/" accesskey="p">&lt; Prev</a>
<a rel="next" href="#" accesskey="n">Next &gt;</a>
a 태그 -> rel == "prev"
a[속성명='속성값'] -> "a[rel='prev']" -> 요소.get
'''

import requests, bs4

target_url = "https://xkcd.com/3237/"

response = requests.get(target_url, timeout=10)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

prev_link_element = soup.select("a[rel='prev']")

print(prev_link_element)
# [<a accesskey="p" href="/3236/" rel="prev">&lt; Prev</a>, <a accesskey="p" href="/3236/" rel="prev">&lt; Prev</a>]
print(prev_link_element[0])
# <a accesskey="p" href="/3236/" rel="prev">&lt; Prev</a>

if not prev_link_element:
    print("이전 페이지 링크 없음")
else:
    # get()는 html 속성 값을 반환
    prev_path = prev_link_element[0].get("href")
    
    print(prev_path) # /3236/

    if not prev_path.startswith("http"):
        prev_path = "https://xkcd.com" + prev_path

    print("다음에 방문할 주소:", prev_path)
    # 다음에 방문할 주소: https://xkcd.com/3236/
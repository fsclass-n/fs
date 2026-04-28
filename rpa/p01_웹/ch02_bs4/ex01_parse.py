# pip install bs4
import requests
import bs4

#target_url = "https://news.naver.com/section/105"
target_url = "https://news.naver.com/section/999"
# 에러: 500 Server Error: Internal Server Error for url: https://news.naver.com/section/999


try:
    response = requests.get(target_url)
    response.raise_for_status()
    print(response.text)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    print(type(soup)) # <class 'bs4.BeautifulSoup'>

except requests.exceptions.HTTPError as e:
    print("에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)
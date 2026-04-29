# 웹 페이지의 특정 요소 찾기
'''
find_element(): 하나 찾기, 없으면 에러(try~except) <- bs4의 select_one()
find_elements(): 여러 개 찾기, 없으면 빈 리스트 <- bs4의 select()

검색 기준
    id -> By.ID
    class -> By.CLASS_NAME
    tag -> By.TAG_NAME
    name -> By.NAME
    css -> By.CSS_SELECTOR
    By.LINK_TEXT
    XPATH -> By.XPATH

    예) ele = browser.find_element(By.ID, 'id값')
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(2) # 2초 대기

try:
    search_box = browser.find_element(By.ID, 'query')
    print(search_box)
    # <selenium.webdriver.remote.webelement.WebElement (session="9e8979a39566d9fccde07d776a83c2fe", element="f.F6696122F13ADA696968B2BE33240D9A.d.7E60E860F2C752337D2724449874CE1D.e.3")>
    print(search_box.tag_name) # input

except Exception as e:
    print("에러: ", e)

menu_links = browser.find_elements(By.CLASS_NAME, 'link_service')
print(len(menu_links)) # 12


for link in menu_links:
    if link.text.strip():
        print("링크 :", link.text.strip())
'''
링크 : 메일
링크 : 카페
링크 : 블로그
링크 : 스토어
링크 : 뉴스
링크 : 증권
링크 : 부동산
링크 : 지도
링크 : 웹툰
링크 : 치지직
추천
링크 : 바로가기 펼침
링크 : 레고코리아
'''


time.sleep(10)
browser.quit()
# 요소 클릭하고, 링크 따라가기
'''
click()
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(1)

try:
    # <시작태그 속성="값">콘텐츠</끝태그>
    # <a href="https://news.naver.com/" class="link_service" target="_blank"><span class="service_icon type_news"></span><span class="service_name">뉴스</span></a>
    news_link = browser.find_element(By.LINK_TEXT, '뉴스')  
    news_link.click()

    time.sleep(3)

    print("title:", browser.title)
    print("current_url:", browser.current_url)
    '''
        title: NAVER
        current_url: https://www.naver.com/
    '''

except Exception as e:
    print("에러:",e)


time.sleep(10)
browser.quit()
# 셀레니엄
# pip install selenium
'''
WebDriver
    Chrome -> webdriver.Chrome()
    Firefox -> webdriver.Firefox()
    Edge -> webdriver.Edge()
browser.get(url)
'''
import time
from selenium import webdriver

# browser = webdriver.Firefox()
# browser = webdriver.Edge()
browser = webdriver.Chrome()

# target_url = "https://www.python.org"
target_url = "https://www.megabox.co.kr"
browser.get(target_url)

time.sleep(20)
browser.quit()
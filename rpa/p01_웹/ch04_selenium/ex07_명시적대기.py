# 명시적 대기(Explicit Waits)
'''
WebDriverWait()
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selenium Explicit Wait Test</title>
    <script>
        function showMessage() {
            // 버튼 클릭 후 3초 뒤 <h2>Hello</h2> 추가
            setTimeout(() => {
                // <h2></h2>
                const h2 = document.createElement('h2');
                // <h2>Hello</h2>
                h2.textContent = 'Hello';
                document.body.appendChild(h2);
            }, 3000);
        }
    </script>
</head>
<body>
    <h1>명시적 대기 실습</h1>
    <p>버튼을 누르면 3초 뒤에 "Hello"가 나타납니다.</p>
    <button onclick="showMessage()">Try it</button>
</body>
</html>

/html/body/h2
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:5500/rpa/p01_%EC%9B%B9/ch04_selenium/app.html")
# browser.get(r"D:\wi\git\fs\rpa\p01_웹\ch04_selenium\app.html")
# time.sleep(2)

try:
    try_it_button = browser.find_element(By.TAG_NAME, 'button')
    try_it_button.click()
    print("버튼 클릭 완료")

    # time.sleep(10)

    hello_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[text()="Hello"]')))

    print("찾은 요소: ", hello_element.text)
    '''
        버튼 클릭 완료
        찾은 요소:  Hello
    '''

except Exception as e:
    print("에러:",e)


time.sleep(10)
browser.quit()
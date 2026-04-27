# pip install requests -> 설치
# pip uninstall requests -> 지우기
import requests

url_success = "https://www.python.org"
url_fail = "https://www.python.org/this-page-does-not-exist"
#url_fail = "https://www.megabox.co.kr/movie/011"
#url_fail = "https://www.google.com/sea"

urls_to_check = [url_success, url_fail]

for url in urls_to_check:
    try: 
        response = requests.get(url)
        # 응답 상태가 200(성공)이 아닐 경우 강제로 에러(HTTPError)를 발생시킵니다
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("페이지 로딩 에러:", e)
    else:
        print("페이지 로딩 성공:", response.status_code)
import requests

# target_url = "https://www.yna.co.kr/view/AKR20250923073400009?section=international/all"
#target_url = "https://ko.wikipedia.org/wiki/한글"
target_url = "https://ko.wikipedia.org/wiki/"

try:
    response = requests.get(target_url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("페이지 로딩 에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)
    # 서버에서 받은 응답(response) 중 문자열로 된 HTML 소스 코드만 추출하여 변수에 저장합니다.
    html_code = response.text

    print("전체 코드 길이:", len(html_code))
    print("----------------코드 미리 보기----------------")
    print(html_code[:])
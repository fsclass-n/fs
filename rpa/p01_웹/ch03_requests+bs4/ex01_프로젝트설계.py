import requests, bs4, os

# 1. 시작 URL 지정
start_url = "https://xkcd.com"

# 2. 이미지 저장 폴더 지정
os.makedirs("xkcd_comics", exist_ok=True)

# 3. 크롤링
# 루프 시작
while True:
    # 현재 페이지 다운로드
    # 만화 이미지 URL 찾기
    # 이미지 다운로드 저장
    # Prev 버튼 URL
    # 다음 페이지 이동하기 위해 URL 업데이트
    # 루프 종료 조건 확인 때까지 반복
    break
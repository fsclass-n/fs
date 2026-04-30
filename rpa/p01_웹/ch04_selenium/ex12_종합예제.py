from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, bs4

URL = "https://tech.kakao.com/blog"

browser = webdriver.Chrome()
browser.get(URL)

time.sleep(3)

post_titles = []

while len(post_titles) < 20:

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.list_post > li')))

    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')

    # 반복문 간소화
    # list Comprehension(컴프리헨션)
    # 시퀀스(반복가능객체): 리스트, 튜플, 문자열, range()
    '''
        [표현식 for 항목 in 시퀀스 [if 조건문]]
    '''
    current_titles = [tag.get_text(strip=True) for tag in soup.select("ul.list_post > li h4.tit_post")]

    # 중복 제거 후 새로운 제목만 추가
    new_titles_added = False
    for title in current_titles:
        if title not in post_titles:
            post_titles.append(title)
            new_titles_added = True

    # 새로 추가된 게 없거나 이미 20개 이상이면 종료
    if not new_titles_added or len(post_titles) >= 20:
        break

    # "다음 페이지" 버튼 클릭
    try:
        next_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn_next'))
        )
        next_button.click()
        print("'다음 페이지' 버튼 클릭 -> 새로운 게시물 로딩 대기...")
        time.sleep(2)
    except Exception:
        print("'다음 페이지' 버튼 없음, 마지막 페이지에 도달했습니다.")
        break

time.sleep(5)

# 브라우저 종료
browser.quit()

# 최종 결과 출력
print("\n--- 수집된 최신 게시물 제목 (상위 20개) ---")
for i, title in enumerate(post_titles[:20], start=1):
    print(f"{i}. {title}")

'''
'다음 페이지' 버튼 클릭 -> 새로운 게시물 로딩 대기...

--- 수집된 최신 게시물 제목 (상위 20개) ---
1. 카카오톡 예약하기에서 그려 본 캘린더
2. 카나나 스칼라 1회 세미나 현장 스케치
3. 수억 건의 보안 신호 속 진짜 위협 찾기 — AI로 보안 모니터링의 패러다임을 바꾸다
4. 학생에서 개발자로: 로또 구현부터 레거시 개선까지, 서버의 흐름을 배우다
5. 학생에서 개발자로: DB, 보안부터 AI까지, 정답보다 합리적인 선택을 배우다
6. 한국 문화 이해부터 화면 조작까지: Kanana-V 기능 확장의 모든 것
7. 2026 카카오그룹 신입크루 공채 코딩테스트 2차 문제해설
8. 2026 카카오그룹 신입크루 공채 코딩테스트 1차 문제해설
9. Kanana-o 신규 모델 및 API 베타 서비스를 공개합니다.
10. 잃어버린 리포트를 찾아서: 카카오 메시징 시스템의 경쟁 조건 문제와 안티 패턴 제거 과정
11. 카카오 AI 앰배서더 ‘KANANA 429 앰배서더’를 신규 모집합니다.
12. Kanana-2 개발기 (2): 개선된 post-training recipe를 중심으로
13. Kanana-2 개발기 (1): Pre-training에서의 의사결정들을 중심으로
14. “생각하고 답변하는” 카카오의 하이브리드 멀티모달 언어모델, Kanana-v-4b-hybrid 개발기
15. 초경량 클래식 형태소 분석기 개발기
16. 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개
17. MongoDB 8.0 업그레이드 해야하는 12가지 이유
18. 더욱 똑똑하게 답하며, 더욱 풍부한 감정표현을 향한 Kanana-o의 진화 과정
19. ​한국어와 이미지를 한 번에, 카카오의 멀티모달 임베딩 모델 개발기
20. AI TOP 100이 우리에게 남긴 것들
'''
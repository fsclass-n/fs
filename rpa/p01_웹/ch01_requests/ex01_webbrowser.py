# webbrowser는 내장 모듈
import webbrowser

search_query = "RPA"
naver_search_url = "https://search.naver.com/search.naver?query=" + search_query

webbrowser.open(naver_search_url)
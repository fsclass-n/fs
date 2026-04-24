# open(filename, [mode])
# open 함수는 '파일 이름'과 '읽기 방법'을 입력받아
# 파일 객체를 반환

# 읽기 방법(mode)을 생략하면
# 기본값인 읽기 모드(r)로 파일 객체를 만들어 반환
# w: 쓰기 모드로 파일 열기
# r: 읽기 모드로 파일 열기
# a: 추가 모드로 파일 열기
# b: 바이너리 모드로 파일 열기

# f = open("binary_file", "rb")

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!")
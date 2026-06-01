import csv, os, usecsv

os.chdir(r'D:\이름\py\p04')

# CSV 파일 쓰기
a = [['구', '전체', '내국인', '외국인'],
     ['관악구', '519864', '502089', '17775'],
     ['강남구', '547602', '542498', '5104'],
     ['송파구', '686181', '679247', '6934'],
     ['강동구', '428547', '424235', '4312']]
# abc.csv 파일을 쓰기 모드(w)로 연다
with open('abc.csv', 'w', newline='', encoding="utf-8-sig") as f:
    # CSV형 리스트의 원소가 쉼표(,)로 구분되어 있을 때는 생략 가능
    csvobject = csv.writer(f, delimiter=',')
    # writerows(): CSV형 리스트가 저장된 객체를 파일에 쓸 때 사용
    # CSV 파일에 CSV형 리스트a 저장
    csvobject.writerows(a)

# 함수로 작성
def writecsv(filename, the_list):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)

# writecsv()를 사용해 test.csv 파일 만들기
a = [['국어', '영어', '수학'], [99, 88, 77]]
usecsv.writecsv('test.csv', a)

# usecsv 모듈 임포트하고 사용하기
a = [['물리','화학', '생물'], [70, 99, 100]]
usecsv.writecsv('test.csv', a)
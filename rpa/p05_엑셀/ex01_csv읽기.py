import pandas as pd
from pathlib import Path

cur_dir=Path(__file__).parent
df=pd.read_csv(cur_dir / "data.csv")

print(df)

#---------------------------------------------------

# CSV 파일 읽기
import csv, os
# a.csv 파일이 있는 폴더로 이동
os.chdir(r'D:\이름\py\p04')
# 읽기 모드(r)로 a.csv 파일 열기
f = open('a.csv', 'r', encoding='utf8')
# 객체 f를 csv.reader로 읽어 new 객체에 저장
new = csv.reader(f)
# new를 입력하면 csv 모듈의 객체임을 확인할 수 있다.
print("10:", new)

for i in new:
    print("13:", i)

a_list = []
for i in new:
    print("17:", i)
    a_list.append(i)
print("19:", a_list)

f.seek(0)

for i in new:
    print("24:", i)
    a_list.append(i)
print("26:", a_list)

# 함수로 만들기
def opencsv(filename):
    f = open(filename, 'r', encoding='utf8')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print("37:", opencsv('example2.csv'))
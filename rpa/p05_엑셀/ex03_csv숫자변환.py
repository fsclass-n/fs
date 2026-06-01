# csv 파일 불러와서 형식 확인하기
import os, usecsv, re
total = usecsv.opencsv(r'D:\이름\py\p04\popSeoul2023.csv')
for i in total [:5]:
    print("5:", i)

# 문자형 자료를 숫자형으로 바꾸기
# float() 함수로 바로 바꾸기
i = '123'
print("10:", float(i))
# 정수로
print("12:", int(i))

# 쉼표(,) 때문에 전환 불가
# print("15:", float('152,212'))

print("17:", float(' 152,212 '.replace(',', '')))

print("19:", type(float(' 152,212 '.replace(',', ''))))

# 숫자 원소만 골라서 쉼표(,) 제거하기
i = total[1]
print("23:", i)

k = []
for j in i:
    # j에 숫자가 들어있다면
    if re.search(r'\d', j):
        # 쉼표(,)를 삭제하고 실수형으로 바꿔 k에 저장
        k.append(float(re.sub(',', '', j)))
        # 그렇지 않으면, 그대로 k에 저장
    else:
        k.append(j)
print("34:", k)

# 문자와 숫자가 섞인 원소 골라내기
p = ['123강남', '151,767', '11,093', '27,394'] # '123강남' 원소 추가
k = []
# for j in p:
#     if re.search(r'\d', j):
#         k.append(float(j.replace(',', '')))
#     else:
#         k.append(j)


for j in p:
    # 알파벳과 한글이 있다면 그대로 k에 저장
    if re.search('[a-z가-힣]', j):
        k.append(j)
    else:
        k.append(float(j.replace(',', '')))
print("52:", k)


# 특수 문자와 숫자가 섞인 원소 골라내기
i = ['123!!', '151,767', '11,093', '27,394'] # '123!!'이란 원소를 추가
k = []
# for j in i:
#     if re.search('[a-z가-힣]', j):
#         k.append(j)
#     else:
#         k.append(float(j.replace(',', '')))

for j in i:
    # search() 함수에 느낌표(!) 추가
    if re.search('[a-z가-힣!]', j):
        k.append(j)
    else:
        k.append(float(j.replace(',', '')))
print("70:", k)


for j in i:
    if re.search('[a-z가-힝!]', j):
        # j가 있던 자리에 그대로 j 저장
        i[i.index(j)] = j
    else:
        # j가 있던 자리에 j를 실수형으로 바꿔 저장
        i[i.index(j)] = float(j.replace(',', ''))
print("80:", i)
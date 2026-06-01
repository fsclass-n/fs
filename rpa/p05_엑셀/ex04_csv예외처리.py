# csv 파일 불러와서 형식 확인하기
import usecsv, re
total = usecsv.opencsv(r'D:\이름\py\p04\popSeoul2023.csv')

# 예외 처리로 오류 넘어가기
# i = ['123!!', '151,767', '11,093', '27394', ''] # i에 빈문자열('') 추가
# for j in i:
#     if re.search('[a-z가-힝]', j):
#         i[i.index(j)] = j
#     else:
#         i[i.index(j)] = float(j.replace(',', ''))


i = ['123!!', '151,767', '11,093', '27394', '', '!!!$%']
for j in i:
    try:
        # 모든 j를 실수형으로 바꾼다.
        i[i.index(j)] = float(j.replace(',', ''))
    # 오류가 발생하면
    except:
        # pass를 실행해 넘어간다.
        pass
print("23:", i)


# 숫자만 골라서 숫자형으로 바꾸기
i = total[1]
k = []
for j in i:
    # j에 숫자가 들어 있으면
    if re.search(r'\d', j):
        # 쉼표(,)를 삭제하고 실수형으로 바꿔 k에 저장
        k.append(float(j.replace(',', '')))
        # j에 숫자가 들어 있지 않으면
    else:
        # 그대로 k에 저장
        k.append(j)
print("38:", k)
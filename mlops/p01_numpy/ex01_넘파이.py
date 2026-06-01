# 넘파이로 배열 정의하기
import numpy as np
# np.array() 함수로 배열 정의
a = np.array([[2, 3], [5, 2]])
print(a)

# 배열 슬라이싱 하기
# 3x5 배열을 만들어 d에 저장
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
print(d)

# 인덱싱
print(d[1][2])
print(d[1, 2]) # 이처럼 표현할 수도 있다.

# 슬라이싱
print(d[1:, 3:])

# 1차원 배열
d = np.array([2, 3, 4, 5, 6])
print(d)

# 배열의 크기 알아내기: shape 속성
# 1차원 배열의 크기: 요소의 개수
print(d.shape) # d에는 1개 리스트에 5개의 원소가 있다.

# 2차원 배열
e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)

# 2차원 배열의 크기: 행과 열의 개수
# 행의 개수: 2, 열의 개수: 4 -> (2, 4)
print(e.shape) # e에는 2개의 리스트에 각 4개의 원소가 있다.

# 배열 d의 자료형 확인
# int64: 64비트 정수형
print(d)
print("38:",d.dtype)

# 배열 유형 바꾸기: astype() 함수
# data 배열의 자료형을 float(실수)으로 바꾸기
print("45:",d.astype('float64'))

# 넘파이 함수 알아보기
# 0으로 이뤄진 배열 만들기 - np.zeros() 함수
# 2행 10열의 0으로 이뤄진 배열 만들기
print(np.zeros((2, 10)))

# 1로 이뤄진 배열 만들기 - np.ones() 함수
# 2행 10열의 1로 이뤄진 배열 만들기
print(np.ones((2, 10)))

# 연속형 정수 생성하기 - np.arange() 함수
# 2부터 9까지의 정수로 이뤄진 배열 만들기
print(np.arange(2, 10))

# 행과 열 바꾸기 - np.transpose() 함수
a = np.ones((2, 3))
print(a)
# a에 저장된 배열의 행과 열을 바꿔서 b에 저장하기
b = np.transpose(a)
print(b)

# 배열의 사칙 연산
arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])
# 배열의 덧셈
print(arr1 + arr2)
# 배열의 곱셈
print(arr1 * arr2)
# 배열의 나눗셈
print(arr1 / arr2)

# 크기가 서로 다른 배열끼리 더하기
arr3 = np.array([100, 200, 300])
print(arr1.shape)
print(arr3.shape)
# arr1과 arr3의 shape이 다르지만, arr1의 열의 개수와 arr3의 요소의 개수가 같기 때문에 arr1과 arr3을 더할 수 있다.
# 브로드캐스팅(Broadcasting): 크기가 서로 다른 배열을 연산하는 기능!
print(arr1 + arr3)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr4.shape)
print(arr1.shape)

# 행과 열의 개수가 모두 다른 arr1과 arr4는 더할 수 없다.
# arr1 + arr4 # 에러

a=np.array([1,2,3])
print(a+10)

arr5 = np.array([[9], [3]])
print(arr5.shape)
print(arr1.shape)
print(arr1)
# arr1의 1행에 9를 더하고, 2행에 3을 더하기
print(arr5 + arr1)

# 파이썬 리스트와 배열의 차이점
# 3 x 5 배열 d 정의
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
# CSV형 데이터로 d_list 정의
d_list = [[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]]
print(d_list)
# CSV형 객체의 자료형은 리스트이다.
print(type(d_list))
# d_list의 두 번째 원소까지 슬라이싱을 해서 0으로 바꾸기 -> 에러 발생
# d_list[:2] = 0 # 에러
# 배열 d의 두 번째 원소까지 슬라이싱을 해서 0으로 바꾸기
d[:2] = 0
print(d)

# 인덱싱과 슬라이싱 연습하기
arr4 = np.arange(10)
print(arr4)
# 슬라이싱
print(arr4[:5])
print(arr4[-3:])

# 인덱싱
print("121:",arr1)
# arr1에서 두 번째 리스트의 세 번째 원소 출력하기
print(arr1[1, 2])
# 모든 리스트의 세 번째 원소 슬라이싱
print(arr1[:, 2])


# 설문지 데이터 전처리하기
# 가정: 5점 만점으로 된 설문 조사 결과가 quest.csv 파일에 저장
# 데이터 전처리(data preprocessing)? 데이터를 분석하기 좋게 미리 가공하는 일
import os, usecsv
# quiz.csv 파일이 있는 폴더로 작업 디렉터리 바꾸기
os.chdir(r'D:\wi\lab\do-it-py\p05')
# quest.csv 파일을 열어 숫자 원소를 실수형으로 바꾼 다음, 배열 형태로 quest 객체에 저장하기
quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
print(quest)
print(quest > 5)
# 인덱싱을 활용해 5보다 큰 원소만 출력하기
print(quest[quest > 5])
quest[quest > 5] = 5
print(quest)
usecsv.writecsv('resultcsv.csv', list(quest))
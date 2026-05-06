# 내장 모듈: shelve(쉘브)
import shelve

# 데이터 저장
# data_file[key] = value
with shelve.open('mydata') as data_file:
    data_file['과일'] = ['사과', '바나나', '딸기']
    data_file['숫자'] = [1, 2, 3, 4, 5]
    data_file['고객정보'] = {'이름': '홍길동', '나이': 30}
    data_file['아이디'] = "오리"
    data_file['비밀번호'] = "1234"


# 데이터 읽기
with shelve.open('mydata') as data_file:
    print("과일:", data_file['과일'])
    print("숫자:", data_file['숫자'])
    print("고객정보:", data_file['고객정보'])
    print("아이디:", data_file['아이디'])
    print("비밀번호:", data_file['비밀번호'])

'''
과일: ['사과', '바나나', '딸기']
숫자: [1, 2, 3, 4, 5]
고객정보: {'이름': '홍길동', '나이': 30}
아이디: 오리
비밀번호: 1234
'''
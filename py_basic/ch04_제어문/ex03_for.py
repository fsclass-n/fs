# 반복문
# for문
# 시퀀스: 리스트, 튜플, 문자열, range() 등
'''
    for 변수 in 시퀀스:
        실행문
'''

lst = ['one', 'two', 'three']
for i in lst:
    print(i)


a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


# continue 문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)


# range(시작, 끝) 함수
a = range(10)
print(a) # range(0, 10)

# 1부터 10까지 합
# range(1, 11): 1,2,3,...,10
sum = 0
# for i in [1,2,3,...,10]
for i in range(1, 11):
    sum += i # i값을 sum에 누적
print(sum)


# 합격 축하 문장 출력
# len(요소): 요소의 개수
# range(5): 0,1,2,3,4 -> range(0,5)
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# 중첩 for 문
# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')





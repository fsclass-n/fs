# 반복문
# while 문
# do~while문 없다.
'''
    while 조건문:
        실행문1
        실행문2
        ...
'''

# 예제: 나무 10번찍기
tree_hit = 0

while tree_hit < 10:
    # tree_hit = tree_hit + 1
    tree_hit += 1
    print("나무를 %d번 찍었습니다." % tree_hit)
    if tree_hit == 10:
        print("나무 넘어갑니다.")


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

# 내장 함수
# int(): 정수
# input(): 사용자 입력

number = 0
while number != 4:
    print(prompt)
    number = int(input())


# break 문
# - break를 포함한 반복문을 탈출한다.
# 커피 자판기
# 터미널 실행 중지: ctrl+c
coffee = 10
money = 300

# 조건이 true -> 무한 반복
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        # money = 0
        break

# 실제 자판기
# 커피 한 잔 가격: 300
coffee = 0
while True:
    money = int(input("돈을 넣어 주세요."))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    
    if coffee <= 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# continue 문
# 홀수 출력
a = 0

while a < 10:
    a += 1
    if a % 2 == 0: # 짝수이면
        continue
    print(a)


# while~else 문
count = 0

while count < 3:
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# break 문으로 while 문을 탈출하면 else 절은 실행되지 않는다.
count = 0
while count < 5:
    if count == 2:
        break
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

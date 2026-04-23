# 오류 일부러 발생시키기

# 부모 클래스
class Bird:
    def fly(self):
        raise NotImplementedError

# 자식 클래스
class Eagle(Bird):
    # pass
    # 메서드 재정의
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


# 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '하하':
        raise MyError()
    print(nick)

try:
    say_nick("호호")
    say_nick("하하")
except MyError:
    print("허용되지 않는 별명입니다.")



class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '하하':
        raise MyError()
    print(nick)

try:
    say_nick("호호")
    say_nick("하하")
except MyError as e:
    print(e)

'''
호호
허용되지 않는 별명입니다.
'''

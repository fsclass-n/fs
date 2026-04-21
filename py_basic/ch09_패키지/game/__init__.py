# C:/doit/game/__init__.py
# 패키지 내 모듈을 미리 import
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하면
# 패키지 사용 시 간편하게 접근할 수 있다.
# .graphic.render의 맨 앞 .은 현재 디렉터리를 의미한다.
from .graphic.render import render_test

# 패키지 변수 및 함수 정의
# __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# __init__.py 파일에 패키지를 처음 불러올 때 실행할 코드를 작성할 수 있다.
# game 패키지의 초기화 코드는 하위 모듈의 함수를 import할 경우에도 실행된다.
# 단, 초기화 코드는 한 번 실행된 후에는 다시 import해도 실행되지 않는다.
print("Initializing game ...")

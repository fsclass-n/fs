# from game.sound.echo import *
# -> *는 모든 함수
# -> __all__ 설정 필요없다.

# from game.sound import *
# -> *는 모든 모듈
# -> __all__ 설정 필요하다.

from game.sound import *
# Initializing game ...

echo.echo_test() # echo

# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined

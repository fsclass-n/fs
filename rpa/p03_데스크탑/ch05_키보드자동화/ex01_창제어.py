import sys
import pyautogui

print(pyautogui.getAllWindows())
# [Win32Window(hWnd=197564), Win32Window(hWnd=131180), Win32Window(hWnd=263146), Win32Window(hWnd=133152), Win32Window(hWnd=723196), Win32Window(hWnd=592184), Win32Window(hWnd=132262), Win32Window(hWnd=264040), Win32Window(hWnd=263412), Win32Window(hWnd=1379024), Win32Window(hWnd=67288), Win32Window(hWnd=328090), Win32Window(hWnd=1051334), Win32Window(hWnd=132516), Win32Window(hWnd=66976), Win32Window(hWnd=132266), Win32Window(hWnd=66892), Win32Window(hWnd=66872), Win32Window(hWnd=66242), Win32Window(hWnd=197308), Win32Window(hWnd=65904), Win32Window(hWnd=65896), Win32Window(hWnd=65878), Win32Window(hWnd=65842), Win32Window(hWnd=65840), Win32Window(hWnd=262168), Win32Window(hWnd=65794)]

# OS 판별
'''
'darwin': macOS
'win32': Windows
'linux': Linux
'''
if not sys.platform.startswith("win"):
    print("이 프로그램은 윈도우에서만 작동 합니다.")
    print("대신 창 제목만 나열합니다.")
    print(pyautogui.getAllWindows())
    sys.exit()


print("-" * 30)
# 메모장의 핸들 가져오기(title...)
wins = pyautogui.getWindowsWithTitle("메모장")
print(wins) # [Win32Window(hWnd=2886594)]

if not wins:
    print("메모장을 열어주세요. 잠시 대기합니다.")
    pyautogui.countdown(10)
    wins = pyautogui.getWindowsWithTitle("메모장")

if not wins:
    print("창을 찾기 못했습니다.")
    exit(1)

win = wins[0]
print(win) 
# <Win32Window left="-1881", top="250", width="1532", height="675", title="메모장">
print("창 제목:", win.title) # 창 제목: 연습.txt - 메모장
print("현재 위치:", win.left, win.top) # 현재 위치: -1881 250
print("현재 위치2:", win.topleft) # 현재 위치2: Point(x=-1881, y=250)
print("창 크기:", win.width, win.height) # 창 크기: 1532 675
print("창 크기2:", win.size) # 창 크기2: Size(width=1532, height=675)

win.activate() # 활성화(맨 앞으로 가져오기)
pyautogui.sleep(1)
win.width = 800
win.height = 200

pyautogui.sleep(1)
win.topleft = (100, 100)

if not win.isMaximized:
    win.maximize()

pyautogui.sleep(1)
win.restore() # 중간 크기

pyautogui.sleep(2)
win.close()
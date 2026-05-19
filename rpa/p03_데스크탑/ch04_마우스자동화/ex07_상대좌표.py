'''
>python
>>>import pyautogui
>>> pyautogui.mouseInfo()
>>> quit()
'''
import pyautogui

pyautogui.countdown(3)



# 그림판 최대화면에서 좌표 찾기, 같은 해상도
# 브러쉬: 376,69 238,247,249 #EEF7F9
# Red: 865,60 237,28,36 #ED1C24 -> 611, 90

wins = pyautogui.getWindowsWithTitle("그림판")

win = wins[0]
print(win)
# <Win32Window left="24", top="46", width="1316", height="788", title="그림.png - 그림판">
print(win.left, win.top) # 24 46
pyautogui.moveTo(win.left + 376, win.top + 69, duration=0.5)
pyautogui.click()

pyautogui.sleep(1)

pyautogui.moveTo(win.left + 877, win.top + 67, duration=0.5)
pyautogui.click()
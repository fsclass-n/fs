import pyautogui

# 실행 -> 5초 대기 -> 그림판 전환 -> 클릭
print("그림판으로 전환해 주세요.")
# pyautogui.sleep(5)
pyautogui.countdown(5)
pyautogui.click()


dist = 300
step = 20
count = 0

while dist > 0:
    pyautogui.drag(dist, 0, duration=0.2)
    dist -= step
    pyautogui.drag(0, dist, duration=0.2)
    pyautogui.drag(-dist, 0, duration=0.2)
    dist -= step
    pyautogui.drag(0, -dist, duration=0.2)
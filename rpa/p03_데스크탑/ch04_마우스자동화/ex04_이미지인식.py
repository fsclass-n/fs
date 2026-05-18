import pyautogui
from pathlib import Path

cur_path = Path(__file__).parent

try:
    img_path = str(cur_path / "setting.png")
    print("img_path:", img_path)
    box = pyautogui.locateOnScreen(img_path)
    print("box:", box)
    # box: Box(left=187, top=841, width=34, height=39)
    pyautogui.moveTo(box.left + box.width // 2, box.top + box.height // 2, duration=0.2)
    pyautogui.click()
except pyautogui.ImageNotFoundException:
    print("해당하는 이미지를 찾을 수 없습니다.")
except Exception as e:
    print("알수 없는 에러:", e)


# try:
#     items = list(pyautogui.locateAllOnScreen("folder.png"))
#     print("items:", items)

#     for i, b in enumerate(items):
#         print(f"{i+1}번째 박스 : ", b)

# except pyautogui.ImageNotFoundException:
#     print("해당하는 이미지를 찾을 수 없습니다.")
# except Exception as e:
#     print("알수 없는 에러:", e)
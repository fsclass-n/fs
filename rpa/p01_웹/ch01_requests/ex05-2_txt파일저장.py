# import requests
# import os
import requests, os

target_url = "https://www.gutenberg.org/files/57362/57362-0.txt"

try:
    response = requests.get(target_url)
    response.raise_for_status()

    # 현재 실행 중인 .py 파일의 절대 경로를 가져옵니다.
    current_file_path = os.path.abspath(__file__)
    print(current_file_path)
    # 그 파일이 들어있는 '폴더' 경로만 추출합니다.
    current_dir = os.path.dirname(current_file_path)
    print(current_dir)

    # 폴더 경로와 파일 이름을 합쳐줍니다.
    save_path = os.path.join(current_dir, "윤동주_시.txt")
    print(save_path)


    cnt = 0
    # 윤동주_시.txt -> 387KB
    with open(save_path, "wb") as my_file:
        # chunk_size=100000 Byte -> 약 100KB
        for chunk in response.iter_content(chunk_size=100000):
            cnt += 1
            print(cnt)
            my_file.write(chunk)

except requests.exceptions.HTTPError as e:
    print("페이지 로딩 에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)


'''
# current_file_path = os.path.abspath(__file__)
d:\wi\git\fs\rpa\p01_웹\ch01_requests\ex05-1_txt파일저장.py

# current_dir = os.path.dirname(current_file_path)
d:\wi\git\fs\rpa\p01_웹\ch01_requests

# save_path = os.path.join(current_dir, "윤동주_시.txt")
d:\wi\git\fs\rpa\p01_웹\ch01_requests\윤동주_시.txt
1
2
3
4
페이지 로딩 성공: 200
'''
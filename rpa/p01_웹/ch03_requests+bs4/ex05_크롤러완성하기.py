import requests, os, bs4, time

url = 'https://xkcd.com'
os.makedirs('xkcd_comics', exist_ok=True)

cnt = 0

while not url.endswith("#"):
    cnt += 1
    if cnt > 10: break

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # 만화 이미지
        comic_image_element = soup.select("#comic img")
        if comic_image_element:
            image_url = comic_image_element[0].get("src")

            if not image_url.startswith("http"):
                image_url = "https:" + image_url

            response_img = requests.get(image_url, timeout=10)
            response_img.raise_for_status()

            save_path = os.path.join("xkcd_comics", os.path.basename(image_url))

            with open(save_path, "wb") as image_file:
                for chunk in response_img.iter_content(100000):
                    if chunk: # 빈 청크 방지
                        image_file.write(chunk)
            print(f"저장 완료: {save_path}")
        
        else:
            print("만화 이미지를 찾지 못했습니다.")

        prev_link_element = soup.select('a[rel="prev"]')

        time.sleep(5)

        if not prev_link_element:
            print("이전 페이지가 없어 크롤링을 종료합니다.")
            break

        prev_page_path = prev_link_element[0].get("href")

        if not prev_page_path.startswith("http"):
            url = "https://xkcd.com" + prev_page_path
        else:
            url = prev_page_path
 
    except Exception as e:
        print("에러:", e)
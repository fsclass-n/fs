'''
<div id="comic">
    <img src="//imgs.xkcd.com/comics/soniferous_aether.png" title="Imagine you could ride alongside a sound wave. It would probably be pretty cool, right? We're putting in a departmental budget request to buy a really fast plane so we can check it out." alt="Soniferous Aether" srcset="//imgs.xkcd.com/comics/soniferous_aether_2x.png 2x" style="image-orientation:none">
</div>
'''
import requests, bs4

target_url = "https://123456"
# target_url = "https://xkcd.com"

try:
    response = requests.get(target_url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    img_ele_list = soup.select("#comic img")
    print(img_ele_list)
    print(len(img_ele_list))

    if not img_ele_list:
        print("만화 이미지가 없습니다.")
    else:
        image_url = img_ele_list[0].get("src")
        print(image_url)

        if not image_url.startswith("http"):
            image_url = "https:" + image_url

        print(image_url)

except Exception as e:
    print("에러가 났어요", e)

'''
[<img alt="Soniferous Aether" src="//imgs.xkcd.com/comics/soniferous_aether.png" srcset="//imgs.xkcd.com/comics/soniferous_aether_2x.png 2x" style="image-orientation:none" title="Imagine you could ride alongside a sound wave. It would probably be pretty cool, right? We're putting in a departmental budget request to buy a really fast plane so we can check it out."/>]
1
//imgs.xkcd.com/comics/soniferous_aether.png
https://imgs.xkcd.com/comics/soniferous_aether.png
'''
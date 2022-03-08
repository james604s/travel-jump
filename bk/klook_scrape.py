import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}

response = requests.get(
    "https://www.klook.com/zh-TW/experiences/cate/19-camping-glamping/?frontend_id_list=19&size=24", headers=headers)
soup = BeautifulSoup(response.text, "lxml")

print(soup)

act = soup.find_all("div data-v-2b8acf88",class_="__virtual?typ=entry")
#
print(act)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
import re
import pandas as pd


# headless
c_options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
c_options.add_argument('--headless')  # 啟動Headless 無頭
c_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
c_options.add_argument(f'user-agent={user_agent}')
# c_options.add_argument('--window-size=1920, 1200')

#chromedirver path
drpath = os.getcwd() + "/chromedriver98"

driver_service = Service(drpath)

driver = webdriver.Chrome(service=driver_service, options=c_options)

klook_url = "https://www.klook.com"

driver.get('https://www.klook.com/zh-TW/experiences/cate/19-camping-glamping/?frontend_id_list=19&size=105')

print(driver.title)

driver.implicitly_wait(1)

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, "lxml")

driver.quit()

# df = pd.DataFrame(columns=columns)
#
dt_today = datetime.today().date()
# default columns
columns = ["oid", "loc_title", "merchandise_title", "price", "star", "star_desc", "tags", "booking_date_desc", "seo_content"]
mer_dict = {x: None for x in columns}
mer_dict.setdefault("_ctime", dt_today)

mer_list = []

# div1 = soup.find_all("div",class_="search-result-activity-list")
div1 = soup.find_all("div",{"class":"search-result-activity-list"})
# div2 = soup.find_all("div", class_ = "search-result-card rwd-activity-card desktop large")
# div2 = soup.find_all("div",{"class":"search-result-card rwd-activity-card desktop large"})
div2 = div1[0].find_all("div", {"class": "search-result-card rwd-activity-card desktop large"})

for i in range(len(div2)):
    # oid
    regex = re.compile("oid=(.*)&amp;idx")
    oid = regex.findall(str(div2[i]))
    if not oid:
        raise Exception("oid is not exists")
    oid = oid[0]
    # b = re.compile('\[(.*?)\]').findall(a)
    # print(str(div2[i]).split("activity_"))
    # test = div2[i].split("activity_")
    # print(test)
    # location_title
    loc_title = div2[i].find("span", {"class":"location-title"})
    if loc_title:
        loc_title = loc_title.getText().strip()
    else:
        loc_title = None

    #title
    title = div2[i].find("a", {"target":"_blank"}).getText().strip()

    url = div2[i].find("a").get("href")

    #price
    # price = div2[i].find("b", {"style":"font-weight:500"}).getText().strip()
    price = div2[i].find("span", {"class":"activity-card-sell-price"})
    if price:
        price = price.getText().strip()
    else:
        price = None

    #star_avg_desc
    # star = div2[i].find("span", {"class":"page-activity-recommend-score-number"}).getText().strip()
    star_avg = div2[i].find("span", {"class":"page-activity-recommend-score-number"})
    if star_avg:
        star_avg = star_avg.getText().strip()
    else:
        star_avg = None

    #star_avg_desc
    star_avg_desc = div2[i].find("span", {"class":"page-activity-recommend-review-number"})
    if star_avg_desc:
        star_avg_desc = star_avg_desc.getText().strip()
    else:
        star_avg_desc = None

    #tag
    tags = div2[i].find("div", {"class":"activity-card-tags"})

    if tags:
        tag_list=list()
        tags_len = len(tags)
        if tags_len==1:
            tag = tags.getText().strip()
            tag_list.append(tag)
        else:
            for tag in tags:
                tag = tag.getText().strip()
                tag_list.append(tag)
    else:
        tag_list = []

    # booking_date_desc
    booking_date_desc = div2[i].find("div", {"class":"activity-booking-start-date home-activity-card_date booking-start-date"})
    if booking_date_desc:
        booking_date_desc = booking_date_desc.getText().strip()
    else:
        booking_date_desc = None

    # seo_content
    seo_content = div2[i].find("div", {"class":"seo-content"})
    if seo_content:
        seo_content = seo_content.getText().strip()
    else:
        seo_content = None

    # # star comment
    driver = webdriver.Chrome(service=driver_service, options=c_options)
    full_url = klook_url + url
    driver.get(full_url)

    print(driver.title)
    driver.implicitly_wait(1)
    # print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    mer_dict = {
        "oid": oid,
        "loc_title": loc_title,
        "title": title,
        "url": full_url,
        "price": price,
        "star_avg": star_avg,
        "star_avg_desc": star_avg_desc,
        "tags": tag_list,
        "booking_date_desc": booking_date_desc,
        "seo_content": seo_content,
        '_ctime': dt_today
    }

    mer_list.append(mer_dict)
# print(len(mer_list), mer_list)
print(mer_dict)

    # print(i, oid, loc_title, title, price, star, star_desc, tag_list, booking_date_desc, seo_content)
#
# print(div2)


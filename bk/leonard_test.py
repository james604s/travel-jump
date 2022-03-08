from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
import pandas as pd


# headless
c_options = Options()
c_options.add_argument('--headless')  # 啟動Headless 無頭
c_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
# c_options.add_argument('--window-size=1920, 1200')

#chromedirver path
drpath = os.getcwd() + "/chromedriver98"

driver_service = Service(drpath)

driver = webdriver.Chrome(service=driver_service, options=c_options)

driver.get('https://www.klook.com/zh-TW/experiences/cate/19-camping-glamping/?frontend_id_list=19&size=105')

print(driver.title)

driver.implicitly_wait(0.5)

# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, "lxml")

driver.quit()


# div1 = soup.find_all("div",class_="search-result-activity-list")
div1 = soup.find_all("div",{"class":"search-result-activity-list"})
# div2 = soup.find_all("div", class_ = "search-result-card rwd-activity-card desktop large")
# div2 = soup.find_all("div",{"class":"search-result-card rwd-activity-card desktop large"})

print(len(div1))
    # print("d1",div1[i])
div2 = div1[0].find_all("div", {"class": "search-result-card rwd-activity-card desktop large"})
for i in range(len(div2)):
    print(i, div2[i])



# # star comment
driver = webdriver.Chrome(service=driver_service, options=c_options)
# full_url = 'https://www.klook.com/zh-TW/activity/68499-vw-combi-classic-picnic-camping-experience-trip-bali/'
full_url = 'https://www.klook.com/zh-TW/activity/51850-lapopo-campground-keelung/?spm=Experience_SubVertical.Activity_LIST&clickId=913a381231'
driver.get(full_url)

print(driver.title)
driver.implicitly_wait(1)
# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, "lxml")
driver.quit()
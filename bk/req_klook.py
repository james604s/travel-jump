import time

import requests
import random

cookie = """klk_currency=TWD; kepler_id=8df2318b-0380-4095-8649-a30ae02c60d7; persisted_source=www.google.com; _gcl_au=1.1.1808311688.1646274487; __lt__cid=f8f9c7fe-0286-4209-b030-ace71df5ae63; __lt__cid.c83939be=f8f9c7fe-0286-4209-b030-ace71df5ae63; _pxvid=8f01df24-9a99-11ec-a5a0-7a4e7564754c; dable_uid=30287057.1635497090224; g_state={"i_p":1646469704818,"i_l":2}; _gcl_aw=GCL.1646554565.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gcl_dc=GCL.1646554565.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; pxcts=aabbf09b-9d25-11ec-a3c3-4a647577586d; _gac_UA-86696233-17=1.1646554566.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gac_UA-181637923-2=1.1646554566.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; gc_tag=gclid=CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gac_UA-86696233-1=1.1646554572.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; traffic_retain=true; _gid=GA1.2.304616447.1646718568; _pxhd=eS7MxyMK/ZDcA2tv5HrcOkLi0sxjz4Pm7-6E16ip720Ycttwx-IKr0Amz6S2UC2MfkqDms4ixADKPcUt2eZp7Q==:9tCLph4P-BQZD1JiCWjlxRtdS3tATqXcuNO4BKD9DheOmnquzUM1uTz6qo9/Q4BmBuVsqdEjtahEJCfDTg86kLKZfoT-9btFSnSSFfhqqrY=; __lt__sid=e1cdad8a-65b831e8; __lt__sid.c83939be=e1cdad8a-65b831e8; _clck=1edxhbn|1|ezl|0; __dbl__pv=6; _dc_gtm_UA-86696233-1=1; _dc_gtm_UA-86696233-17=1; _px3=6adc7e832b7e4040d739b6d835c96d0b59a98e4564d9bf4eb43175e69e09a7f2:MTZDUtV11Auvvx826kiwdUs+CmcfuIgJtIOCwtN40o11lBcMHEcuwchLAktld9yvF8by7wQfpvNNIFk/GdnTQg==:1000:Q1F7tqCriK/MVBHZfyk7rJTiB6ruYDtA3J6Z543eMTakNI+a703a4N5VRJbxdoePPbM/7koJm7Jmf6tc4EQvQUAo51Zpq1fDD55TpuWK8tA8d7tnULzGTUfnyr6wc0w6a+94ACulHSPigVShx/eaWTZIPjZGXaryyAepQMd4YdoFIGANDfMdyNQ0iBFNRbPfFPlP+fqTuPWFa88HmlP1YQ==; _clsk=lg0rjh|1646721531060|15|0|l.clarity.ms/collect; _pxff_tm=1; wcs_bt=s_2cb388a4aa34:1646721557; _uetsid=85ac7b309ea311ec8157d93c282bdc28; _uetvid=8fc15a909a9911ec90224198df462e5a; _ga_FW3CMDM313=GS1.1.1646718569.18.1.1646721557.0; _ga=GA1.1.8df2318b-0380-4095-8649-a30ae02c60d7"""
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
print(cookie_dict)

ua_list = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
]

#"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
# 商品清單
headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encodings":"gzip, deflate, br",
    "cache-control":"no-cache",
    "accept-language": "zh-TW",
    "user-agent": random.choice(ua_list),
    "currency": "TWD",
    "cookie":cookie
}

full_url = "https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=19&size=24"

res = requests.get(full_url, headers=headers)

print(f"status code:{res.status_code}")
print(f"encoding: {res.encoding}")
res_json = res.json()
total_size = res_json['result'].get("total", 0)
total_page = total_size / 24
if (total_size % 24) != 0 :
    total_page = int(total_page) + 1
print(f"total_size: {total_size}, total_page: {total_page}")
# print(res_json)

activities_list = []
for i in range(1, total_page+1):
    print(i)
    full_url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=19&size=24&start={i}"
    res = requests.get(full_url, headers=headers)
    print(f"status code:{res.status_code}")
    print(f"encoding: {res.encoding}")
    res_json = res.json()
    activities_list.extend(res_json['result']['activities'])
    time.sleep(1)
print(len(activities_list))
#location_title, deep_link, title, tags, review_star, review_hint, sell_price, start_time, city_id, activity_id
#oid, loc_title, title, price, star, star_desc, tag_list, booking_date_desc, seo_content)
#res_json['result'].keys()
#res_json['result']['cities']
#dict_keys(['activities', 'frontend_tree_mapping', 'channel', 'cities', 'city_count', 'ranges', 'start_time', 'price', 'total'])
#res_json['result']['frontend_tree_mapping']

# 商品內頁
headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encodings":"gzip, deflate, br",
    "cache-control":"no-cache",
    "accept-language": "zh-TW",
    "user-agent": random.choice(ua_list),
    "currency": "TWD",
    "cookie":cookie
}

#full_url = f"https://www.klook.com/v1/usrcsrv/activities/{activity_id}/reviews?page=1&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
full_url = "https://www.klook.com/v1/usrcsrv/activities/51850/reviews?page=2&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
full_url ="https://www.klook.com/v1/usrcsrv/activities/58082/reviews?page=1&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
full_url ="https://www.klook.com/v1/usrcsrv/activities/62186/reviews?page=1&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"

res = requests.get(full_url, headers=headers)
print(f"status code:{res.status_code}")
print(f"encoding: {res.encoding}")
res_json = res.json()
print(res_json)
total_size = res_json['result'].get("total", 0)

if total_size == 0:
    #return []
    123
total_page = total_size / 10
print(total_page)
if (total_size % 10) != 0:
    total_page = int(total_page) + 1
total_page = int(total_page)
print(f"total_size: {total_size}, total_page: {total_page}")

item_list = []
for i in range(1, total_page+1):
    print(i)
    full_url = f"https://www.klook.com/v1/usrcsrv/activities/62186/reviews?page={i}&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
    res = requests.get(full_url, headers=headers)
    print(f"status code:{res.status_code}")
    print(f"encoding: {res.encoding}")
    res_json = res.json()
    item_list.extend(res_json['result']['item'])
    time.sleep(random.randint(3,30))
print(item_list)
print(len(item_list))

from pymongo import MongoClient
m_client = MongoClient("mongodb://mongodb:mongodb123@127.0.0.1:27017/")
db = m_client['travel-jump']
db_col = db["activities_rating_info"]

dt_today = datetime.strftime(datetime.today().date(), "%Y-%m-%d")
for i in item_list:
    i.update({"activity_id":62186, "_ctime":dt_today})
db_col.insert_many(item_list)



dt_today = kwargs.get('dt_today', None)
m_client = MongoClient("mongodb://mongodb:mongodb123@127.0.0.1:27017/")
db = m_client['travel-jump']
db_col = db["activities_rating_info"]
docs = db_col.find({"_ctime": dt_today})
import pandas as pd
df = pd.DataFrame(list(docs))
df['rating'] = df['rating'].apply(lambda x: replace_rating_score(x) if x else None)
df = df[df['rating'] <= 4].reset_index(drop=True)
df = df.drop(['_id'], axis=1)
df.to_csv(f"{dt_today}_klook_activities_rating_info.csv", header=True, index=False)
# print(res_json)
# id, author, date, avatar, author_id, rating, content, language, translate_content, translate_language, need_translate_button, has_reply, reply, review


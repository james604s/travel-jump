import time

import requests
import random

# cookie = """klk_currency=TWD; kepler_id=8df2318b-0380-4095-8649-a30ae02c60d7; persisted_source=www.google.com; _gcl_au=1.1.1808311688.1646274487; __lt__cid=f8f9c7fe-0286-4209-b030-ace71df5ae63; __lt__cid.c83939be=f8f9c7fe-0286-4209-b030-ace71df5ae63; _pxvid=8f01df24-9a99-11ec-a5a0-7a4e7564754c; dable_uid=30287057.1635497090224; _gid=GA1.2.36662618.1646383299; g_state={"i_p":1646469704818,"i_l":2}; _pxhd=171pqhwhUejJJYcCmExDEuql8ilxiyC9a7J6mb4HKxvHMKXwtUvw7wwCM5nShKu2CiRVXkzQNKVRTT64L4Q6sg==:/5IwdZfW-A-dgWJM5HWkriZGGYAJ22CJRiY2D0tpdFNommFCZgYXB/cNX/dV0xsoshQxrfCYSKva3nBVaUj-8A2X/UF57BdEMRuYVaXqXjI=; _clck=1edxhbn|1|ezj|0; _gcl_aw=GCL.1646554565.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gcl_dc=GCL.1646554565.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; pxcts=aabbf09b-9d25-11ec-a3c3-4a647577586d; _gac_UA-86696233-17=1.1646554566.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gac_UA-181637923-2=1.1646554566.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; gc_tag=gclid%3DCjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; _gac_UA-86696233-1=1.1646554572.CjwKCAiA1JGRBhBSEiwAxXblwVWgl3XiMpvW-mwAXFnQmR6TZd_nKiZii48qYAoVpyi-H1QyrBVS9BoCrNUQAvD_BwE; traffic_retain=true; _dc_gtm_UA-86696233-1=1; __lt__sid=e1cdad8a-db55363d; __lt__sid.c83939be=e1cdad8a-db55363d; _dc_gtm_UA-86696233-17=1; __dbl__pv=12; _pxff_ne=1; _px3=51c44490e4bb2581ca4290d70c06884620e9507f426f37ef7d55c7d40eac3233:+6S5k7cjT6sU0RkbWMn8twTRVBXuVRni2Oe4OvogmcsKpQLKqNObGx/7D2Hutl7wGY2DVeeaSPNDmXeCGlN95A==:1000:+SCtfy77If4KPGW66bOvuU/eSgGdEjchGcfjN1PMMXrKvqh1QSeBwLBDoumiC8KPm8dlhxZfl2JRQnJ8BBjmAkda5A+tJgP/udK2PSuY7PAz7dZvR7ugcBppET/yESiUv9kzTsorS0mwzK1BmD2VPQncfbagFulbUItCLSkqVnV6x4Qip4GRMdqwaz8nTuSpuNifqdFJVneGvG0MymPFUA==; _clsk=13xo39x|1646570053251|6|0|k.clarity.ms/collect; wcs_bt=s_2cb388a4aa34:1646570068; _ga_FW3CMDM313=GS1.1.1646570046.15.1.1646570068.0; _ga=GA1.2.8df2318b-0380-4095-8649-a30ae02c60d7; _uetsid=e853d8909b9611eca565f38c999cbb6e; _uetvid=8fc15a909a9911ec90224198df462e5a"""
# cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
# print(cookie_dict)

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
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
]

# 商品清單
headers = {
    "accept":"application/json, text/plain, */*",
    "accept-encodings":"gzip, deflate, br",
    "cache-control":"no-cache",
    "accept-language": "zh-TW",
    "user-agent": random.choice(ua_list),
    "currency": "TWD",
}

item_id = 123
category_id = "activity"
activities_url = "https://www.klook.com/v1/experiencesrv/category/{}?frontend_id_list=19&size=24"
activities_item_url = "https://www.klook.com/v1/usrcsrv/activities/{}/reviews?page=1&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"

get_total_page(activities_url, headers, "activity", 24)

def get_total_page(url, headers, item_id, page_size):
    res = requests.get(url.format(item_id), headers=headers)
    if res.status_code != 200:
        raise Exception(f"status_code: {res.status_code}")
    print(f"status code: {res.status_code}")
    print(f"encoding: {res.encoding}")
    res_json = res.json()
    total_size = res_json['result'].get("total",0)

    total_page = total_size / page_size
    if (total_size % page_size) != 0:
        total_page = int(total_page) + 1
    print(f"total_size: {total_size}, total_page: {total_page}")
    return total_page


def get_activities_list(total_page):
    activities_list = []
    for i in range(1, total_page + 1):
        full_url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=19&size=24&start={i}"
        res = requests.get(full_url, headers=headers)
        # if res.status_code != 200:
        #     raise Exception(f"status_code: {res.status_code}")
        print(f"status code:{res.status_code}")
        print(f"encoding: {res.encoding}")
        res_json = res.json()
        activities_list.extend(res_json['result']['activities'])
        time.sleep(5)
    return activities_list

def get_activities_rating_info(total_page, activity_id):
    if total_page == 0:
        return []
    item_list = []
    for i in range(1, total_page + 1):
        print(i)
        full_url = f"https://www.klook.com/v1/usrcsrv/activities/{activity_id}/reviews?page={i}&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
        res = requests.get(full_url, headers=headers)
        if res.status_code == 200:
            print(f"status code:{res.status_code}")
            print(f"encoding: {res.encoding}")
            res_json = res.json()
            item_list.extend(res_json['result']['item'])
            time.sleep(5)

    print(item_list)
    print(len(item_list))
    return item_list

def soup_klook(item):
    # oid
    regex = re.compile("oid=(.*)&amp;idx")
    oid = regex.findall(str(item))
    if not oid:
        raise Exception("oid is not exists")
    oid = oid[0]
    print("get oid successful!")

    # location_title
    loc_title = item.find("span", {"class": "location-title"})
    if loc_title:
        loc_title = loc_title.getText().strip()
    else:
        loc_title = None
    print("get loc_title successful!")

    # title
    title = item.find("a", {"target": "_blank"}).getText().strip()

    url = item.find("a").get("href")
    print("get title successful!")

    # price
    # price = item.find("b", {"style":"font-weight:500"}).getText().strip()
    price = item.find("span", {"class": "activity-card-sell-price"})
    if price:
        price = price.getText().strip()
    else:
        price = None
    print("get price successful!")

    # star_avg
    star_avg = item.find("span", {"class": "page-activity-recommend-score-number"})
    if star_avg:
        star_avg = star_avg.getText().strip()
    else:
        star_avg = None
    print("get star_avg_desc successful!")

    # star_avg_desc
    star_avg_desc = item.find("span", {"class": "page-activity-recommend-review-number"})
    if star_avg_desc:
        star_avg_desc = star_avg_desc.getText().strip()
    else:
        star_avg_desc = None
    print("get star_avg_desc successful!")

    # tag
    tags = item.find("div", {"class": "activity-card-tags"})

    if tags:
        tag_list = list()
        tags_len = len(tags)
        if tags_len == 1:
            tag = tags.getText().strip()
            tag_list.append(tag)
        else:
            for tag in tags:
                tag = tag.getText().strip()
                tag_list.append(tag)
    else:
        tag_list = []
    print("get tags successful!")

    # booking_date_desc
    booking_date_desc = item.find("div", {
        "class": "activity-booking-start-date home-activity-card_date booking-start-date"})
    if booking_date_desc:
        booking_date_desc = booking_date_desc.getText().strip()
    else:
        booking_date_desc = None
    print("get booking_date_desc successful!")

    # seo_content
    seo_content = item.find("div", {"class": "seo-content"})
    if seo_content:
        seo_content = seo_content.getText().strip()
    else:
        seo_content = None
    print("get seo_content successful!")


    mer_dict = {
        "oid": oid,
        "loc_title": loc_title,
        "title": title,
        "url": klook_url + url,
        "price": price,
        "star_avg": star_avg,
        "star_avg_desc": star_avg_desc,
        "tags": tag_list,
        "booking_date_desc": booking_date_desc,
        "seo_content": seo_content,
        '_ctime': dt_today
    }

    return mer_dict
    # mer_list.append(mer_dict)
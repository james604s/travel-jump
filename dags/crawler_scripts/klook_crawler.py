# import sys
# import os
#
# sys.path.append(os.getcwd())
import random
import requests
import time
from datetime import datetime

def crawler_total_page(url, headers, item_id ,page_size):
    """
    desc:
    :param kwargs:
    :return:
    """
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

def _crawler_activities_list(**kwargs):
    """
    desc:
    :param kwargs:
    :return:
    """
    url = kwargs.get("url", None)
    item_id = kwargs.get("item_id", None)
    headers=kwargs.get("headers", None)
    page_size = kwargs.get("page_size", None)
    dt_today = kwargs.get("dt_today", None)

    total_page = crawler_total_page(url, headers, item_id, page_size)
    activities_list = []
    activities_id_list = []
    # dt_today = datetime.strftime(datetime.today().date(), "%Y-%m-%d")
    for i in range(1, total_page + 1):
        full_url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=19&size=24&start={i}"
        res = requests.get(full_url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"status_code: {res.status_code}")
        print(f"status code:{res.status_code}")
        print(f"encoding: {res.encoding}")
        res_json = res.json()
        activities_list.extend(res_json['result']['activities'])
        for j in res_json['result']['activities']:
            activities_id_list.append(j['activity_id'])
            j.update({"_ctime": dt_today})
        time.sleep(5)
    print(activities_list)

    from db.mongodb import MongoOperation
    m_client = MongoOperation(conn_id = "mongo_travel_jump")
    m_client.mongo_insert_many(activities_list, activities_list)
    return activities_id_list

def _crawler_activities_rating_info(**kwargs):
    """
    desc:
    :param kwargs:
    :return:
    """
    activities_id_list = kwargs['ti'].xcom_pull(task_ids='crawler_activities_list')
    url = kwargs.get("url", None)
    headers=kwargs.get("headers", None)
    page_size = kwargs.get("page_size", None)
    dt_today = kwargs.get("dt_today", None)

    item_list = []
    for activity_id in activities_id_list:
        total_page = crawler_total_page(url, headers, activity_id, page_size)
        if total_page == 0:
            continue
        for i in range(1, total_page + 1):
            print(i)
            full_url = f"https://www.klook.com/v1/usrcsrv/activities/{activity_id}/reviews?page={i}&limit=10&star_num=&lang=&sort_type=0&only_image=false&preview=0"
            res = requests.get(full_url, headers=headers)
            if res.status_code == 200:
                print(f"status code:{res.status_code}")
                print(f"encoding: {res.encoding}")
                res_json = res.json()
                for j in res_json['result']['item']:
                    j.update({"_ctime":dt_today})
                item_list.extend(res_json['result']['item'])
                time.sleep(random.randint(3,15))

    from db.mongodb import MongoOperation
    m_client = MongoOperation(conn_id = "mongo_travel_jump")
    m_client.mongo_insert_many("activities_rating_info", item_list)
    # return item_list

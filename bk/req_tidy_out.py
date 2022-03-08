import requests
import time



def get_total_page(self, url, headers, page_size):
    res = requests.get(url, headers=headers)
    print(f"status code:{res.status_code}")
    print(f"encoding: {res.encoding}")
    res_json = res.json()
    total_size = res_json['result'].get("total", 0)
    total_page = total_size / page_size
    if (total_size % page_size) != 0:
        total_page = int(total_page) + 1
    print(f"total_size: {total_size}, total_page: {total_page}")
    return total_page

def get_activities_list(self, api_url, total_page):
    activities_list = []
    for i in range(1, total_page + 1):
        print(i)
        # full_url = f"https://www.klook.com/v1/experiencesrv/category/activity?frontend_id_list=19&size=24&start={i}"
        res = requests.get(api_url, headers= self.headers)
        print(f"status code:{res.status_code}")
        print(f"encoding: {res.encoding}")
        res_json = res.json()
        activities_list.extend(res_json['result']['activities'])
        print(i, "get data successful!")
        time.sleep(1)
    return activities_list

def get_activities_rating_info(self, api_url, total_page,activity_id):
    return
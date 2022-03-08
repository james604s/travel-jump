import os
import sys
import pandas as pd

from pymongo import MongoClient
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
# sys.path.extend([os.getcwd(),os.getcwd()+"/crawler_scripts"])
from crawler_scripts.klook_crawler import (
    _crawler_activities_list,
    _crawler_activities_rating_info
)
from crawler_scripts.crawler_settings import *
from utils.func import replace_rating_score

def _check_mongo_conn(**kwargs):
    """
    desc:
    :param kwargs:
    :return:
    """
    m_client = MongoClient("mongodb://mongodb:mongodb123@mongodb:27017/")
    db_list = m_client.list_database_names()
    if "travel-jump" in db_list:
        print("DB: travel-jump 已存在!")
        db = m_client['travel-jump']
        db_collection_list = db.list_collection_names()
        if "activities_list" and "activities_rating_info" in db_collection_list:
            print("travel-jump: activities_list&activities_rating_info 已存在!")
            m_client.close()
            return 1
    m_client.close()
    return 0

def _create_schema_if_not_exists(**kwargs):
    """
    desc:
    :param kwargs:
    :return:
    """
    check_mongo_conn_status = kwargs['ti'].xcom_pull(task_ids='check_mongo_conn')
    if check_mongo_conn_status == 0:
        m_client = MongoClient("mongodb://mongodb:mongodb123@mongodb:27017/")
        db = m_client['travel-jump']
        db_col = db["activities_list"]
        db_col.insert_one({"create":"create"})
        db_col.delete_one({"create":"create"})
        print("db_collection: activities_list create succussful!")

        db_col = db["activities_rating_info"]
        db_col.insert_one({"create":"create"})
        db_col.delete_one({"create":"create"})
        print("db_collection: activities_rating_info create succussful!")
        m_client.close()

def rating_info_to_csv(**kwargs):
    """
    desc:
        filter create_time -> Replace Score -> Drop id
    :param kwargs:
    :return:
    """
    dt_today = kwargs.get('dt_today', None)
    m_client = MongoClient("mongodb://mongodb:mongodb123@mongodb:27017/")
    db = m_client['travel-jump']
    db_col = db["activities_list"]
    docs = db_col.find({"_ctime": dt_today})
    df = pd.DataFrame(list(docs))
    df = df['rating'].apply(lambda x: replace_rating_score(x) if x else None)
    df = df[df['rating'] <= 4].reset_index(drop=True)
    df = df.drop(['_id'], axis=1)
    df.to_csv(f"/tmp/{dt_today}_klook_activities_rating_info.csv", header=True, index=False)

dt_today = datetime.strftime(datetime.today().date(), "%Y-%m-%d")

default_args = {
    "owner":"airflow",
    # "email": ["james604s@gmail.com"],
    # "email_on_failure": True,
    # "retries": 1,
    # "retry_delay": 60,
}

dag = DAG('klook_activities',
          start_date=datetime(2022,3,1),
          schedule_interval="0 4 * * *",
          tags=["klook", "crawler", "activities"],
          default_args=default_args,
          catchup=False)

check_mongo_conn = PythonOperator(
    task_id = "check_mongo_conn",
    python_callable = _check_mongo_conn,
    dag = dag
)

check_source_conn = DummyOperator(
    task_id = "check_source_conn",
    dag=dag
)

create_schema_if_not_exists = PythonOperator(
    task_id = "create_schema_if_not_exists",
    python_callable = _create_schema_if_not_exists,
    dag = dag
)

crawler_activities_list = PythonOperator(
    task_id = "crawler_activities_list",
    python_callable = _crawler_activities_list,
    op_kwargs={
        "url": ACTIVITIES_URL,
        "headers": HEADERS,
        "item_id": "activity",
        "page_size": 24,
        "dt_today": dt_today,
        # "dt_today": "{{ execution_date | ds }}"
    },
    dag = dag
)

crawler_activities_rating_info = PythonOperator(
    task_id = "crawler_activities_rating_info",
    python_callable = _crawler_activities_rating_info,
    op_kwargs={
        "url": ACTIVITIES_URL,
        "headers": HEADERS,
        "page_size": 10,
        "dt_today": dt_today
    },
    dag=dag
)

rating_info_to_csv = PythonOperator(
    task_id = "rating_info_to_csv",
    python_callable = rating_info_to_csv,
    op_kwargs={
        "dt_today": dt_today
    },
    dag=dag
)

[check_mongo_conn, check_source_conn] >> create_schema_if_not_exists >> crawler_activities_list >> crawler_activities_rating_info >> rating_info_to_csv
# is_api_conn = PythonOperator()
#
# create_schema_if_not_exists = PythonOperator()
#
# crawler_activities_list = PythonOperator()
#
# crawler_activities_rating_info = PythonOperator()
#
# trigger_activities_rating_to_csv = TriggerDagRunOperator()
"""
is_mongo_conn >> create_schema_if_not_exists 
is_api_conn >> create_schema_if_not_exists >> crawler_activities_list >> crawler_activities_rating_info >> trigger_activities_rating_to_csv
"""

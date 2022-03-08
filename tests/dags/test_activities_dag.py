
import pytest
from dags.activities_dag import _check_mongo_conn

@pytest.mark.skip(reason="wait a minute")
def test_check_mongo_conn():
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

    from airflow.operators.python import PythonOperator
    test = PythonOperator(
        task_id="check_mongo_conn",
        python_callable=_check_mongo_conn,
        dag=dag
    )
    result = test.execute(kwargs={})
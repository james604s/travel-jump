
class MongoOperation:
    from airflow.providers.mongo.hooks.mongo import Mongohook
    def __init__(self, conn_id):
        self.m_client = Mongohook(mongo_conn_id=conn_id)

    def mongo_insert_one(self, mongo_collection, data_dict):
        self.m_client.get_conn()
        self.m_client.insert_one(mongo_collection, data_dict)
        self.m_client.close_conn()

    def mongo_insert_many(self, mongo_collection, data_list):
        self.m_client.get_conn()
        self.m_client.insert_many(mongo_collection, data_list)
        self.m_client.close_conn()
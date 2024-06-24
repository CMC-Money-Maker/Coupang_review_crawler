import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

class Crawl_repository:
    def get_mongo_client(self):
        mongodb_pw = os.environ['MONGODB_PW']
        uri = f"mongodb+srv://daldal_admin:{mongodb_pw}@daldal-coupang-review-d.dn7cm6g.mongodb.net/?retryWrites=true&w=majority&appName=Daldal-coupang-review-data"
        # Create a new client and connect to the server
        client = MongoClient(uri,
                             serverSelectionTimeoutMS=100000,
                             connectTimeoutMS=100000,
                             socketTimeoutMS=100000)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        return client

    def write_crawl_data(self, collection_name:str, data):
        self.client = self.get_mongo_client()
        self.db = self.client['Daldal-coupang-review-data']

        collection = self.db[collection_name]
        collection.drop()
        collection.insert_one(data)



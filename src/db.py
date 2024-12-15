import os
from pymongo import MongoClient
from dotenv import load_dotenv
from src.constants import DB_NAME, BUY_WATCHLIST_COLLECTION, MONGO_URI, MONGO_DB_NAME

# may need to use .env instead
load_dotenv()


def get_buy_watchlist_collection():
    client = MongoClient(os.getenv(MONGO_URI))
    db = client[os.getenv(MONGO_DB_NAME)]
    data = list(db[BUY_WATCHLIST_COLLECTION].find({}, {'_id': 0}))
    client.close()
    return data


def add_to_watchlist(data):
    client = MongoClient(os.getenv(MONGO_URI))
    db = client[os.getenv(MONGO_DB_NAME)]
    db[BUY_WATCHLIST_COLLECTION].insert_one(data)
    client.close()


def add_batch_to_watchlist(data):
    client = MongoClient(os.getenv(MONGO_URI))
    db = client[os.getenv(MONGO_DB_NAME)]
    db[BUY_WATCHLIST_COLLECTION].insert_many(data)

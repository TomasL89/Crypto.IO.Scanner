import os
from pymongo import MongoClient
from dotenv import load_dotenv
from .constants import DB_NAME, BUY_WATCHLIST_COLLECTION

load_dotenv()


def get_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client[DB_NAME]


def get_buy_watchlist_collection():
    return get_db()[BUY_WATCHLIST_COLLECTION]


def add_to_watchlist(data):
    get_buy_watchlist_collection().insert_one(data)
import dotenv
import json
import os
from pymongo import MongoClient
from src.scanner import scan_for_buy_signals
from src.db import add_to_watchlist, get_buy_watchlist_collection
import src.constants as constants
import unittest

TESTING_DB_NAME = 'cryptoIOScannerTest'
LOCAL_DB_HOST = 'mongodb://localhost:27017/'


class TestDBIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up MongoDB client and database
        cls.client = MongoClient(LOCAL_DB_HOST)
        os.environ["MONGO_DB_NAME"] = TESTING_DB_NAME
        os.environ["MONGO_URI"] = LOCAL_DB_HOST
        cls.db = cls.client[TESTING_DB_NAME]
        cls.collection = cls.db[constants.BUY_WATCHLIST_COLLECTION]

    @classmethod
    def tearDownClass(cls):
        # Drop the test database
        cls.client.drop_database(TESTING_DB_NAME)
        cls.client.close()

    def setUp(self):
        # Clear the collection before each test
        self.collection.delete_many({})

    def test_buy_signals_saved_and_queried_correctly(self):
        with open('buy_signals.json', 'r') as f:
            test_data = json.load(f)

        # Save the buy signals to the database
        for signal in test_data:
            data = signal.copy()
            add_to_watchlist(data)

        # Query the saved buy signals
        queried_buy_signals = get_buy_watchlist_collection()

        # Compare the original and queried buy signals
        self.assertEqual(len(test_data), len(queried_buy_signals))
        for original, queried in zip(test_data, queried_buy_signals):
            self.assertDictEqual(original, queried)


if __name__ == '__main__':
    unittest.main()
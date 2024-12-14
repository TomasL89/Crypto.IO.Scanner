import unittest
from unittest.mock import patch, MagicMock
from src.db import get_db, get_buy_watchlist_collection, add_to_watchlist
from src.constants import DB_NAME, BUY_WATCHLIST_COLLECTION


class TestDB(unittest.TestCase):

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_get_db(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/'
        }[key]
        mock_client = MagicMock()
        mock_mongo_client.return_value = mock_client
        db = get_db()
        mock_getenv.assert_called_with('MONGO_URI')
        mock_mongo_client.assert_called_with('mongodb://localhost:27017/')
        self.assertEqual(db, mock_client[DB_NAME])

    @patch('src.db.get_db')
    def test_get_buy_watchlist_collection(self, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        collection = get_buy_watchlist_collection()
        mock_get_db.assert_called_once()
        self.assertEqual(collection, mock_db[BUY_WATCHLIST_COLLECTION])

    @patch('src.db.get_buy_watchlist_collection')
    def test_add_to_watchlist(self, mock_get_buy_watchlist_collection):
        mock_collection = MagicMock()
        mock_get_buy_watchlist_collection.return_value = mock_collection
        data = {"symbol": "BTCUSD", "price": 50000}
        add_to_watchlist(data)
        mock_get_buy_watchlist_collection.assert_called_once()
        mock_collection.insert_one.assert_called_with(data)


if __name__ == '__main__':
    unittest.main()
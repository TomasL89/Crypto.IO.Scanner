import unittest
from unittest.mock import patch, MagicMock
from src.db import get_buy_watchlist_collection, add_to_watchlist, add_batch_to_watchlist


class TestDB(unittest.TestCase):

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_get_buy_watchlist_collection_returns_data(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_client = MagicMock()
        mock_db = mock_client['test_db']
        mock_db['buy_watchlist'].find.return_value = [{"symbol": "BTCUSD", "price": 50000}]
        mock_mongo_client.return_value = mock_client

        data = get_buy_watchlist_collection()
        self.assertEqual(data, [{"symbol": "BTCUSD", "price": 50000}])

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_add_to_watchlist_inserts_data(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_client = MagicMock()
        mock_db = mock_client['test_db']
        mock_mongo_client.return_value = mock_client

        data = {"symbol": "BTCUSD", "price": 50000}
        add_to_watchlist(data)
        mock_db['buy_watchlist'].insert_one.assert_called_with(data)

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_add_batch_to_watchlist_inserts_multiple_data(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_client = MagicMock()
        mock_db = mock_client['test_db']
        mock_mongo_client.return_value = mock_client

        data = [{"symbol": "BTCUSD", "price": 50000}, {"symbol": "ETHUSD", "price": 4000}]
        add_batch_to_watchlist(data)
        mock_db['buy_watchlist'].insert_many.assert_called_with(data)

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_get_buy_watchlist_collection_handles_connection_error(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_mongo_client.side_effect = ConnectionError

        with self.assertRaises(ConnectionError):
            get_buy_watchlist_collection()

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_add_to_watchlist_handles_connection_error(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_mongo_client.side_effect = ConnectionError

        data = {"symbol": "BTCUSD", "price": 50000}
        with self.assertRaises(ConnectionError):
            add_to_watchlist(data)

    @patch('src.db.MongoClient')
    @patch('os.getenv')
    def test_add_batch_to_watchlist_handles_connection_error(self, mock_getenv, mock_mongo_client):
        mock_getenv.side_effect = lambda key: {
            'MONGO_URI': 'mongodb://localhost:27017/',
            'MONGO_DB_NAME': 'test_db'
        }[key]
        mock_mongo_client.side_effect = ConnectionError

        data = [{"symbol": "BTCUSD", "price": 50000}, {"symbol": "ETHUSD", "price": 4000}]
        with self.assertRaises(ConnectionError):
            add_batch_to_watchlist(data)


if __name__ == '__main__':
    unittest.main()

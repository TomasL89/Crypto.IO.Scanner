import unittest
from unittest.mock import patch, MagicMock
from src.broker_data import get_list_of_symbols


class TestBrokerData(unittest.TestCase):

    @patch('src.broker_data.get_binance_client')
    def test_get_list_of_symbols_returns_usdt_pairs(self, mock_get_binance_client):
        mock_client = MagicMock()
        mock_get_binance_client.return_value = mock_client
        mock_client.get_exchange_info.return_value = {
            'symbols': [
                {'symbol': 'BTCUSDT', 'status': 'TRADING', 'quoteAsset': 'USDT'},
                {'symbol': 'ETHUSDT', 'status': 'TRADING', 'quoteAsset': 'USDT'},
                {'symbol': 'BNBBTC', 'status': 'TRADING', 'quoteAsset': 'BTC'},
            ]
        }

        symbols = get_list_of_symbols()
        self.assertEqual(symbols, ['BTCUSDT', 'ETHUSDT'])

    @patch('src.broker_data.get_binance_client')
    def test_get_list_of_symbols_handles_no_usdt_pairs(self, mock_get_binance_client):
        mock_client = MagicMock()
        mock_get_binance_client.return_value = mock_client
        mock_client.get_exchange_info.return_value = {
            'symbols': [
                {'symbol': 'BNBBTC', 'status': 'TRADING', 'quoteAsset': 'BTC'},
                {'symbol': 'ETHBTC', 'status': 'TRADING', 'quoteAsset': 'BTC'}
            ]
        }

        symbols = get_list_of_symbols()
        self.assertEqual(symbols, [])

    @patch('src.broker_data.get_binance_client')
    def test_get_list_of_symbols_handles_empty_exchange_info(self, mock_get_binance_client):
        mock_client = MagicMock()
        mock_get_binance_client.return_value = mock_client
        mock_client.get_exchange_info.return_value = {'symbols': []}

        symbols = get_list_of_symbols()
        self.assertEqual(symbols, [])

    @patch('src.broker_data.get_binance_client')
    def test_get_list_of_symbols_handles_missing_symbols_key(self, mock_get_binance_client):
        mock_client = MagicMock()
        mock_get_binance_client.return_value = mock_client
        mock_client.get_exchange_info.return_value = {}

        symbols = get_list_of_symbols()
        self.assertEqual(symbols, [])


if __name__ == '__main__':
    unittest.main()

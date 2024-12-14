import pandas as pd
from src.helpers import transform_data, transform_data_to_dataframe
from src.technical_analysis import calculate_exponential_moving_average
import unittest


class TestHelpers(unittest.TestCase):

    def test_transform_data_with_valid_input(self):
        raw_data = [
            [1609459200000, "29000.00", "29500.00", "28500.00", "29000.00", "1000.0", 1609545599999, "29000000.00", 1000, "500.0", "14500000.00", "0"]
        ]
        expected_output = [
            {
                "timestamp": 1609459200000,
                "open": 29000.00,
                "high": 29500.00,
                "low": 28500.00,
                "close": 29000.00,
                "volume": 1000.0,
                "close_time": 1609545599999,
                "quote_asset_volume": 29000000.00,
                "number_of_trades": 1000,
                "taker_buy_base_asset_volume": 500.0,
                "taker_buy_quote_asset_volume": 14500000.00,
                "ignore": "0"
            }
        ]
        self.assertEqual(transform_data(raw_data), expected_output)

    def test_transform_data_with_empty_input(self):
        raw_data = []
        expected_output = []
        self.assertEqual(transform_data(raw_data), expected_output)

    def test_transform_data_with_invalid_input(self):
        raw_data = [
            [1609459200000, "invalid", "29500.00", "28500.00", "29000.00", "1000.0", 1609545599999, "29000000.00", 1000, "500.0", "14500000.00", "0"]
        ]
        with self.assertRaises(ValueError):
            transform_data(raw_data)

    def test_transform_data_to_dataframe_with_valid_data(self):
        data = [
            {
                "timestamp": 1609459200000,
                "open": 29000.00,
                "high": 29500.00,
                "low": 28500.00,
                "close": 29000.00,
                "volume": 1000.0,
                "close_time": 1609545599999,
                "quote_asset_volume": 29000000.00,
                "number_of_trades": 1000,
                "taker_buy_base_asset_volume": 500.0,
                "taker_buy_quote_asset_volume": 14500000.00,
                "ignore": "0"
            }
        ]
        df = transform_data_to_dataframe(data)
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(df.shape[1], 12)
        self.assertEqual(df['timestamp'][0], pd.Timestamp('2021-01-01 00:00:00'))

    def test_transform_data_to_dataframe_with_empty_data(self):
        data = []
        df = transform_data_to_dataframe(data)
        self.assertTrue(df.empty)

    def test_transform_data_to_dataframe_with_invalid_data(self):
        data = [
            {
                "timestamp": "invalid",
                "open": 29000.00,
                "high": 29500.00,
                "low": 28500.00,
                "close": 29000.00,
                "volume": 1000.0,
                "close_time": 1609545599999,
                "quote_asset_volume": 29000000.00,
                "number_of_trades": 1000,
                "taker_buy_base_asset_volume": 500.0,
                "taker_buy_quote_asset_volume": 14500000.00,
                "ignore": "0"
            }
        ]
        with self.assertRaises(ValueError):
            transform_data_to_dataframe(data)


if __name__ == '__main__':
    unittest.main()
import unittest
from src.broker_data import get_test_data
import os
import json
from unittest.mock import patch, mock_open

class TestBrokerData(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
    @patch("os.path.join", return_value="tests/test_data.json")
    def test_get_test_data_returns_correct_data(self, mock_join, mock_file):
        expected_data = [{"key": "value"}]
        result = get_test_data()
        self.assertEqual(result, expected_data)

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.path.join", return_value="tests/test_data.json")
    def test_get_test_data_returns_empty_list_for_empty_file(self, mock_join, mock_file):
        expected_data = []
        result = get_test_data()
        self.assertEqual(result, expected_data)

    @patch("builtins.open", new_callable=mock_open, read_data='invalid json')
    @patch("os.path.join", return_value="tests/test_data.json")
    def test_get_test_data_raises_exception_for_invalid_json(self, mock_join, mock_file):
        with self.assertRaises(json.JSONDecodeError):
            get_test_data()

    @patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
    @patch("os.path.join", return_value="tests/test_data.json")
    @patch("os.path.dirname", return_value="src")
    def test_get_test_data_constructs_correct_path(self, mock_dirname, mock_join, mock_file):
        get_test_data()
        mock_join.assert_called_with("src", "..", "tests", "test_data.json")


if __name__ == '__main__':
    unittest.main()
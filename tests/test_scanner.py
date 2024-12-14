import json
from src.helpers import transform_data_to_dataframe
from src.scanner import scan_for_buy_signals
import unittest


class TestScanner(unittest.TestCase):

    def test_scan_for_buy_signals_with_test_data(self):
        with open('test_data.json', 'r') as f:
            test_data = json.load(f)

        with open('buy_signals.json', 'r') as f:
            expected_signals = json.load(f)

        test_data = transform_data_to_dataframe(test_data)
        buy_signals = scan_for_buy_signals(test_data)

        self.assertEqual(len(buy_signals), len(expected_signals))
        for i, signal in enumerate(expected_signals):
            self.assertEqual(buy_signals[i]['epoch_time'], signal['epoch_time'])
            self.assertEqual(buy_signals[i]['timestamp'], signal['timestamp'])
            self.assertEqual(buy_signals[i]['close'], signal['close'])
            self.assertEqual(buy_signals[i]['ema_50'], signal['ema_50'])
            self.assertEqual(buy_signals[i]['ema_200'], signal['ema_200'])
            self.assertEqual(buy_signals[i]['distance_from_50'], signal['distance_from_50'])
            self.assertEqual(buy_signals[i]['distance_from_200'], signal['distance_from_200'])

    def test_scan_for_buy_signals_with_invalid_data(self):
        with self.assertRaises(ValueError):
            scan_for_buy_signals(None)


if __name__ == '__main__':
    unittest.main()

import unittest
from src.technical_analysis import calculate_exponential_moving_average


class TestTechnicalAnalysis(unittest.TestCase):

    def test_calculate_exponential_moving_average_with_valid_data(self):
        data = [10, 20, 30, 40, 50, 60, 70]
        window = 3
        expected_output = [10.0, 15.0, 22.5, 31.25, 40.625, 50.3125, 60.15625]
        self.assertEqual(calculate_exponential_moving_average(data, window), expected_output)

    def test_calculate_exponential_moving_average_with_window_size_greater_than_data_length(self):
        data = [1, 2]
        window = 3
        with self.assertRaises(ValueError):
            calculate_exponential_moving_average(data, window)

    def test_calculate_exponential_moving_average_with_empty_data(self):
        data = []
        window = 3
        with self.assertRaises(ValueError):
            calculate_exponential_moving_average(data, window)


if __name__ == '__main__':
    unittest.main()
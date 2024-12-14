import os
import json


def get_test_data():
    # Get the path to the data file
    current_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(current_dir, '..', 'tests', 'test_data.json')

    # Read the JSON data from the file
    with open(data_file_path, 'r') as file:
        data = json.load(file)

    return data



# data/data_manager.py

import json

class DataManager:
    def __init__(self):
        self.collected_data = []

    def extract_data(self, raw_data):
        print("Extracting data...")
        extracted_data = [item.strip() for item in raw_data.split('\n') if item.strip()]
        return extracted_data

    def consolidate_data(self, new_data):
        print("Consolidating data...")
        self.collected_data.extend(new_data)
        return self.collected_data

    def save_data(self, filename='data.json'):
        print(f"Saving data to {filename}...")
        with open(filename, 'w') as file:
            json.dump(self.collected_data, file)

    def load_data(self, filename='data.json'):
        print(f"Loading data from {filename}...")
        try:
            with open(filename, 'r') as file:
                self.collected_data = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty data.")
            self.collected_data = []

    def filter_data(self, criteria):
        """
        Filter collected data based on given criteria.

        Args:
            criteria (function): A function that defines the filter logic.

        Returns:
            list: Filtered data.
        """
        return [item for item in self.collected_data if criteria(item)]

    def get_collected_data(self):
        return self.collected_data

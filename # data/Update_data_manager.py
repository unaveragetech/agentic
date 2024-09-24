# data/data_manager.py

class DataManager:
    def __init__(self):
        self.collected_data = []

    def extract_data(self, raw_data):
        # Extract relevant data from raw data (placeholder logic)
        print("Extracting data...")
        # For now, simply return the raw data as a list of strings
        extracted_data = [item.strip() for item in raw_data.split('\n') if item.strip()]
        return extracted_data

    def consolidate_data(self, new_data):
        # Consolidate newly extracted data with existing data
        print("Consolidating data...")
        self.collected_data.extend(new_data)
        return self.collected_data

# data/data_manager.py

import json

class DataManager:
    @staticmethod
    def save_data(data, filename='data.json'):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_data(filename='data.json'):
        with open(filename, 'r') as file:
            return json.load(file)


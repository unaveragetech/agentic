# data/storage.py

import json
import os

class StorageManager:
    def __init__(self, storage_file='data_storage.json'):
        self.storage_file = storage_file

    def save_data(self, data):
        # Save data to a JSON file
        print(f"Saving data to {self.storage_file}...")
        with open(self.storage_file, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_data(self):
        # Load data from a JSON file
        if not os.path.exists(self.storage_file):
            print("Storage file does not exist.")
            return None
        print(f"Loading data from {self.storage_file}...")
        with open(self.storage_file, 'r') as file:
            data = json.load(file)
        return data

# data/data_manager.py

import json

class DataManager:
    def __init__(self):
        self.collected_data = []

    def extract_data(self, raw_data):
        """
        Extract relevant data from raw data.
        
        Args:
            raw_data (str): Raw data as a string, typically fetched from web scraping.

        Returns:
            list: A list of extracted and cleaned strings.
        """
        print("Extracting data...")
        extracted_data = [item.strip() for item in raw_data.split('\n') if item.strip()]
        return extracted_data

    def consolidate_data(self, new_data):
        """
        Consolidate newly extracted data with existing data.
        
        Args:
            new_data (list): A list of newly extracted data.

        Returns:
            list: The updated list of consolidated data.
        """
        print("Consolidating data...")
        self.collected_data.extend(new_data)
        return self.collected_data

    def save_data(self, filename='data.json'):
        """
        Save the collected data to a JSON file.
        
        Args:
            filename (str): The name of the file to save data.
        """
        print(f"Saving data to {filename}...")
        with open(filename, 'w') as file:
            json.dump(self.collected_data, file)

    def load_data(self, filename='data.json'):
        """
        Load data from a JSON file into the collected data list.
        
        Args:
            filename (str): The name of the file to load data from.
        """
        print(f"Loading data from {filename}...")
        try:
            with open(filename, 'r') as file:
                self.collected_data = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty data.")
            self.collected_data = []

    def get_collected_data(self):
        """
        Retrieve the currently collected data.
        
        Returns:
            list: The list of collected data.
        """
        return self.collected_data

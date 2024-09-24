# config/settings.py

# config/settings.py

import json

class Settings:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.load_settings()

    def load_settings(self):
        # Load settings from a JSON file
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                self.base_url = config.get('base_url', "https://example.com")
                self.user_agent = config.get('user_agent', "Mozilla/5.0 ...")
                self.max_depth = config.get('max_depth', 3)
                self.timeout = config.get('timeout', 10)
                self.retry_attempts = config.get('retry_attempts', 3)
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found. Using defaults.")
            self.set_defaults()

    def set_defaults(self):
        # Set default values if config file not found
        self.base_url = "https://example.com"
        self.user_agent = "Mozilla/5.0 ..."
        self.max_depth = 3
        self.timeout = 10
        self.retry_attempts = 3

    def get_settings(self):
        return {
            "base_url": self.base_url,
            "user_agent": self.user_agent,
            "max_depth": self.max_depth,
            "timeout": self.timeout,
            "retry_attempts": self.retry_attempts,
        }

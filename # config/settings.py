# config/settings.py

class Settings:
    def __init__(self):
        self.base_url = "https://example.com"  # Base URL for crawling
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"  # User-Agent string
        self.max_depth = 3  # Maximum depth for crawling
        self.timeout = 10  # Timeout for requests in seconds
        self.retry_attempts = 3  # Number of retry attempts for failed requests

    def get_settings(self):
        # Return a dictionary of all settings
        return {
            "base_url": self.base_url,
            "user_agent": self.user_agent,
            "max_depth": self.max_depth,
            "timeout": self.timeout,
            "retry_attempts": self.retry_attempts,
        }

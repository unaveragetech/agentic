# main.py

from architecture.arch import ARCH
from config.settings import Settings
from utils.logger import Logger
from data.data_manager import DataManager

def main():
    # Initialize settings, logger, and data manager
    settings = Settings()
    logger = Logger()
    data_manager = DataManager()
    
    logger.log_info("Starting the web crawler...")

    # Get user inquiry
    user_inquiry = input("Please enter a research topic (e.g., 'web development using Python'): ")

    # Create an instance of ARCH
    arch = ARCH()

    # Process the user inquiry and gather results
    results = arch.process_user_inquiry(user_inquiry)

    # Log and save results
    logger.log_info("Crawling completed.")
    logger.log_info(f"Results: {results}")
    data_manager.save_data()

if __name__ == "__main__":
    main()

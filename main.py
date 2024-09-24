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

    # Create an instance of ARCH
    arch = ARCH()

    # Example user inquiry
    user_inquiry = "web development using Python"
    
    # Process the user inquiry and gather results
    results = arch.process_user_inquiry(user_inquiry)

    # Log and save results
    logger.log_info("Crawling completed.")
    logger.log_info(f"Results: {results}")
    data_manager.save_data(results)

if __name__ == "__main__":
    main()

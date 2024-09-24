# main.py

from architecture.arch import ARCH
from config.settings import Settings
from utils.logger import Logger

def main():
    # Initialize settings and logger
    settings = Settings()
    logger = Logger()
    
    # Log the start of the process
    logger.log("Starting the web crawler...")
    
    # Create an instance of ARCH
    arch = ARCH()
    
    # Example user inquiry
    user_inquiry = "web development using Python"
    
    # Process the user inquiry and gather results
    synthesized_data, results = arch.process_user_inquiry(user_inquiry)
    
    # Log the results
    logger.log("Crawling completed. Synthesized data:")
    logger.log(synthesized_data)
    
    # Optionally save results to storage
    # storage_manager = StorageManager()
    # storage_manager.save_data(synthesized_data)

if __name__ == "__main__":
    main()

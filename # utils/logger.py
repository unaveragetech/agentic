# utils/logger.py

import logging

class Logger:
    def __init__(self, log_file='crawler.log'):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def log(self, message):
        # Log a message to the log file
        logging.info(message)
        print(message)  # Print to console for real-time monitoring

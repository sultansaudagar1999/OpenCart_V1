import logging
import os
from datetime import datetime


class LoggerUtility:
    def __init__(self, log_level=logging.DEBUG):
        # Define the logs directory inside your project structure
        log_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_filename = os.path.join(log_folder, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # File handler for log file
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(log_level)

        # Formatter for log messages
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add handler to the logger
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

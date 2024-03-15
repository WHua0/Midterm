'''CSV File Checker'''
import os
import re
import logging

class CSVFileChecker:
    '''Class CSVFileChecker'''

    data_directory = "./data"

    @staticmethod
    def check_data_directory():
        '''Creates and checks if data directory is writable'''

        if not os.path.exists(CSVFileChecker.data_directory):
            os.makedirs(CSVFileChecker.data_directory)
            logging.info(f"Created '{CSVFileChecker.data_directory}' directory.")

        elif not os.access(CSVFileChecker.data_directory, os.W_OK):
            print(f"An error occurred: Directory '{CSVFileChecker.data_directory}' is not writable.")
            logging.error(f"Directory '{CSVFileChecker.data_directory}' is not writable.")
            return

    @staticmethod
    def check_file_writable(filepath):
        '''Checks if file is writable'''

        if os.path.exists(filepath):

            if not os.access(filepath, os.W_OK):
                print(f"An error occurred: File '{filepath}' is not writable.")
                logging.error(f"File '{filepath}' is not writable.")
                return False

        return True

    @ staticmethod
    def validate_filename(filename):
        '''Validates File Name'''

        if not re.match(r"^[a-zA-Z0-9_\-.]+$", filename):
            print(f"Invalid File Name: {filename}.")
            logging.warning(f"Invalid File Name: {filename}.")
            return False

        return True
    
    @staticmethod
    def get_filepath(directory, filename):
        '''Adds csv file extension'''

        filepath = os.path.join(directory, filename)

        if not filepath.endswith(".csv"):
            filepath += ".csv"

        if not CSVFileChecker.check_file_writable(filepath):
            return None

        return filepath
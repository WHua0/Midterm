'''CSV File Checker'''
import os
import re
import logging

class CSVFileChecker:
    '''Class CSVFileChecker'''

    data_directory = "./data"

    @staticmethod
    def check_data_directory():
        '''Creates or checks if Data Directory is writable'''

        if not os.path.exists(CSVFileChecker.data_directory):
            os.makedirs(CSVFileChecker.data_directory)
            logging.info(f"Created '{CSVFileChecker.data_directory}' directory.")
            return True

        elif not os.access(CSVFileChecker.data_directory, os.W_OK):
            print(f"An error occurred: Directory '{CSVFileChecker.data_directory}' is not writable.")
            logging.error(f"Directory '{CSVFileChecker.data_directory}' is not writable.")
            return False
        
        else:
            return True

    @staticmethod
    def check_file_writable(filepath):
        '''Checks if file is writable'''

        if os.path.exists(filepath):

            if not os.access(filepath, os.W_OK):
                print(f"An error occurred: File '{filepath}' is not writable.")
                logging.error(f"File '{filepath}' is not writable.")
                return False

        return True

    @staticmethod
    def check_file_exists(filepath):
        '''Checks if file exists '''

        if os.path.exists(filepath):
            return True

        else:
            print(f"File '{filepath}' was not found.")
            logging.warning(f"File '{filepath}' was not found.")
            return False

    @staticmethod
    def check_file_not_exists(filepath):
        '''Checks if file does not exists '''

        if not os.path.exists(filepath):
            return True

        else:
            print(f"File '{filepath}' already exists.")
            logging.warning(f"File '{filepath}' already exists.")
            return False

    @ staticmethod
    def validate_filename(filename):
        '''Validates Filename'''

        if not re.match(r"^[a-zA-Z0-9_\-.]+$", filename):
            print(f"Invalid File Name: {filename}.")
            logging.warning(f"Invalid File Name: {filename}.")
            return False

        return True

    @staticmethod
    def get_filepath(directory, filename):
        '''Adds CSV file extension and gets Filepath'''

        filepath = os.path.join(directory, filename)

        if not filepath.endswith(".csv"):
            filepath += ".csv"

        if not CSVFileChecker.check_file_writable(filepath):
            return False

        return filepath

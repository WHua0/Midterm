'''File Checker'''
import os
import re
import logging

class FileChecker:
    '''Class FileChecker'''

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
        if not filename.endswith(".csv"):
            filename += ".csv"
        return os.path.join(directory, filename)

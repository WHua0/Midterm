'''CSVHandler'''
import os
import pandas as pd
import logging
from app.csvhandler.csvfilechecker import CSVFileChecker

class CSVHandler:
    '''Class CSVHandler'''
    headers = ["Operator", "Operand_A", "Operand_B"]

    @staticmethod
    def create_csv_file(filename):
        '''Creates CSV File in data directory'''

        CSVFileChecker.check_data_directory()

        if not CSVFileChecker.validate_filename(filename):
            return

        filepath = CSVFileChecker.get_filepath(CSVFileChecker.data_directory, filename)

        if os.path.exists(filepath):
            print(f"File '{filename}' already exists.")
            logging.warning(f"File '{filename}' already exists.")
            return

        df = pd.DataFrame(columns = CSVHandler.headers)
        df.to_csv(filepath, index = True, index_label = "Index")
        print(f"File '{filename}' has been created.")
        logging.info(f"Created File '{filename}'.")
  

    @staticmethod
    def delete_csv_file(filename):
        '''Deletes CSV File in data directory'''

        CSVFileChecker.check_data_directory()

        if not CSVFileChecker.validate_filename(filename):
            return

        filepath = CSVFileChecker.get_filepath(CSVFileChecker.data_directory, filename)

        if not os.path.exists(filepath):
            print(f"File '{filename}' was not found.")
            logging.warning(f"File '{filename}' does not exist.")
            return

        os.remove(filepath)
        print(f"File '{filename}' has been deleted.")
        logging.info(f"Deleted File '{filename}'.")

def CSVFactory(operation, filename):
    '''CSV Factory Method'''

    if operation == "create":
        return CSVHandler.create_csv_file(filename)
    elif operation == "delete":
        return CSVHandler.delete_csv_file(filename)
    else:
        print(f"Invalid CSV Operation: {operation}.")
        logging.warning(f"Invalid CSV Operation: {operation}.")
        return None

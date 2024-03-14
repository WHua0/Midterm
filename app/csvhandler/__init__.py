'''CSVHandler'''
import os
import pandas as pd
import logging
from app.historyhandler.csvfilechecker import CSVFileChecker

class CSVHandler:
    '''Class CSVHandler'''
    headers = ["Operator", "Operand_A", "Operand_B"]

    @staticmethod
    def create_csv_file(filename, filepath):
        '''Creates CSV File in data directory'''

        if os.path.exists(filepath):
            print(f"File '{filename}' already exists.")
            logging.warning(f"File '{filename}' already exists.")
            return

        df = pd.DataFrame(columns = CSVHandler.headers)
        df.to_csv(filepath, index = True, index_label = "Index")
        print(f"File '{filename}' has been created.")
        logging.info(f"Created File '{filename}'.")
  

    @staticmethod
    def delete_csv_file(filename, filepath):
        '''Deletes CSV File in data directory'''

        if not os.path.exists(filepath):
            print(f"File '{filename}' was not found.")
            logging.warning(f"File '{filename}' does not exist.")
            return

        os.remove(filepath)
        print(f"File '{filename}' has been deleted.")
        logging.info(f"Deleted File '{filename}'.")
    
    @staticmethod
    def clear_csv_file(filename, filepath):
        '''Clears CSV File in data directory'''
    
        if not os.path.exists(filepath):
            print(f"File '{filename}' was not found.")
            logging.warning(f"File '{filename}' does not exist.")
            return

        df = pd.DataFrame(columns = CSVHandler.headers)
        df.to_csv(filepath, index = True, index_label = "Index")
        print(f"File '{filename}' has been cleared.")
        logging.info(f"Cleared File '{filename}'.")

def CSVFactory(operation, filename):
    '''CSV Factory Method'''

    CSVFileChecker.check_data_directory()

    if not CSVFileChecker.validate_filename(filename):
        return

    filepath = CSVFileChecker.get_filepath(CSVFileChecker.data_directory, filename)

    if filepath is None:
        return

    if operation == "create":
        return CSVHandler.create_csv_file(filename, filepath)
    elif operation == "delete":
        return CSVHandler.delete_csv_file(filename, filepath)
    elif operation == "clear":
        return CSVHandler.clear_csv_file(filename, filepath)
    else:
        print(f"Invalid CSV Operation: {operation}.")
        logging.warning(f"Invalid CSV Operation: {operation}.")
        return None

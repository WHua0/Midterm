'''CSVHandler'''
import os
import pandas as pd
import logging
import re

class CSVHandler:
    '''Class CSVHandler'''
    data_directory = "./data"
    headers = ["Operator", "Operand_A", "Operand_B"]

    @staticmethod
    def check_data_directory():
        '''Creates and checks if data directory is writable'''

        if not os.path.exists(CSVHandler.data_directory):
            os.makedirs(CSVHandler.data_directory)
            logging.info(f"Created '{CSVHandler.data_directory}' directory.")

        elif not os.access(CSVHandler.data_directory, os.W_OK):
            print(f"An error occurred: Directory '{CSVHandler.data_directory}' is not writable.")
            logging.error(f"Directory '{CSVHandler.data_directory}' is not writable.")
            return

    @staticmethod
    def create_csv_file(filename):
        '''Creates CSV File in data directory'''

        if not re.match(r"^[a-zA-Z0-9_\-.]+$", filename):
            print(f"Invalid File Name: {filename}.")
            logging.warning(f"Invalid File Name: {filename}.")
            return

        if not filename.endswith(".csv"):
            filename += ".csv"

        filepath = os.path.join(CSVHandler.data_directory, filename)

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

        if not re.match(r"^[a-zA-Z0-9_\-.]+$", filename):
            print(f"Invalid File Name: {filename}.")
            logging.warning(f"Invalid File Name: {filename}.")
            return

        if not filename.endswith(".csv"):
            filename += ".csv"

        filepath = os.path.join(CSVHandler.data_directory, filename)

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
        logging.error(f"Invalid CSV Operation: {operation}.")
        return None

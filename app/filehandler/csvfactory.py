'''CSVFactory'''
import os
import logging
import pandas as pd
from app.filehandler.csvfilechecker import CSVFileChecker
from app.historyhandler import HistoryHandler

class CSVHandler:
    '''Factory Class CSVHandler'''

    @staticmethod
    def save_history_to_csv_file(filename, filepath):
        '''Saves history to CSV File in directory'''

        if not CSVFileChecker.check_file_not_exists(filepath):
            return

        HistoryHandler.create_history()
        history_df = HistoryHandler.retrieve_history()
        history_df.to_csv(filepath, index = False)
        print(f"History has been saved to File {filename}.")
        logging.info(f"Saved history to file {filename}.")

    @staticmethod
    def delete_csv_file(filename, filepath):
        '''Deletes CSV File in directory'''

        if not CSVFileChecker.check_file_exists(filepath):
            return

        os.remove(filepath)
        print(f"File {filename} has been deleted.")
        logging.info(f"Deleted file {filename}.")

    @staticmethod
    def load_csv_file_to_history(filename, filepath):
        '''Loads CSV File in directory to history'''
        if not CSVFileChecker.check_file_exists(filepath):
            return

        try:
            history_df = pd.read_csv(filepath)
            history_instance = HistoryHandler.import_history(history_df)
            print(f"Loaded History from File {filename}.")
            logging.info(f"Loaded history from file {filename}.")
            return history_instance

        except Exception as e:
            print(f"An error occurred: {e}.")
            logging.error(f"{e}, Failed to load history from file {filepath}.")
            return None

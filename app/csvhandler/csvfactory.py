'''CSVFactory'''
import os
import logging
import pandas as pd
from app.csvhandler.csvfilechecker import CSVFileChecker
from app.historyhandler import HistoryHandler

class CSVHandler:
    '''Factory Class CSVHandler'''

    @staticmethod
    def save_history_to_csv_file(filename, filepath):
        '''Saves history to CSV File in directory'''

        if not CSVFileChecker.check_file_not_exists(filepath):
            return

        history_instance = HistoryHandler.create_history()
        history_df = HistoryHandler.retrieve_history(history_instance)
        history_df.to_csv(filepath, index = False)
        print(f"Saved History to File '{filename}'.")
        logging.info(f"Saved History to File '{filename}'.")

    @staticmethod
    def delete_csv_file(filename, filepath):
        '''Deletes CSV File in directory'''

        if not CSVFileChecker.check_file_exists(filepath):
            return

        os.remove(filepath)
        print(f"File '{filename}' has been deleted.")
        logging.info(f"Deleted File '{filename}'.")

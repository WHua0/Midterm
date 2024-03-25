'''HistoryHandler'''
from app.calculator.history import History
import pandas as pd

class HistoryHandler:
    '''Factory Class HistoryHandler'''

    @staticmethod
    def create_history():
        '''Creates History instance'''
        return History()

    @staticmethod
    def retrieve_history():
        '''Retrieves history from History instance'''
        return History().get_history()

    @staticmethod
    def clear_history():
        '''Clears history from History instance'''
        History().clear_history()

    @staticmethod
    def import_history(history_df):
        '''Imports data from a DataFrame to History instance'''
        history_instance = History()
        history_instance.history = history_df.copy()
        return history_instance
    
    @staticmethod
    def delete_calculation(index):
        '''Deletes calculation log at given index'''
        History().delete_log(index)

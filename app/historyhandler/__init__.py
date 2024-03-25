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
    def retrieve_history(history_instance):
        '''Retrieves history from an instance'''
        return history_instance.get_history()

    @staticmethod
    def clear_history(history_instance):
        '''Clears history from an instance'''
        history_instance.clear_history()

    @staticmethod
    def import_history(history_df):
        '''Imports data from a DataFrame to History instance'''
        history_instance = History()
        history_instance.history = history_df.copy()
        return history_instance
    
    @staticmethod
    def delete_calculation(history_instance, index):
        '''Deletes calculation log at given index'''
        history_instance.delete_log(index)

'''HistoryHandler'''
from app.calculator.history import History
import pandas as pd

class HistoryHandler:
    '''Factory Class HistoryHandler'''

    @staticmethod
    def create_history():
        '''Creates a history instance'''
        return History()

    @staticmethod
    def retrieve_history(history_instance):
        '''Retrieves history'''
        return history_instance.get_history()

    @staticmethod
    def clear_history(history_instance):
        '''Clears history'''
        history_instance.clear_history()

    @staticmethod
    def import_history(history_df):
        '''Imports a history instance from a DataFrame'''
        history_instance = History()
        history_instance.history = history_df.copy()
        return history_instance
    
    @staticmethod
    def delete_calculation(history_instance, index):
        '''Deletes calculation log at given index'''
        history_instance.delete_log(index)

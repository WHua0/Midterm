'''HistoryHandler'''
from app.calculator.history import History

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

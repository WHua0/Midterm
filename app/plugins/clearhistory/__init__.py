'''ClearHistory'''
import logging
import pandas as pd
from app.commandhandler import Command
from app.historyhandler import HistoryHandler

class ClearHistoryCommand(Command):
    '''ClearHistory Command'''

    def execute(self):
        history_handler = HistoryHandler()
        history_instance = history_handler.create_history()
        history_data = history_handler.retrieve_history(history_instance)
        df = pd.DataFrame(history_data)
        history_handler.clear_history(history_instance)

        print("History cleared.")
        logging.info(f"Cleared history\n{df}.")

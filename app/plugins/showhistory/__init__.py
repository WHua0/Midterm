'''ShowHistory'''
import logging
import pandas as pd
from app.commandhandler import Command
from app.historyhandler import HistoryHandler

class ShowHistoryCommand(Command):
    '''ShowHistory Command'''

    def execute(self):
        history_handler = HistoryHandler()
        history_instance = history_handler.create_history()
        history_data = history_handler.retrieve_history(history_instance)
        print("History:")
        df = pd.DataFrame(history_data)
        print(df.to_string(index = True))
        logging.info(f"Printed History:\n{df}")

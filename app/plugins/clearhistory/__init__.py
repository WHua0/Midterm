'''ClearHistory'''
import logging
from app.commandhandler import Command
from app.historyhandler import HistoryHandler

class ClearHistoryCommand(Command):
    '''ClearHistory Command'''

    def execute(self):
        history_handler = HistoryHandler()
        history_instance = history_handler.create_history()
        history_handler.clear_history(history_instance)

        print("History cleared.")
        logging.info(f"Cleared History.")

'''ClearHistory'''
import logging
from app.commandhandler import Command
from app.calculator.history import History

class ClearHistoryCommand(Command):
    '''ClearHistory Command'''

    def __init__(self, history: History):
        self.history = history

    def execute(self):
        self.history.clear_history()
        print("History cleared.")
        logging.info(f"Cleared History.")

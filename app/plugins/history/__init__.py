'''history'''
import logging
import pandas as pd
from app.commandhandler import Command
from app.calculator.history import History

class ShowHistoryCommand(Command):
    '''ShowHistory Command'''

    def __init__(self, history: History):
        self.history = history

    def execute(self):
        history_data = self.history.retrieve_history()
        print("History:")
        print(history_data)

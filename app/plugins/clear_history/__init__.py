'''Clear_History'''
import logging
from app.commandhandler import Command
from app.calculator import Calculator

class ClearHistoryCommand(Command):
    '''Clear History Command'''

    def execute(self):
        Calculator.clear_history()

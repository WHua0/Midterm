'''Show_History'''
import logging
from app.commandhandler import Command
from app.calculator import Calculator

class ShowHistoryCommand(Command):
    '''Show History Command'''

    def execute(self):
        Calculator.show_history()

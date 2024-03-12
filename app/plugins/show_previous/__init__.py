'''Show_Previous'''
import logging
from app.commandhandler import Command
from app.calculator import Calculator

class ShowPreviousCommand(Command):
    '''Show Previous Command'''

    def execute(self):
        Calculator.show_previous()

'''Divide'''
import logging
from app.commandhandler import Command
from app.calculator import Calculator

class DivideCommand(Command):
    '''Divide Command'''

    def execute(self):
        values = input("Please provide two numbers separated by a space: ").split()

        if len(values) == 2:
            a, b = values[0], values[1]
            logging.info(f"User inputted {a} and {b}.")
            Calculator.calculate_and_print(a, b, "divide")

        else:
            print(f"An error occurred: incorrect number of inputs.")
            values_string = " ".join(map(str, values))
            logging.warning(f"User inputted {values_string}, Failed to execute.")

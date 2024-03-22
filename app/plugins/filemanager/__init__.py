'''FileManager'''
import logging
from app.commandhandler import Command
from app.filehandler import FileHandler

class FileManagerCommand(Command):
    '''FileManager Command'''

    def execute(self):
        print("FileManager Commands: save / delete / load.")
        values = input("Please provide a Command and Filename separated by a space: ").split()

        if len(values) == 2:
            csvcommand, filename = values[0], values[1]
            logging.info(f"User inputted {csvcommand} and {filename}.")
            FileHandler.CSVCommands(csvcommand, filename)

        else:
            print(f"An error occurred: incorrect number of inputs.")
            values_string = " ".join(map(str, values))
            logging.warning(f"Incorrect number of inputs, User inputted {values_string}, Failed to execute.")

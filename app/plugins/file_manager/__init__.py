'''FileManager'''
import logging
from app.commandhandler import Command
from app.csvhandler import CSVHandler, CSV_Factory

class CSVCommand(Command):
    '''CSV Command'''

    def execute(self):
        CSVHandler.check_data_directory()
        print("CSV Commands: create / delete.")
        values = input("Please provide a Command and File Name separated by a space: ").split()

        if len(values) == 2:
            csvcommand, filename = values[0], values[1]
            logging.info("Inputs: '%s', '%s'.", csvcommand, filename)
            CSV_Factory(csvcommand, filename)

        else:
            print(f"An error occurred: incorrect number of inputs.")
            values_string = " ".join(map(str, values))
            logging.warning("Incorrect number of inputs: '%s'.", values_string)
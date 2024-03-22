'''ShowFiles'''
import os
import logging
from app.commandhandler import Command

class ShowFilesCommand(Command):
    '''ShowFiles Command'''

    def execute(self):
        from app.filehandler.csvfilechecker import CSVFileChecker

        if not CSVFileChecker.check_data_directory():
            return
        
        directory = CSVFileChecker.data_directory
        
        try:
             filenames = os.listdir(directory)

        except Exception as e:
            print(f"An error occurred: {e}.")
            logging.error(f"Exception {e}, Failed to print filenames in data directory {directory}.")
            return

        print("Filenames in Data Directory:")
        for filename in filenames:
            print(filename)
        logging.info("Printed filenames in data directory.")

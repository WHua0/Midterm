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
            print(f"Failed to list directory {directory}: {e}.")
            logging.error(f"Failed to list directory {directory}: {e}.")
            return

        print("Files in Data Directory:")
        for filename in filenames:
            print(filename)
        logging.info("Printed Data Directory.")

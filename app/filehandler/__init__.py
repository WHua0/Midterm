'''FileHandler'''
import logging
from app import App
from app.filehandler.csvfactory import CSVHandler
from app.filehandler.csvfilechecker import CSVFileChecker

class FileHandler:
    '''Class FileHandler'''

    @staticmethod
    def CSVCommands(operation, filename):
        '''CSV Commands'''

        data_directory = App.get_data_directory()

        CSVFileChecker.check_data_directory()

        if not CSVFileChecker.validate_filename(filename):
            return

        filepath = CSVFileChecker.get_filepath(data_directory, filename)

        if not filepath:
            return

        if operation == "save":
            return CSVHandler.save_history_to_csv_file(filename, filepath)
        elif operation == "delete":
            return CSVHandler.delete_csv_file(filename, filepath)
        elif operation == "load":
            return CSVHandler.load_csv_file_to_history(filename, filepath)
        else:
            print(f"Invalid File Operation: {operation}.")
            logging.warning(f"Invalid File Operation: {operation}.")
            return

# pylint: disable = duplicate-code

'''Test CSVFactory'''
import unittest
import os
from unittest.mock import patch
import pandas as pd
from app.filehandler.csvfactory import CSVHandler
from app.filehandler.csvfilechecker import CSVFileChecker

class TestCSVHandler(unittest.TestCase):
    '''Tests CSVFactory'''

    def setUp(self):
        '''Creates temporary test_data directory'''
        self.testdir = "./test_data"
        os.makedirs(self.testdir, exist_ok = True)

    @patch("logging.info")
    def test_save_history_to_csv_file(self, mock_logging_info):
        '''Tests CSVFactory.save_history_to_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        mock_logging_info.assert_called_once_with(f"Saved History to File '{filename}'.")

    @patch("logging.warning")
    def test_save_history_to_csv_file_if_file_already_exists(self, mock_logging_warning):
        '''Tests CSVFactory.save_history_to_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        mock_logging_warning.assert_called_once_with(f"File '{filepath}' already exists.")

    @patch("logging.info")
    def test_delete_csv_file(self, mock_logging_info):
        '''Tests CSVFactory.delete_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        CSVHandler.delete_csv_file(filename, filepath)
        mock_logging_info.assert_called_with(f"Deleted File '{filename}'.")

    @patch("logging.warning")
    def test_delete_csv_file_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVFactory.delete_csv_file if file does not exist'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.delete_csv_file(filename, filepath)
        mock_logging_warning.assert_called_with(f"File '{filepath}' was not found.")

    @patch("logging.info")
    def test_load_csv_file_to_history(self, mock_logging_info):
        '''Tests CSVFactory.load_csv_file_to_history'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        CSVHandler.load_csv_file_to_history(filename, filepath)
        mock_logging_info.assert_called_with(f"Loaded history from File '{filename}'.")

    @patch("logging.warning")
    def test_load_csv_file_to_history_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVFactory.load_csv_file_to_history if file does not exist'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.load_csv_file_to_history(filename, filepath)
        mock_logging_warning.assert_called_with(f"File '{filepath}' was not found.")

    @patch("logging.error")
    def test_load_csv_file_to_history_if_parsing_error(self, mock_logging_error):
        '''Tests CSVHandler.load_csv_file_to_history if parsing error'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.save_history_to_csv_file(filename, filepath)
        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.side_effect = pd.errors.ParserError("Error parsing CSV file")
            CSVHandler.load_csv_file_to_history(filename, filepath)
            mock_logging_error.assert_called_once_with(f"Failed to load history from CSV file '{filepath}': Error parsing CSV file")

    def tearDown(self):
        '''Deletes temporary test_data directory'''
        for filename in os.listdir(self.testdir):
            filepath = os.path.join(self.testdir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        os.rmdir(self.testdir)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover

# pylint: disable = unused-argument

"Test FileHandler"
import unittest
import os
from unittest.mock import patch
from app.filehandler import FileHandler
from app.filehandler.csvfilechecker import CSVFileChecker


class TestFileHandler(unittest.TestCase):
    '''Tests FileHandler'''

    def setUp(self):
        '''Creates temporary test_data directory'''
        self.testdir = "./test_data"
        os.makedirs(self.testdir, exist_ok = True)


    @patch("logging.warning")
    def test_invalid_filename(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid filename'''
        CSVFileChecker.data_directory = self.testdir
        filename = "$test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_warning.assert_called_once_with(f"Invalid File Name: {filename}.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_not_writable_filename(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests FileHandler.CVSCommands with unwritable file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_error.assert_called_with("File './test_data/test.csv' is not writable.")

    @patch("logging.info")
    def test_save_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Save'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_info.assert_called_once_with(f"Saved History to File '{filename}'.")

    @patch("logging.info")
    def test_delete_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Delete'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("delete", filename)
        mock_logging_info.assert_called_with(f"Deleted File '{filename}'.")

    @patch("logging.info")
    def test_load_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Load'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("load", filename)
        mock_logging_info.assert_called_with(f"Loaded history from File '{filename}'.")

    @patch("logging.warning")
    def test_invalid_command(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid command'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("invalid", filename)
        mock_logging_warning.assert_called_with("Invalid File Operation: invalid.")

    def tearDown(self):
        '''Deletes temporary test_data directory'''
        for filename in os.listdir(self.testdir):
            filepath = os.path.join(self.testdir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        os.rmdir(self.testdir)

if __name__ == "__main__":
    unittest.main() # pragma: no cover
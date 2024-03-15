"Test FileHandler"
import unittest
import os
from unittest.mock import patch
from app.filehandler import FileHandler


class TestFileHandler(unittest.TestCase):
    '''Tests FileHandler'''

    def tearDown(self):
        filename = "data/test.csv"
        if os.path.exists(filename):
            os.remove(filename)

    @patch("logging.warning")
    def test_invalid_filename(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid filename'''
        filename = "$test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_warning.assert_called_once_with(f"Invalid File Name: {filename}.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_not_writable_filename(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests FileHandler.CVSCommands with unwritable file'''
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_error.assert_called_with(f"File './data/test.csv' is not writable.")

    @patch("logging.info")
    def test_save_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Save'''
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_info.assert_called_once_with(f"Saved History to File '{filename}'.")
        
    @patch("logging.info")
    def test_delete_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Delete'''
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("delete", filename)
        mock_logging_info.assert_called_with(f"Deleted File '{filename}'.")

    @patch("logging.info")
    def test_load_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Load'''
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("load", filename)
        mock_logging_info.assert_called_with(f"Loaded history from File '{filename}'.")

    @patch("logging.warning")
    def test_invalid_command(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid command'''
        filename = "test.csv"
        FileHandler.CSVCommands("invalid", filename)
        mock_logging_warning.assert_called_with(f"Invalid File Operation: invalid.")

if __name__ == "__main__":
    unittest.main() # pragma: no cover

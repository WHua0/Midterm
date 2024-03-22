# pylint: disable = unused-argument
# pylint: disable = unused-variable
# pylint: disable = duplicate-code

"Test FileHandler"
import unittest
import os
from unittest.mock import patch
from app.filehandler import FileHandler



class TestFileHandler(unittest.TestCase):
    '''Tests FileHandler'''

    def setUp(self):
        '''Creates temporary test_data directory'''
        self.testdir = "./test_data"
        os.makedirs(self.testdir, exist_ok = True)


    @patch("logging.warning")
    def test_invalid_filename(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid filename'''
        data_directory = self.testdir
        filename = "$test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_warning.assert_called_once_with(f"Invalid File Name: {filename}.")

    @patch("app.filehandler.csvfilechecker.CSVFileChecker.get_filepath", return_value = None)
    def test_not_writable_filename(self, mock_get_filepath):
        '''Tests FileHandler.CVSCommands with unwritable file'''
        result = FileHandler.CSVCommands("save", "test.csv")
        self.assertIsNone(result)

    @patch("logging.info")
    def test_save_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Save'''
        data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        mock_logging_info.assert_called_with(f"Saved history to file {filename}.")

    @patch("logging.info")
    def test_delete_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Delete'''
        data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("delete", filename)
        mock_logging_info.assert_called_with(f"Deleted file {filename}.")

    @patch("logging.info")
    def test_load_csv_file(self, mock_logging_info):
        '''Tests FileHandler.CVSCommands Load'''
        data_directory = self.testdir
        filename = "test.csv"
        FileHandler.CSVCommands("save", filename)
        FileHandler.CSVCommands("load", filename)
        mock_logging_info.assert_called_with(f"Loaded history from file {filename}.")

    @patch("logging.warning")
    def test_invalid_command(self, mock_logging_warning):
        '''Tests FileHandler.CVSCommands with invalid command'''
        data_directory = self.testdir = self.testdir
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

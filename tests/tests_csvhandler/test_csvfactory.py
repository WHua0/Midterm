'''Test CSVFactory'''
import unittest
import os
from unittest.mock import patch
from app.csvhandler.csvfactory import CSVHandler
from app.csvhandler.csvfilechecker import CSVFileChecker

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

    def tearDown(self):
        '''Deletes temporary test_data directory'''
        for filename in os.listdir(self.testdir):
            filepath = os.path.join(self.testdir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        os.rmdir(self.testdir)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover

# pylint: disable = unused-argument
# pylint: disable = duplicate-code

'''Test ShowFiles'''
import unittest
import os
from unittest.mock import patch
from app.plugins.showfiles import ShowFilesCommand

class TestShowFilesCommand(unittest.TestCase):
    '''Tests ShowFilesCommand'''

    def setUp(self):
        '''Creates temporary test_data directory'''
        self.testdir = "./test_data"
        os.makedirs(self.testdir, exist_ok = True)
        fake_files = ["file1.txt", "file2.txt", "file3.txt"]
        for filename in fake_files:
            with open(os.path.join(self.testdir, filename), 'w', encoding='utf-8'):
                pass

    @patch("os.path.exists", return_value = True)
    @patch("os.makedirs")
    @patch("logging.info")
    def test_execute_with_valid_directory(self, mock_logging_info, mock_makedirs, mock_exist):
        '''Tests ShowFilesCommand if data directory exists'''
        show_files_command = ShowFilesCommand()
        show_files_command.execute()
        mock_logging_info.assert_called_once_with("Printed filenames in data directory.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error")
    def test_execute_with_invalid_directory(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests ShowFilesCommand if invalid data directory'''
        show_files_command = ShowFilesCommand()
        show_files_command.execute()
        mock_logging_error.assert_called_once_with("Directory './test_data' is not writable.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = True)
    @patch("os.listdir", side_effect = Exception("Mocked exception"))
    @patch("logging.error")
    def test_execute_handles_exception(self, mock_logging_error, mock_listdir, mock_access, mock_exists):
        '''Tests ShowFilesCommand exception handling'''
        show_files_command = ShowFilesCommand()
        show_files_command.execute()
        mock_logging_error.assert_called_once_with("Exception Mocked exception, Failed to print filenames in directory ./test_data.")

    def tearDown(self):
        '''Deletes temporary test_data directory'''
        for filename in os.listdir(self.testdir):
            filepath = os.path.join(self.testdir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        os.rmdir(self.testdir)

if __name__ == '__main__':
    unittest.main() # pragma: no cover

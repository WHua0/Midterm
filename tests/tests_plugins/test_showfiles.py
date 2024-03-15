# pylint: disable = unused-argument

'''Test ShowFiles'''
import unittest
from unittest.mock import patch
from app.plugins.showfiles import ShowFilesCommand

class TestShowFilesCommand(unittest.TestCase):
    '''Tests ShowFilesCommand'''

    @patch("os.path.exists", return_value = True)
    @patch("os.makedirs")
    @patch("logging.info")
    def test_execute_with_valid_directory(self, mock_logging_info, mock_makedirs, mock_exist):
        '''Tests ShowFilesCommand if data directory exists'''
        show_files_command = ShowFilesCommand()
        show_files_command.execute()
        mock_logging_info.assert_called_once_with("Printed Data Directory.")

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
        mock_logging_error.assert_called_once_with("Failed to list directory ./test_data: Mocked exception.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover

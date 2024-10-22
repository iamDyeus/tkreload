import unittest
import os
import sys
from unittest.mock import patch
from tkreload.file_utils import file_exists, clear_terminal

class TestFileUtils(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(file_exists(__file__))
        self.assertFalse(file_exists('non_existent_file.txt'))

    @patch('os.system')
    def test_clear_terminal_windows(self, mock_system):
        with patch.object(os, 'name', 'nt'):
            clear_terminal()
            mock_system.assert_called_once_with('cls')

    @patch('os.system')
    def test_clear_terminal_unix(self, mock_system):
        with patch.object(os, 'name', 'posix'):
            clear_terminal()
            mock_system.assert_called_once_with('clear')

    def test_file_exists_with_relative_path(self):
        relative_path = os.path.join('tests', 'test_file_utils.py')
        self.assertTrue(file_exists(relative_path))

if __name__ == '__main__':
    unittest.main()

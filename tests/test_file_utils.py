import unittest
import os
from src.tkreload.file_utils import file_exists, clear_terminal

class TestFileUtils(unittest.TestCase):

    def test_file_exists(self):
        # Test if file_exists detects an actual file
        test_file = __file__  # Current file should exist
        self.assertTrue(file_exists(test_file))
        
        # Test with a non-existent file
        self.assertFalse(file_exists('non_existent_file.txt'))

    def test_clear_terminal(self):
        try:
            clear_terminal()
            self.assertTrue(True)  # Ensure it runs without throwing errors
        except Exception as e:
            self.fail(f"clear_terminal() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()

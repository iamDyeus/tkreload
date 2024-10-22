import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tkreload.auto_reload import AutoReloadManager
from rich.console import Console


class TestAutoReloadManager(unittest.TestCase):

    def setUp(self):
        self.console = Console()
        self.manager = AutoReloadManager(self.console)

    def test_initial_status(self):
        # Test if the auto-reload is initially set to True
        self.assertTrue(self.manager.get_status())

    def test_toggle_off(self):
        # Test if toggling changes the auto-reload status to False
        self.manager.toggle()
        self.assertFalse(self.manager.get_status())

    def test_toggle_on(self):
        # Test if toggling twice turns auto-reload on again
        self.manager.toggle()  # First toggle to False
        self.manager.toggle()  # Second toggle to True
        self.assertTrue(self.manager.get_status())

if __name__ == '__main__':
    unittest.main()

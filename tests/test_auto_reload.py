import unittest
from src.tkreload.auto_reload import AutoReloadManager
from rich.console import Console

class TestAutoReloadManager(unittest.TestCase):

    def setUp(self):
        self.console = Console()
        self.manager = AutoReloadManager(self.console)

    def test_initial_status(self):
        # Test if the auto-reload is initially set to False
        self.assertFalse(self.manager.get_status())

    def test_toggle_on(self):
        # Test if toggling changes the auto-reload status to True
        self.manager.toggle()
        self.assertTrue(self.manager.get_status())

    def test_toggle_off(self):
        # Test if toggling twice turns auto-reload off again
        self.manager.toggle()  # First toggle to True
        self.manager.toggle()  # Second toggle to False
        self.assertFalse(self.manager.get_status())

if __name__ == '__main__':
    unittest.main()

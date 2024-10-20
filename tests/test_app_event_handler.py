import unittest
from src.tkreload.app_event_handler import AppFileEventHandler
from unittest.mock import Mock
from watchdog.events import FileModifiedEvent

class TestAppFileEventHandler(unittest.TestCase):

    def setUp(self):
        self.callback = Mock()
        self.handler = AppFileEventHandler(self.callback, 'test_app.py')

    def test_on_modified_app_file(self):
        # Simulate modifying the app file and check if callback is called
        event = FileModifiedEvent('test_app.py')
        self.handler.on_modified(event)
        self.callback.assert_called_once()

    def test_on_modified_unrelated_file(self):
        # Simulate modifying an unrelated file and ensure callback is not called
        event = FileModifiedEvent('other_file.py')
        self.handler.on_modified(event)
        self.callback.assert_not_called()

if __name__ == '__main__':
    unittest.main()

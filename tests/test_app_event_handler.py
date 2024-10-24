import unittest
from tkreload.app_event_handler import AppFileEventHandler
from tkreload.auto_reload import AutoReloadManager
from unittest.mock import Mock, MagicMock
from watchdog.events import FileModifiedEvent
from rich.console import Console

class TestAppFileEventHandler(unittest.TestCase):

    def setUp(self):
        self.callback = Mock()
        self.console = MagicMock(spec=Console)
        self.auto_reload_manager = AutoReloadManager(self.console)
        self.handler = AppFileEventHandler(self.callback, 'example/sample_app.py', self.auto_reload_manager)

    def test_on_modified_app_file_auto_reload_enabled(self):
        # Auto-reload is enabled by default
        event = FileModifiedEvent('example/sample_app.py')
        self.handler.on_modified(event)
        self.callback.assert_called_once()

    def test_on_modified_app_file_auto_reload_disabled(self):
        self.auto_reload_manager.toggle()  # Disable auto-reload
        event = FileModifiedEvent('example/sample_app.py')
        self.handler.on_modified(event)
        self.callback.assert_not_called()

    def test_on_modified_unrelated_file(self):
        event = FileModifiedEvent('other_file.py')
        self.handler.on_modified(event)
        self.callback.assert_not_called()

    def test_auto_reload_manager_toggle(self):
        initial_status = self.auto_reload_manager.get_status()
        self.auto_reload_manager.toggle()
        self.assertNotEqual(initial_status, self.auto_reload_manager.get_status())
        self.auto_reload_manager.toggle()
        self.assertEqual(initial_status, self.auto_reload_manager.get_status())

    def test_auto_reload_manager_initial_state(self):
        self.assertTrue(self.auto_reload_manager.get_status())

if __name__ == '__main__':
    unittest.main()

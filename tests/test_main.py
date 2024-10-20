import unittest
from unittest.mock import patch, Mock
from src.tkreload.main import TkreloadApp

class TestTkreloadApp(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_run_tkinter_app(self, mock_popen):
        app = TkreloadApp('test_app.py')
        process = Mock()
        mock_popen.return_value = process
        
        # Run the app and check if subprocess is called
        result = app.run_tkinter_app()
        mock_popen.assert_called_once_with(['python', 'test_app.py'])
        self.assertEqual(result, process)

    @patch('main.AppFileEventHandler')
    @patch('main.Observer')
    def test_monitor_file_changes(self, mock_observer, mock_event_handler):
        app = TkreloadApp('test_app.py')
        mock_callback = Mock()
        
        # Start monitoring and check if the observer was set up correctly
        observer = app.monitor_file_changes(mock_callback)
        mock_event_handler.assert_called_once_with(mock_callback, 'test_app.py')
        mock_observer().schedule.assert_called_once()

if __name__ == '__main__':
    unittest.main()

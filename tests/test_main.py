import unittest
from unittest.mock import patch, Mock, MagicMock
from tkreload.main import TkreloadApp, main
from rich.console import Console
import sys
import time
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


class TestTkreloadApp(unittest.TestCase):

    @patch("tkreload.main.subprocess.Popen")
    @patch("tkreload.main.show_progress")
    def test_run_tkinter_app(self, mock_show_progress, mock_popen):
        app = TkreloadApp("example/sample_app.py")
        process = Mock()
        mock_popen.return_value = process

        result = app.run_tkinter_app()
        mock_show_progress.assert_called_once()
        mock_popen.assert_called_once_with([sys.executable, "example/sample_app.py"])
        self.assertEqual(result, process)

    @patch("tkreload.main.Observer")
    @patch("tkreload.main.AppFileEventHandler")
    def test_monitor_file_changes(self, mock_event_handler, mock_observer):
        app = TkreloadApp("example/sample_app.py")
        mock_callback = Mock()

        observer = app.monitor_file_changes(mock_callback)
        mock_event_handler.assert_called_once()
        mock_observer().schedule.assert_called_once()
        mock_observer().start.assert_called_once()

    # @patch('tkreload.main.time.sleep', side_effect=KeyboardInterrupt)
    # @patch('tkreload.main.subprocess.Popen')
    # def test_start_keyboard_interrupt(self, mock_popen, mock_sleep):
    #     app = TkreloadApp('example/sample_app.py')
    #     mock_process = Mock()
    #     mock_popen.return_value = mock_process

    #     with self.assertRaises(SystemExit):
    #         app.start()

    #     mock_process.terminate.assert_called_once()

    @patch("tkreload.main.sys.argv", ["tkreload", "example/sample_app.py"])
    @patch("tkreload.main.file_exists", return_value=True)
    @patch("tkreload.main.TkreloadApp")
    def test_main_function(self, mock_tkreload_app, mock_file_exists):
        main()
        mock_file_exists.assert_called_once_with("example/sample_app.py")
        mock_tkreload_app.assert_called_once_with("example/sample_app.py")
        mock_tkreload_app().start.assert_called_once()

    @patch("tkreload.main.sys.argv", ["tkreload"])
    @patch("tkreload.main.Console")
    @patch("tkreload.main.argparse.ArgumentParser")
    def test_main_function_no_file_provided(self, mock_parser, mock_console):
        mock_parser_instance = Mock()
        mock_parser.return_value = mock_parser_instance
        mock_parser_instance.parse_args.side_effect = SystemExit(2)

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()

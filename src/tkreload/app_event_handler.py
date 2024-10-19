from watchdog.events import FileSystemEventHandler

class AppFileEventHandler(FileSystemEventHandler):
    """Handles file changes to trigger app reload."""

    def __init__(self, callback, app_file):
        self.callback = callback
        self.app_file = app_file  # Store the app_file to check against

    def on_modified(self, event):
        if event.src_path.endswith(self.app_file):  # Check if the modified file is the app_file
            self.callback()

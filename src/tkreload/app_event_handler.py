from watchdog.events import FileSystemEventHandler

class AppFileEventHandler(FileSystemEventHandler):
    """Handles file changes to trigger app reload."""

    def __init__(self, callback, app_file, auto_reload_manager):
        self.callback = callback
        self.app_file = app_file
        self.auto_reload_manager = auto_reload_manager

    def on_modified(self, event):
        if event.src_path.endswith(self.app_file) and self.auto_reload_manager.get_status():
            self.callback()

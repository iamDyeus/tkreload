from watchdog.events import FileSystemEventHandler

class AppFileEventHandler(FileSystemEventHandler):
    """Handles file changes to trigger app reload."""
    def __init__(self, callback, app_file, auto_reload_manager):
        self.callback = callback
        self.app_file = app_file
        self.auto_reload_manager = auto_reload_manager
        self.last_content = None

    def on_modified(self, event):
        """
        Called when a file is modified.

        This method checks if the modified file is the one being monitored
        and if the auto-reload manager is active. If the content of the file
        has changed, it triggers the provided callback function.

        Args:
            event: The event object containing information about the file modification.
        """
        if event.src_path.endswith(self.app_file) and self.auto_reload_manager.get_status():
            current_content = self.read_file_content(self.app_file)
            if current_content != self.last_content:
                self.last_content = current_content
                self.callback()

    def read_file_content(self, file_path):
        """
        Reads the content of a file.

        This method opens the specified file in read mode and returns its content
        as a string.

        Args:
            file_path (str): The path to the file to be read.

        Returns:
            str: The content of the file.
        """
        with open(file_path, 'r') as file:
            return file.read()

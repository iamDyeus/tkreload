from rich.console import Console

class AutoReloadManager:
    """Class to manage the auto-reload feature."""

    def __init__(self, console):
        self.console = console
        self.auto_reload = True  # Initially set to True

    def toggle(self):
        """Toggles the auto-reload feature on or off."""
        self.auto_reload = not self.auto_reload
        status = "Enabled" if self.auto_reload else "Disabled"
        self.console.print(f"[bold yellow]Auto-reload is now {status}.[/bold yellow]")

    def get_status(self):
        """Returns the current status of auto-reload."""
        return self.auto_reload

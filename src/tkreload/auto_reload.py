from rich.console import Console

class AutoReloadManager:
    """Class to manage the auto-reload feature."""

    def __init__(self,console):
        self.console = console
        self.auto_reload = False  # Initially set to False

    def toggle(self):
        """Toggles the auto-reload feature on or off."""
        self.console.print(f"[bold yellow]Auto-reload is currently {'enabled' if self.auto_reload else 'disabled'}.[/bold yellow]")
        self.auto_reload = not self.auto_reload
        self.console.print(f"[bold yellow]Auto-reload is now {'enabled' if self.auto_reload else 'disabled'}.[/bold yellow]")

    def get_status(self):
        """Returns the current status of auto-reload."""
        return self.auto_reload

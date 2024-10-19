# from rich.console import Console

# class AutoReloadManager:
#     """Class to manage the auto-reload feature."""

#     def __init__(self,console):
#         self.console = console
#         self.auto_reload = False  # Initially set to False

#     def toggle(self):
#         """Toggles the auto-reload feature on or off."""
#         self.console.print(f"[bold yellow]Auto-reload is currently {'enabled' if self.auto_reload else 'disabled'}.[/bold yellow]")
#         self.auto_reload = not self.auto_reload
#         self.console.print(f"[bold yellow]Auto-reload is now {'enabled' if self.auto_reload else 'disabled'}.[/bold yellow]")

#     def get_status(self):
#         """Returns the current status of auto-reload."""
#         return self.auto_reload

import threading
import time
from rich.console import Console

class AutoReloadManager:
    def __init__(self, console):
        self.console = console
        self.auto_reload = False
        self.stop_reload_event = threading.Event()

    def toggle(self):
        if self.auto_reload:
            self.console.print("[red]Stopping auto-reload...[/red]")
            self.stop_auto_reload()
        else:
            self.console.print("[green]Starting auto-reload...[/green]")
            self.start_auto_reload()

    def start_auto_reload(self):
        self.auto_reload = True
        self.stop_reload_event.clear()
        self.console.print("[green]Auto-reload is now ON.[/green]")
        threading.Thread(target=self._reload_loop).start()

    def stop_auto_reload(self):
        self.auto_reload = False
        self.stop_reload_event.set()
        self.console.print("[red]Auto-reload is now OFF.[/red]")

    def _reload_loop(self):
        while not self.stop_reload_event.is_set():
            self.console.print("[cyan]Reloading...[/cyan]")
            time.sleep(5)
        self.console.print("[yellow]Reloading stopped.[/yellow]")


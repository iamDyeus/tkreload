import sys
import subprocess
import time
import os
import keyboard  
from rich.console import Console 
from watchdog.observers import Observer
from .app_event_handler import AppFileEventHandler
from .file_utils import clear_terminal, file_exists
from .progress import show_progress
from .help import show_help
from .auto_reload import AutoReloadManager

class TkreloadApp:
    """Main application class for managing the Tkinter app."""

    def __init__(self, app_file):
        self.console = Console()
        self.auto_reload_manager = AutoReloadManager(console=self.console)  # Uncommented and initialized auto-reload manager
        self.app_file = app_file
        self.process = None
        self.observer = None

    def run_tkinter_app(self):
        """Run the given Tkinter app."""
        show_progress()  # [TODO]: need to implement this function, currently its just all show and no real work
        self.process = subprocess.Popen([sys.executable, self.app_file])
        return self.process

    def monitor_file_changes(self, on_reload):
        """Monitors app file for changes and triggers reload."""
        if self.observer:
            self.observer.stop()
            self.observer.join()

        event_handler = AppFileEventHandler(on_reload, self.app_file)  # Pass app_file to the handler
        self.observer = Observer()
        self.observer.schedule(event_handler, path=os.path.dirname(self.app_file) or '.', recursive=False)
        self.observer.start()
        return self.observer

    def restart_app(self):
        """Restarts the Tkinter app."""
        if self.process:
            self.console.log("[bold yellow]Restarting the Tkinter app...[/bold yellow]")
            self.process.terminate()
            self.process.wait()
            time.sleep(1)
            self.run_tkinter_app()

    def start(self):
        """Starts the application, including monitoring and handling commands."""
        self.run_tkinter_app()
        
        if self.auto_reload_manager.get_status():  # Start monitoring if auto-reload is enabled
            self.monitor_file_changes(self.restart_app)

        try:
            self.console.print("\n\n\t[bold cyan]Tkreload[/bold cyan] [bold blue]is running ✅\n\t[/bold blue]- Press [bold cyan]Enter + H[/bold cyan] for help,\n\t[bold cyan]- Enter + R[/bold cyan] to restart,\n\t[bold cyan]- Enter + A[/bold cyan] to toggle auto-reload (currently [bold magenta]{}[/bold magenta]),\n\t[bold red]- Ctrl + C[/bold red] to exit.".format("Enabled" if self.auto_reload_manager.get_status() else "Disabled"))

            # Setup keyboard listeners for commands
            keyboard.add_hotkey('enter+h', lambda: show_help("Enabled" if self.auto_reload_manager.get_status() else "Disabled"))
            keyboard.add_hotkey('enter+r', self.restart_app)
            keyboard.add_hotkey('enter+a', self.auto_reload_manager.toggle)  # Toggle auto-reload when 'Enter + A' is pressed

            while True:
                if self.auto_reload_manager.get_status():
                    self.monitor_file_changes(self.restart_app)
                time.sleep(1)

        except KeyboardInterrupt:
            self.console.print("[bold red]Ctrl + C detected. Exiting...[/bold red]")
            self.process.terminate()
            if self.observer:
                self.observer.stop()
                self.observer.join()

def main():
    if len(sys.argv) < 2:
        Console().print("[bold red]Error: No Tkinter app file provided![/bold red]")
        sys.exit(1)

    app_file = sys.argv[1]

    if not file_exists(app_file):
        Console().print(f"[bold red]Error: File '{app_file}' not found![/bold red]")
        sys.exit(1)

    tkreload_app = TkreloadApp(app_file)
    tkreload_app.start()

if __name__ == "__main__":
    clear_terminal()
    main()

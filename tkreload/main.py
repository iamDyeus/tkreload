import sys
import subprocess
import time
import os
import select
import platform
import argparse
from rich.console import Console
from watchdog.observers import Observer
from .app_event_handler import AppFileEventHandler
from .file_utils import clear_terminal, file_exists
from .progress import show_progress
from .help import show_help
from .auto_reload import AutoReloadManager

# Only import `msvcrt` on Windows
if platform.system() == "Windows":
    import msvcrt


class TkreloadApp:
    """Main application class for managing the Tkinter app."""

    def __init__(self, app_file):
        self.console = Console()
        self.auto_reload_manager = AutoReloadManager(console=self.console)
        self.app_file = app_file
        self.process = None
        self.observer = None
        self.reload_count = 0
        self.startup_time=0

    def run_tkinter_app(self):
        """Run the given Tkinter app."""
        show_progress()
        self.process = subprocess.Popen([sys.executable, self.app_file])
        return self.process

    def monitor_file_changes(self, on_reload):
        """Monitors app file for changes and triggers reload."""
        if self.observer:
            self.observer.stop()
            self.observer.join()

        event_handler = AppFileEventHandler(
            on_reload, self.app_file, self.auto_reload_manager
        )
        self.observer = Observer()
        self.observer.schedule(
            event_handler, path=os.path.dirname(self.app_file) or ".", recursive=False
        )
        self.observer.start()
        return self.observer

    def restart_app(self):
        """Restarts the Tkinter app."""
        if self.process:
            self.reload_count += 1
            self.console.log(
                f"[bold yellow]Restarting the Tkinter app... (x{self.reload_count})[/bold yellow]"
            )
            self.process.terminate()
            self.process.wait()
            time.sleep(1)
            self.run_tkinter_app()

    def start(self):
        """Starts the application, including monitoring and handling commands."""
        start_time = time.time()  # Record the start time
        self.run_tkinter_app()
        self.monitor_file_changes(self.restart_app)
        self.startup_time = (time.time() - start_time) * 1000  # Calculate startup time in milliseconds

        try:
            self.console.print(
                f"\n[bold white]Tkreload ✅[/bold white] [dim](ready in {self.startup_time:.2f} ms)[/dim]\n"
                f"\t[bold cyan]→[/bold cyan] [bold white]Auto-reload:[/bold white] [bold magenta]{'Enabled' if self.auto_reload_manager.get_status() else 'Disabled'}[/bold magenta]\n"
                "\t[bold cyan]→[/bold cyan] [bold white]Help:[/bold white] Press [bold cyan]H[/bold cyan]\n"
                "\t[bold cyan]→[/bold cyan] [bold white]Restart:[/bold white] Press [bold cyan]R[/bold cyan]\n"
                "\t[bold cyan]→[/bold cyan] [bold white]Exit:[/bold white] Press [bold red]Ctrl + C[/bold red]"
            )


            while True:
                if platform.system() == "Windows":
                    if msvcrt.kbhit():  # Check for keyboard input (Windows only)
                        user_input = (
                            msvcrt.getch().decode("utf-8").lower()
                        )  # Read single character input
                        self.handle_input(user_input)
                else:
                    # Use select for Unix-like systems
                    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                        user_input = sys.stdin.read(
                            1
                        ).lower()  # Capture a single character input
                        self.handle_input(user_input)

                time.sleep(0.1)

        except KeyboardInterrupt:
            self.console.print("[bold red]Ctrl + C detected. Exiting...[/bold red]")
            self.process.terminate()
            if self.observer:
                self.observer.stop()
                self.observer.join()

    def handle_input(self, user_input):
        """Handles the user input commands."""
        if user_input == "h":
            show_help(
                "Enabled" if self.auto_reload_manager.get_status() else "Disabled"
            )
        elif user_input == "r":
            self.restart_app()
        elif user_input == "a":
            self.toggle_auto_reload()

    def toggle_auto_reload(self):
        """Toggles auto-reload and updates file monitoring accordingly."""
        self.auto_reload_manager.toggle()
        if self.auto_reload_manager.get_status():
            self.reload_count = 0
        status = "Enabled" if self.auto_reload_manager.get_status() else "Disabled"


def main():
    parser = argparse.ArgumentParser(
        description="Real-time reload Tkinter app",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("app_file", help="Tkinter app file path")

    args = parser.parse_args()

    app_file = args.app_file

    if not file_exists(app_file):
        Console().print(f"[bold red]Error: File '{app_file}' not found![/bold red]")
        sys.exit(1)

    tkreload_app = TkreloadApp(app_file)
    tkreload_app.start()


if __name__ == "__main__":
    clear_terminal()
    main()

import sys
import subprocess
import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import keyboard  # For capturing keypresses
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# probably this shit works fine, when I tried breaking it up for making a library, then it created a mess for me!

console = Console()
auto_reload = False  # Initially set to False

class AppFileEventHandler(FileSystemEventHandler):
    """Handles file changes to trigger app reload."""
    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        if auto_reload and event.src_path.endswith(app_file):  # Only reload if auto-reload is enabled
            self.callback()

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_tkinter_app(app_file):
    """Run the given Tkinter app."""
    console.log("[bold green]Starting Tkinter app...[/bold green]")

    # Adding progress animation between start and completion of the app.
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Booting Tkinter app...[/bold green]"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True  # This hides the progress bar once done.
    ) as progress:
        task = progress.add_task("[green]Starting up...", total=100)

        # Simulating progress
        for _ in range(10):
            progress.update(task, advance=2)
            time.sleep(0.05)  # Simulates some delay between steps

    process = subprocess.Popen([sys.executable, app_file])
    
    console.log("[bold green]Tkinter app started...[/bold green]")
    return process

def show_help():
    """Displays help commands with detailed info and rich formatting."""
    clear_terminal()
    console.print("\n[bold yellow]Tkreload Help:[/bold yellow]")
    console.print("[bold blue]-----------------------------------------[/bold blue]")
    console.print("[bold cyan]Enter + H[/bold cyan]     : Display this help section.")
    console.print("[bold cyan]Enter + R[/bold cyan]     : Restart the Tkinter app.")
    console.print("[bold cyan]Enter + A[/bold cyan]     : Toggle auto-reload (currently [bold magenta]{}[/bold magenta]).".format("Enabled" if auto_reload else "Disabled"))
    console.print("[bold red]Ctrl + C[/bold red] : Exit the development server.")
    console.print("[bold blue]-----------------------------------------[/bold blue]\n")

def toggle_auto_reload():
    """Toggles the auto-reload feature on or off."""
    global auto_reload
    auto_reload = not auto_reload
    console.print(f"[bold yellow]Auto-reload is now {'enabled' if auto_reload else 'disabled'}.[/bold yellow]")

def monitor_file_changes(app_file, on_reload):
    """Monitors app file for changes and triggers reload."""
    event_handler = AppFileEventHandler(on_reload)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(app_file) or '.', recursive=False)
    observer.start()
    return observer

def main():
    global app_file
    if len(sys.argv) < 2:
        console.print("[bold red]Error: No Tkinter app file provided![/bold red]")
        console.print("Usage: python tkinter_dev_server.py <app_file>")
        sys.exit(1)

    app_file = sys.argv[1]

    if not os.path.exists(app_file):
        console.print(f"[bold red]Error: File '{app_file}' not found![/bold red]")
        sys.exit(1)

    def restart_app():
        """Restarts the Tkinter app."""
        nonlocal process
        console.log("[bold yellow]Restarting the Tkinter app...[/bold yellow]")
        process.terminate()
        process.wait()
        time.sleep(1)
        process = run_tkinter_app(app_file)

    process = run_tkinter_app(app_file)

    # Monitor file changes for auto-reload
    observer = monitor_file_changes(app_file, restart_app)

    try:
        # Startup message with auto-reload status
        console.print("\n\n\t[bold cyan]Tkreload[/bold cyan] [bold blue]is running ✅\n\t[/bold blue]- Press [bold cyan]Enter + H[/bold cyan] for help,\n\t[bold cyan]- Enter + R[/bold cyan] to restart,\n\t[bold cyan]- Enter + A[/bold cyan] to toggle auto-reload (currently [bold magenta]{}[/bold magenta]),\n\t[bold red]- Ctrl + C[/bold red] to exit.".format("Enabled" if auto_reload else "Disabled"))

        # Set up keyboard listeners with the combination of Enter + key
        keyboard.add_hotkey('enter+h', show_help)
        keyboard.add_hotkey('enter+r', restart_app)
        keyboard.add_hotkey('enter+a', toggle_auto_reload)

        # Keep the program running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        console.print("[bold red]Ctrl + C detected. Exiting...[/bold red]")
        process.terminate()
        process.wait()
        observer.stop()
        observer.join()

if __name__ == "__main__":
    clear_terminal()
    main()

# /src/tkreload/progress.py

import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def show_progress():
    """Display a progress animation when starting the app."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Booting Tkinter app...[/bold green]"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True
    ) as progress:
        task = progress.add_task("[green]Starting up...", total=100)
        for _ in range(10):
            progress.update(task, advance=2)
            time.sleep(0.05)

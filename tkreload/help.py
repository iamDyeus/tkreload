# /src/tkreload/help.py

from rich.console import Console

console = Console()

def show_help(auto_reload):
    """Displays help commands with detailed info and rich formatting."""
    console.print("\n[bold yellow]Tkreload Help:[/bold yellow] [dim](detailed command info)[/dim]\n")
    console.print("[bold cyan]→[/bold cyan] [bold white]Press H[/bold white]     : Display this help section.")
    console.print("[bold cyan]→[/bold cyan] [bold white]Press R[/bold white]     : Restart the Tkinter app.")
    console.print(
        f"[bold cyan]→[/bold cyan] [bold white]Press A[/bold white]     : Toggle auto-reload "
        f"(currently [bold magenta]{auto_reload}[/bold magenta])."
    )
    console.print("[bold cyan]→[/bold cyan] [bold white]Ctrl + C[/bold white] : Exit the development server.\n")

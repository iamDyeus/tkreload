# /src/tkreload/help.py

from rich.console import Console

console = Console()

def show_help(auto_reload):
    """Displays help commands with detailed info and rich formatting."""
    console.print("\n[bold yellow]Tkreload Help:[/bold yellow]")
    console.print("[bold blue]-----------------------------------------[/bold blue]")
    console.print("[bold cyan]Enter + H[/bold cyan]     : Display this help section.")
    console.print("[bold cyan]Enter + R[/bold cyan]     : Restart the Tkinter app.")
    console.print("[bold cyan]Enter + A[/bold cyan]     : Toggle auto-reload (currently [bold magenta]{}[/bold magenta]).".format("Enabled" if auto_reload else "Disabled"))
    console.print("[bold red]Ctrl + C[/bold red] : Exit the development server.")
    console.print("[bold blue]-----------------------------------------[/bold blue]\n")

# /src/tkreload/file_utils.py

import os
import sys

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.exists(file_path)

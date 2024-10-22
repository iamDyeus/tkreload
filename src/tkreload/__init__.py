"""
Tkreload: A tool for automatically reloading Tkinter applications during development.

This package provides functionality to monitor and automatically reload Tkinter
applications, enhancing the development workflow for Tkinter-based projects.
"""


from .main import TkreloadApp, main
from .auto_reload import AutoReloadManager
from .help import show_help

__all__ = ["TkreloadApp", "AutoReloadManager", "show_help"]

__version__ = "1.0.0"
__author__ = "iamDyeus"
__license__ = "Apache 2.0"
__email__ = "dyeusyt@gmail.com"

'''This file:

Imports the MainWindow class that we'll create later in main_window.py
Imports the widgets subpackage to make it available
Uses __all__ to specify which names should be exported when using from quantum_gui.gui import *
This structure allows users to:

Import the main window directly: from quantum_gui.gui import MainWindow
Access widgets through: from quantum_gui.gui.widgets import CircuitView, HistogramView, ...
Make sure to create the main_window.py file in the same directory later.'''

from .main_window import MainWindow

__all__ = ['MainWindow']
#from . import widgets
#__all__ = [
#    'MainWindow',
#    #'widgets'
#]
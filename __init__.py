# __init__.py

# Import classes or functions from app.py
from .app import substitute_text  # Assuming main_function is a function in app.py

# Import mappings from mappings.py
from .mappings import mappings
from .filehandling import fh

# __all__ is a list of public objects of that module, as interpreted by import *
__all__ = ['substitute_text', 'mappings', 'fh']
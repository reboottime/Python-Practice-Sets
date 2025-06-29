"""Calculator package for mathematical operations."""

__version__ = '1.0.0'
__author__ = 'Kate'

from .basic_ops import add, substract
from .addvanced_ops import multiply, divide

# Package-level initialization
print(f"Calculator package v{__version__} loaded")

# Define what gets imported with "from calculator import *" or what methods package exports
__all__ = ['add', 'substract', 'multiply', 'divide']

"""
pytextlib: A collection of simple utility functions for text processing.

This package provides reliable, easy-to-use tools for common and repetitive
text-manipulation tasks in Python. Each function is designed to be clear,
robust, and self-documented.
"""

from .formatter import slugify, truncate_text, generate_initials
from .parser import parse_csv
from .validator import is_email

__all__ = [
    "slugify",
    "truncate_text",
    "generate_initials",
    "parse_csv",
    "is_email",
]
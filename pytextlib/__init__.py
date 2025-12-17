"""
pytextlib: A collection of simple utility functions for text processing.

This package provides reliable, easy-to-use tools for common and repetitive
text-manipulation tasks in Python. Each function is designed to be clear,
robust, and self-documented.
"""

from .analyzer import analyze_text
from .extractor import extract_emails
from .formatter import convert_case, generate_initials, slugify, truncate_text
from .parser import parse_csv
from .validator import is_email

__all__ = [
    "analyze_text",
    "convert_case",
    "extract_emails",
    "generate_initials",
    "is_email",
    "parse_csv",
    "slugify",
    "truncate_text",
]
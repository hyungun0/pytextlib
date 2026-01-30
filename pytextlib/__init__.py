"""
pytextlib: A collection of simple utility functions for text processing.

This package provides reliable, easy-to-use tools for common and repetitive
text-manipulation tasks in Python. Each function is designed to be clear,
robust, and self-documented.
"""

from .extractor import extract_emails, extract_urls
from .formatter import convert_case, mask_email, mask_middle, mask_text, remove_all_whitespace, remove_digits, remove_lines_containing, remove_newlines, remove_punctuation, slugify
from .parser import parse_csv
from .validator import has_digits, is_blank, is_email, is_ip, is_mac_address, is_url, validate_filename

__all__ = [
    "convert_case",
    "extract_emails",
    "extract_urls",
    "has_digits",
    "is_blank",
    "is_email",
    "is_ip",
    "is_mac_address",
    "is_url",
    "mask_email",
    "mask_middle",
    "mask_text",
    "parse_csv",
    "remove_all_whitespace",
    "remove_lines_containing",
    "remove_digits",
    "remove_newlines",
    "remove_punctuation",
    "slugify",
    "validate_filename"
]
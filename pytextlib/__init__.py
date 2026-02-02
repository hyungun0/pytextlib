"""
pytextlib: A text processing library dedicated to Data Sanitization.

This package focuses on normalizing and validating 'dirty' human input data.
It helps developers easily convert inconsistent user inputs (like "yes/no", 
"-", "N/A") into standard Python types, ensuring data integrity before 
database storage or processing.
"""

from .extractor import extract_emails, extract_urls
from .formatter import convert_case, empty_to_none, mask_email, mask_middle, mask_text, remove_all_whitespace, remove_digits, remove_lines_containing, remove_newlines, remove_punctuation, slugify, str_to_bool
from .parser import parse_csv
from .validator import has_digits, is_blank, is_email, is_ip, is_mac_address, is_url, validate_filename

__all__ = [
    "convert_case",
    "empty_to_none",
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
    "str_to_bool",
    "validate_filename"
]
# pytextlib

A collection of simple utility functions for common text-processing tasks in Python.

This project was created to provide reliable, easy-to-use tools for the small but repetitive challenges often found when working with text.

---

## ✨ Features

`pytextlib` offers a comprehensive suite of utilities to handle nearly any text-processing task.

*   **Formatting & Transformation:**
    *   `convert_case`: Convert strings between snake, camel, pascal, kebab, and constant cases.
    *   `generate_initials`: Create uppercase initials from names or phrases.
    *   `mask_text` / `mask_email`: Protect sensitive data by partially hiding strings or emails.
    *   `pad_text`: Reach target width with custom characters and alignment (left/right).
    *   `remove_punctuation`: Strip symbols and keep only alphanumeric characters.
    *   `slugify`: Generate URL-friendly strings.
    *   `truncate_text`: Shorten text without cutting words (smart truncate).

*   **Extraction:**
    *   `extract_emails`: Find and list all email addresses within a text.
    *   `extract_urls`: Extract all web links (http/https) using robust regex patterns.

*   **Analysis & Comparison:**
    *   `analyze_text`: Get instant stats (character, word, and line counts).
    *   `find_string_diff`: Identify differences between two strings at the word level.

*   **Validation:**
    *   `is_blank`: Detect if a string is empty or contains only whitespace.
    *   `is_email`: Validate if a string follows proper email formatting.
    *   `validate_filename`: Check if a filename is safe based on cross-platform OS standards.

> For a complete list of all functions, please see the `pytextlib/__init__.py` file.

---

## 🚀 Installation
    
While this library is not yet on PyPI, you can install it directly from GitHub using `pip`:

```bash
pip install git+https://github.com/hyungun0/pytextlib.git
```

---

## ✍️ Usage

Each function is fully documented with detailed docstrings. You can view usage instructions directly in your code editor or by using Python's built-in `help()` function.

**Basic Example (`slugify`):**

```python
from pytextlib import slugify

# The docstring for slugify will appear in your editor!
url_slug = slugify("Hello, World! This is pytextlib.")
print(url_slug)
# Output: hello-world-this-is-pytextlib
```

---

## 🗺️ Roadmap

Future plans for `pytextlib`:

*   **PyPI Support:** Prepare for official release so you can `pip install pytextlib`.
*   **Testing:** Add unit tests to make sure everything works correctly.
*   **More Tools:** Keep adding small, useful text functions as needed.
*   **Zero Dependencies:** Always use pure Python (no external libraries).

---

## ⚖️ License

This project is licensed under the MIT License.
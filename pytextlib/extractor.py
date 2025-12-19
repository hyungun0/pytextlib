import re

# --- Patterns ---
DEFAULT_EMAIL_PATTERN = re.compile(r"""[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@
(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?""", re.IGNORECASE | re.VERBOSE)

RFC5322_EMAIL_PATTERN = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
  |  "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]
      |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
@ (?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?
  |  \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
       (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:
          (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]
          |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])+)
     \])""", re.IGNORECASE | re.VERBOSE)

URL_PATTERN = r"https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,63}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)"

def extract_emails(input_string: str, extract_mode: str = "default") -> list[str]:
    """
    Extracts all email addresses from a given string.

    Args:
        input_string (str): The text containing email addresses.
        extract_mode (str, optional): The extraction mode to use.
                              'default': A practical regex for common email formats.
                              'rfc5322': Currently uses the same robust pattern as default.
                              Defaults to 'default'.

    Returns:
        list[str]: A list of extracted email addresses.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If an unknown mode is specified.
    """

    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    extract_mode = extract_mode.lower()
    
    # --- Core Logic ---
    if extract_mode == "default":
        return re.findall(DEFAULT_EMAIL_PATTERN, input_string)
    elif extract_mode == "rfc5322":
        return re.findall((RFC5322_EMAIL_PATTERN), input_string)
    else:
        raise ValueError(f"Unknown mode: '{extract_mode}'. Available modes are 'default' and 'rfc5322'.")
    
def extract_urls(input_string: str) -> list[str]:
    """
    Extracts all URLs starting with http or https from a given string.

    Args:
        input_string (str): The text containing URLs.

    Returns:
        list[str]: A list of extracted URLs.
    """

    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    return re.findall(URL_PATTERN, input_string)
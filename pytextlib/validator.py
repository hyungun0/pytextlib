import re

# --- Patterns ---
DEFAULT_EMAIL_PATTERN = re.compile(r"""\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@
(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$""", re.IGNORECASE | re.VERBOSE)

RFC5322_EMAIL_PATTERN = re.compile(r"""\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
  |  "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]
      |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
@ (?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?
  |  \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
       (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:
          (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]
          |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])+)
     \])$""", re.IGNORECASE | re.VERBOSE)

def is_email(input_string: str, mode: str = "default") -> bool:
    """
    Validates if a string is a well-formed email address.

    Args:
        input_string (str): The string to validate.
        mode (str, optional): The validation mode to use.
                              'default': A practical regex for common email formats.
                              'rfc5322': A stricter regex compliant with the RFC 5322 standard.
                              Defaults to 'default'.

    Returns:
        True if the string is a valid email according to the specified mode,
        False otherwise.

    Raises:
        ValueError: If an unknown mode is specified.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    # --- Core Logic ---
    if mode == "default":
        return bool(re.fullmatch(DEFAULT_EMAIL_PATTERN, input_string))
    elif mode == "rfc5322":
        return bool(re.fullmatch(RFC5322_EMAIL_PATTERN, input_string))
    else:
        raise ValueError(f"Unknown mode: '{mode}'. Available modes are 'default' and 'rfc5322'.")
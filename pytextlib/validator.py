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

def is_email(input_string: str, validation_mode: str = "default") -> bool:
    """
    Validates if a string is a well-formed email address.

    Args:
        input_string (str): The string to validate.
        validation_mode (str, optional): The validation mode to use.
                              'default': A practical regex for common email formats.
                              'rfc5322': A stricter regex compliant with the RFC 5322 standard.
                              Defaults to 'default'.

    Returns:
        True if the string is a valid email according to the specified mode,
        False otherwise.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If an unknown mode is specified.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    validation_mode = validation_mode.lower()
    
    # --- Core Logic ---
    if validation_mode == "default":
        return bool(re.fullmatch(DEFAULT_EMAIL_PATTERN, input_string))
    elif validation_mode == "rfc5322":
        return bool(re.fullmatch(RFC5322_EMAIL_PATTERN, input_string))
    else:
        raise ValueError(f"Unknown mode: '{validation_mode}'. Available modes are 'default' and 'rfc5322'.")


def is_blank(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is empty or whitespace only, False otherwise.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # --- Core Logic ---
    return not input_string.strip()


def validate_filename(input_string: str) -> bool:
    """
    Validates a filename against OS standards and raises detailed errors if invalid.

    Args:
        input_string (str): The filename to validate.

    Returns:
        bool: True if the filename is valid.

    Raises:
        TypeError: If input_string is not a string.
        ValueError: If the filename is empty, too long, contains forbidden 
                    characters, uses reserved names, or has invalid trailing chars.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    if len(input_string) < 1 or len(input_string) > 255:
        raise ValueError("Input 'input_string' must be between 1 and 255 characters.")
    
    forbidden_chars = "<>:\"/\|?*"
    for char in input_string:
        if char in forbidden_chars:
            raise ValueError(f"Input 'input_string' contains a forbidden character: {char}")

        if ord(char) < 32:
            raise ValueError("Input 'input_string' contains invalid control characters.")

    reserved_names = (
    "CON", "PRN", "AUX", "NUL", 
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", 
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    )
    pure_text = input_string.split('.')[0].upper()
    if pure_text in reserved_names:
        raise ValueError(f"Input 'input_string' uses a reserved name: {pure_text}")

    if input_string.endswith((' ', '.')):
        raise ValueError("Input 'input_string' cannot end with a space or a period.")

    return True
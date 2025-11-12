def truncate_text(input_string: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncates a string to a specified maximum length and appends a suffix.

    If the length of the input string is less than or equal to `max_length`,
    the original string is returned without any changes.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum allowed length. Must be a positive integer.
        suffix (str, optional): The string to append if truncated. Defaults to "...".

    Returns:
        str: The truncated string, or the original string.

    Raises:
        TypeError: If an input has an inappropriate type.
        ValueError: If `max_length` is not a positive integer.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    if not isinstance(max_length, int):
        raise TypeError("Input 'max_length' must be an integer.")

    if max_length <= 0:
        raise ValueError("Input 'max_length' must be a positive integer.")

    # --- Core Logic ---
    if len(input_string) > max_length:
        return input_string[:max_length] + suffix
    else:
        return input_string
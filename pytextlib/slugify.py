def slugify(input_string: str, force_lowercase: bool = True, separator: str = '-') -> str:
    """
    Converts a string into a URL-friendly slug.

    Args:
        input_string (str): The string to convert.
        force_lowercase (bool, optional): Converts to lowercase if True. Defaults to True.
        separator (str, optional): The character to replace spaces with. Defaults to '-'.

    Returns:
        str: The converted slug string.

    Raises:
        ValueError: If the separator is invalid.
    """
    # --- Input Validation ---
    if len(separator) > 1 or separator.isalnum():
        raise ValueError("Separator must be a single, non-alphanumeric character.")
        
    # --- Core Logic ---
    text = input_string
    if force_lowercase:
        text = text.lower()
    text = text.replace(' ', separator)
    
    slug = ""
    for char in text:
        if char.isalnum() or char == separator:
            slug += char

    return slug
import re

def slugify(input_string: str, force_lowercase: bool = True, separator: str = '-') -> str:
    """
    Converts a string into a URL-friendly slug.

    Args:
        input_string (str): The string to convert.
        force_lowercase (bool, optional): Converts to lowercase if True. Defaults to True.
        separator (str, optional): The character to replace spaces with. Defaults to '-'.

    Returns:
        str: The converted slug string.
[]
    Raises:
        ValueError: If the separator is invalid.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    if len(separator) > 1 or separator.isalnum():
        raise ValueError("Separator must be a single, non-alphanumeric character.")
        
    # --- Core Logic ---
    text = input_string
    if force_lowercase:
        text = text.lower()
    text = text.replace(' ', separator)
    
    slug = ""
    for character in text:
        if character.isalnum() or character == separator:
            slug += character

    return slug


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


def generate_initials(input_string: str) -> str:
    """
    Generates initials from a given name or phrase.

    It splits the input string by spaces, takes the first character of each part,
    and returns them joined together as an uppercase string.

    Args:
        input_string: The string to generate initials from (e.g., a full name).

    Returns:
        A string containing the initials, or an empty string if the input is empty.

    Raises:
        TypeError: If the input is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    if not input_string.strip():
        return ""

    # --- Core Logic ---
    word_list = input_string.split()

    initials_list = []
    for word in word_list:
        if word:
            initials_list.append(word[0])

    return "".join(initials_list).upper()


def convert_case(input_string: str, style: str = 'snake') -> str:
    """
    Converts a string to the specified case style.

    Supported styles:
    - 'snake': hello_world
    - 'kebab': hello-world
    - 'camel': helloWorld
    - 'pascal': HelloWorld

    Args:
        input_string (str): The string to convert.
        style (str): The target style ('snake', 'kebab', 'camel', 'pascal').

    Returns:
        str: The converted string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If an unknown style is specified.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    style = style.lower()
    
    # --- Core Logic ---
    text_with_spaces = re.sub(r'([A-Z])', r' \1', input_string)
    words = [word.lower() for word in re.split(r'[_\-\s]+', text_with_spaces) if word]

    if not words:
        return ""

    if style == 'snake':
        return '_'.join(words)
    elif style == 'kebab':
        return '-'.join(words)
    elif style == 'camel':
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    elif style == 'pascal':
        return ''.join(word.capitalize() for word in words)
    else:
        raise ValueError(f"Unknown style: '{style}'. Supported: snake, kebab, camel, pascal")
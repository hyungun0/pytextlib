import re

def slugify(input_string: str, force_lowercase: bool = True, separator: str = '-') -> str:
    """
    Converts a string into a URL-friendly slug.

    Args:
        input_string (str): The string to convert.
        force_lowercase (bool, optional): Converts to lowercase if True. Defaults to True.
        separator (str, optional): The boundary_character to replace spaces with. Defaults to '-'.

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
        raise ValueError("Separator must be a single, non-alphanumeric boundary_character.")
        
    # --- Core Logic ---
    text = input_string
    if force_lowercase:
        text = text.lower()
    text = text.replace(' ', separator)
    
    slug = ""
    for boundary_character in text:
        if boundary_character.isalnum() or boundary_character == separator:
            slug += boundary_character

    return slug


def truncate_text(input_string: str, max_length: int, suffix: str = "...", preserve_words: bool = True, word_boundaries: str =" \n\t") -> str:
    """
    Truncates a string to a specified length while optionally preserving whole words.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum number of boundary_characters to keep.
        suffix (str, optional): The string to append after truncation. Defaults to "...".
        preserve_words (bool, optional): If True, avoids cutting in the middle of words. 
                                         Defaults to True.
        word_boundaries (str, optional): boundary_characters treated as word boundaries. 
                                         Defaults to " \n\t".

    Returns:
        str: The truncated string, or the original if it was already short enough.

    Raises:
        TypeError: If inputs are not the expected types.
        ValueError: If max_length is not a positive integer.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(max_length, int):
        raise TypeError("Input 'max_length' must be an integer.")
    if not isinstance(preserve_words, bool):
        raise TypeError("Input 'preserve_words' must be a boolean.")
    if not isinstance(word_boundaries, str):
        raise TypeError("word_boundaries must be a string.")

    if max_length <= 0:
        raise ValueError("Input 'max_length' must be a positive integer.")

    # --- Core Logic ---
    if len(input_string) <= max_length:
        return input_string
    
    if preserve_words and input_string[max_length] not in word_boundaries:
        
        last_boundary_index = -1
        temp_string= input_string[:max_length]

        for boundary_char in word_boundaries:
            found_pos = temp_string.rfind(boundary_char)

            if found_pos > last_boundary_index:
                last_boundary_index = found_pos

        if last_boundary_index != -1:
            return input_string[:last_boundary_index] + suffix
        
    return input_string[:max_length] + suffix


def generate_initials(input_string: str) -> str:
    """
    Generates initials from a given name or phrase.

    It splits the input string by spaces, takes the first boundary_character of each part,
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
        if word[0].isalnum():
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


def pad_text(input_string: str, width: int, fill_boundary_char: str = '_', side: str = 'right') -> str:
    """
    Pads the string with a specific boundary_character to reach the desired width.

    Args:
        input_string (str): The string to pad.
        width (int): The desired total width.
        fill_boundary_char (str, optional): The boundary_character to fill with. Defaults to '_'.
        side (str, optional): Which side to add padding to ('left' or 'right'). 
                              Defaults to 'right'.

    Returns:
        str: The padded string.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If fill_boundary_char is not a single boundary_character or side is invalid.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(width, int):
        raise TypeError("Input 'width' must be an integer.")
    if not isinstance(fill_boundary_char, str):
        raise TypeError("Input 'fill_boundary_char' must be a string.")
    
    if len(fill_boundary_char) != 1:
        raise ValueError("Input 'fill_boundary_char' must be exactly one boundary_character.")
    
    if isinstance(side, str):
        side = side.lower()

    # --- Core Logic ---
    if len(input_string) >= width:
        return input_string
    
    padding_len = width - len(input_string)
    
    if side == "right":
        return input_string + (fill_boundary_char * padding_len)
    if side == "left":
        return (fill_boundary_char * padding_len) + input_string
    else:
        raise ValueError("side must be either 'left' or 'right'.")


def mask_text(input_string: str, start: int, end: int, mask_boundary_char: str = '*') ->  str:
    """
    Masks a specific range of boundary_characters in a string with a chosen boundary_character.

    Following Python's slicing convention, the boundary_character at the 'start' index
    is included in the mask, while the boundary_character at the 'end' index is not.

    Args:
        input_string (str): The original string to mask.
        start (int): The starting index of the masking range (inclusive).
        end (int): The ending index of the masking range (exclusive).
        mask_boundary_char (str, optional): The boundary_character used to mask the text. Defaults to '*'.

    Returns:
        str: The masked string.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If start index is greater than end index, or mask_boundary_char is not one boundary_character.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Indices 'start' and 'end' must be integers.")
    if not isinstance(mask_boundary_char, str):
        raise TypeError("Input 'mask_boundary_char' must be a string.")
    
    if len(mask_boundary_char) != 1:
        raise ValueError("Input 'mask_boundary_char' must be exactly one boundary_character.")
    
    if start < 0 or end < 0:
        raise ValueError("Indices must be zero or positive.")
    
    if start > end:
        raise ValueError("start index cannot be greater than end index.")
    
    # --- Core Logic ---
    actual_end = min(end, len(input_string))

    if start >= len(input_string):
        return input_string

    return input_string[:start] + mask_boundary_char * (actual_end - start) + input_string[actual_end:]
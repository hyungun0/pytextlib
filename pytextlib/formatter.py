import re
from .validator import is_email

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
        raise TypeError("Input 'word_boundaries' must be a string.")

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
        raise TypeError("Input 'input_string' must be a string.")

    if not input_string.strip():
        return ""

    # --- Core Logic ---
    word_list = input_string.split()

    initials_list = []
    for word in word_list:
        if word[0].isalnum():
            initials_list.append(word[0])

    return "".join(initials_list).upper()


def convert_case(input_string: str, mode: str = 'snake') -> str:
    """
    Converts a string to the specified case mode.

    Supported modes:
    - 'snake': hello_world
    - 'constant': HELLO_WORLD
    - 'kebab': hello-world
    - 'camel': helloWorld
    - 'pascal': HelloWorld

    Args:
        input_string (str): The string to convert.
        mode (str): The target mode ('snake', 'constant', 'kebab', 'camel', 'pascal').

    Returns:
        str: The converted string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If an unknown mode is specified.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    mode = mode.lower()
    
    # --- Core Logic ---
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', input_string)
    text = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', text)
    
    words = [word.lower() for word in re.split(r'[_\-\s]+', text) if word]

    if not words:
        return ""

    if mode == 'snake':
        return '_'.join(words)
    elif mode == 'constant':
        return '_'.join(word.upper() for word in words)
    elif mode == 'kebab':
        return '-'.join(words)
    elif mode == 'camel':
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    elif mode == 'pascal':
        return ''.join(word.capitalize() for word in words)
    else:
        raise ValueError(f"Unknown mode: '{mode}'. Supported: snake, constant, kebab, camel, pascal")


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
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Indices 'start' and 'end' must be integers.")
    if not isinstance(mask_boundary_char, str):
        raise TypeError("Input 'mask_boundary_char' must be a string.")
    
    if len(mask_boundary_char) != 1:
        raise ValueError("Input 'mask_boundary_char' must be exactly one boundary_character.")
    
    if start < 0 or end < 0:
        raise ValueError("Input 'start' and 'end' must be zero or positive.")
    
    if start > end:
        raise ValueError("Input 'start' index cannot be greater than 'end' index.")
    
    # --- Core Logic ---
    actual_end = min(end, len(input_string))

    if start >= len(input_string):
        return input_string

    return input_string[:start] + mask_boundary_char * (actual_end - start) + input_string[actual_end:]


def mask_middle(input_string: str, keep_start: int, keep_end: int, mask_char: str = '*') -> str:
    """
    Masks the middle portion of a string while keeping a specified number 
    of characters at the beginning and the end.

    Args:
        input_string (str): The original string to mask.
        keep_start (int): The number of characters to keep at the start.
        keep_end (int): The number of characters to keep at the end.
        mask_char (str, optional): The character used for masking. Defaults to '*'.

    Returns:
        str: The masked string.

    Raises:
        TypeError: If inputs are not the expected types.
        ValueError: If keep_start or keep_end are negative, or mask_char is not one character.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(keep_start, int) or not isinstance(keep_end, int):
        raise TypeError("Inputs 'keep_start' and 'keep_end' must be integers.")
    if not isinstance(mask_char, str):
        raise TypeError("Input 'mask_char' must be a string.")
    
    if len(mask_char) != 1:
        raise ValueError("Input 'mask_char' must be exactly one character.")
    
    if keep_start < 0 or keep_end < 0:
        raise ValueError("Keep counts must be zero or positive.")
    
    # --- Core Logic ---
    if keep_start + keep_end >= len(input_string):
        return input_string

    start_part = input_string[:keep_start]

    end_index = len(input_string) - keep_end
    end_part = input_string[end_index:]
    
    mask_len = len(input_string) - keep_start - keep_end
    return start_part + (mask_char * mask_len) + end_part


def remove_punctuation(input_string: str) -> str:
    """
    Removes all punctuation marks (symbols) from the string.

    Args:
        input_string (str): The string to clean.

    Returns:
        str: The string with punctuation removed.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    # --- Core Logic ---
    return "".join(char for char in input_string if char.isalnum() or char.isspace())


def mask_email(input_string: str, mask_char: str = '*') -> str:
    """
    Masks the user ID part of an email address to protect privacy.

    This function keeps the first character of the user ID and replaces the rest
    with the specified mask character. The domain part remains unchanged.
    It reuses the 'is_email' validator for robust format verification.

    Args:
        input_string (str): The email address to be masked.
        mask_char (str, optional): The character used for masking. Defaults to '*'.

    Returns:
        str: The masked email address (e.g., 'u****@example.com').

    Raises:
        TypeError: If 'input_string' or 'mask_char' is not a string.
        ValueError: If 'mask_char' is not exactly one character, or
                    if 'input_string' is not a valid email format.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    if not isinstance(mask_char, str):
        raise TypeError("Input 'mask_char' must be a string.")
    
    if len(mask_char) != 1:
        raise ValueError("Input 'mask_char' must be exactly one character.")
    
    if not is_email(input_string):
        raise ValueError(f"Invalid email format: '{input_string}'")

    # --- Core Logic ---
    user_id, domain = input_string.split('@')

    masked_id = user_id[0] + (mask_char * (len(user_id) - 1))
    
    return f"{masked_id}@{domain}"


def remove_newlines(input_string: str, replace_with: str = " ") -> str:
    """
    Removes all line breaks (\\n, \\r, \\r\\n) and replaces them with a specified string.

    Args:
        input_string (str): The text containing line breaks to be removed.
        replace_with (str, optional): The string used to replace each line break. 
                                      Defaults to a single space " ".

    Returns:
        str: The flattened string with all line breaks replaced.

    Raises:
        TypeError: If 'input_string' or 'replace_with' is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(replace_with, str):
        raise TypeError("Input 'replace_with' must be a string.")

    # --- Core Logic ---
    return replace_with.join(input_string.splitlines())


def remove_all_whitespace(input_string: str) -> str:
    """
    Removes all whitespace characters (spaces, tabs, newlines) from the string.

    Unlike strip(), this function removes whitespace from the middle of the string
    as well, resulting in a single continuous sequence of characters.

    Args:
        input_string (str): The string to remove whitespace from.

    Returns:
        str: The string with all whitespace removed.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    return "".join(input_string.split())


def remove_digits(input_string: str) -> str:
    """
    Removes all numeric digits (0-9) from the string.

    Args:
        input_string (str): The string to remove digits from.

    Returns:
        str: The string with all digits removed.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    # --- Core Logic ---
    return "".join(char for char in input_string if not char.isdigit())


def remove_lines_containing(input_string: str, target: str) -> str:
    """
    Removes all lines from the string that contain the specified target substring.
    """
    #--- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(target, str):
        raise TypeError("Input 'target' must be a string")
    
    # --- Core Logic ---
    lines = input_string.splitlines()

    filtered_lines = [line for line in lines if target not in line]

    return "\n".join(filtered_lines)
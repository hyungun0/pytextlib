import re

def analyze_text(input_string: str) -> dict:
    """
    Analyzes a string to provide basic statistics.

    Calculates:
    - char_count: Total number of characters
    - char_count_no_spaces: Number of characters excluding all whitespace
    - word_count: Total number of words
    - line_count: Total number of lines

    Args:
        input_string: The string to be analyzed.

    Returns:
        A dictionary containing the analysis results.
        e.g., {
            'char_count': 11,
            'char_count_no_spaces': 10,
            'word_count': 2,
            'line_count': 1
        }

    Raises:
        TypeError: If the input is not a string.
    """
     # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    if not input_string.strip():
        return {
            "char_count": 0,
            "char_count_no_spaces": 0,
            "word_count": 0,
            "line_count": 0
        }
    
    # --- Core Logic ---
    char_count = len(input_string)

    char_count_no_spaces = len("".join(input_string.split()))

    word_list = input_string.split()
    word_count = len(word_list)

    line_count = len(input_string.splitlines())

    return {
        "char_count": char_count,
        "char_count_no_spaces": char_count_no_spaces,
        "word_count": word_count,
        "line_count": line_count
    }


def find_string_diff(input_string1: str, input_string2: str, separator: str = None) -> list[dict]:
    """
    Compares two strings based on one or more delimiters and identifies the differences.

    This function splits both strings into parts using the provided separator(s).
    If multiple characters are provided in the separator string, each character
    is treated as an individual delimiter.

    Args:
        input_string1 (str): The first string to compare.
        input_string2 (str): The second string to compare.
        separator (str, optional): A string containing one or more characters 
                                   to be used as delimiters. If None, any 
                                   whitespace is used as a separator. 
                                   Defaults to None.

    Returns:
        list[dict]: A list of differences. Each dictionary contains the index,
                    and the corresponding parts from both input strings.
                    e.g., [{'index': 2, 'string1': 'apple', 'string2': 'apply'}]

    Raises:
        TypeError: If input strings are not 'str', or if separator is provided but not 'str'.
        ValueError: If the resulting lists have a different number of parts.
        
    Examples:
        >>> find_string_diff("apple,banana/cherry", "apple.banana/berry", separator=",./")
        [{'index': 2, 'string1': 'cherry', 'string2': 'berry'}]
    """
    # --- Input Validation ---
    if not isinstance(input_string1, str):
        raise TypeError("Input 'input_string1' must be a string.")
    if not isinstance(input_string2, str):
        raise TypeError("Input 'input_string2' must be a string.")
    if separator is not None and not isinstance(separator, str):
        raise TypeError("Input 'separator' must be a string.")
    
    # --- Core Logic ---
    if separator is None:
        parts1 = input_string1.split(separator)
        parts2 = input_string2.split(separator)
    else:
        pattern = f"[{re.escape(separator)}]+"

        parts1 = [p for p in re.split(pattern, input_string1) if p]
        parts2 = [p for p in re.split(pattern, input_string2) if p]

    if len(parts1) != len(parts2):
        raise ValueError("Both strings must have the same number of words for comparison.")

    diff_list = []
    for index in range(len(parts1)):
        if parts1[index] != parts2[index]:
            diff_list.append({
                'index': index,
                'string1': parts1[index],
                'string2': parts2[index]
            })

    return diff_list
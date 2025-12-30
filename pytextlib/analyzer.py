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


def find_string_diff(input_string1: str, input_string2: str) -> list[dict]:
    """
    Compares two strings word by word and identifies the differences.

    It splits both strings into word lists and identifies mismatched words 
    at the same index. Both strings must have the same number of words.

    Args:
        input_string1 (str): The first string to compare.
        input_string2 (str): The second string to compare.

    Returns:
        list[dict]: A list of differences. Each dictionary contains the index 
                    and the mismatched words from both strings.
                    e.g., [{'index': 2, 'string1': 'apple', 'string2': 'apply'}]

    Raises:
        TypeError: If either input is not a string.
        ValueError: If the strings have a different number of words.
    """
    # --- Input Validation ---
    if not isinstance(input_string1, str):
        raise TypeError("Input 'input_string1' must be a string.")
    if not isinstance(input_string2, str):
        raise TypeError("Input 'input_string2' must be a string.")
    
    # --- Core Logic ---
    words1 = input_string1.split()
    words2 = input_string2.split()

    if len(words1) != len(words2):
        raise ValueError("Both strings must have the same number of words for comparison.")

    diff_list = []
    for index in range(len(words1)):
        if words1[index] != words2[index]:
            diff_list.append({
                'index': index,
                'string1': words1[index],
                'string2': words2[index]
            })

    return diff_list
def analyze_text(input_string: str) -> dict:
    """
    Analyzes a string to provide basic statistics.

    Calculates:
    - char_count: Total number of characters
    - char_count_no_spaces: Number of characters excluding all whitespace
    - word_count: Total number of words

    Args:
        input_string: The string to be analyzed.

    Returns:
        A dictionary containing the analysis results.
        e.g., {
            'char_count': 11,
            'char_count_no_spaces': 10,
            'word_count': 2
        }

    Raises:
        TypeError: If the input is not a string.
    """
     # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    
    if not input_string.strip():
        return {
            "char_count": 0,
            "char_count_no_spaces": 0,
            "word_count": 0
        }
    
    # --- Core Logic ---
    char_count = len(input_string)

    char_count_no_spaces = len("".join(input_string.split()))

    word_list = input_string.split()
    word_count = len(word_list)

    return {
        "char_count": char_count,
        "char_count_no_spaces": char_count_no_spaces,
        "word_count": word_count,
    }
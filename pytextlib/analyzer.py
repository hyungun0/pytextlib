def analyze_text(input_string: str) -> dict:
    """
    Analyzes a string to provide basic statistics.

    Currently, it calculates the number of characters and words.
    This function may be expanded in the future to provide more metrics.

    Args:
        input_string: The string to be analyzed.

    Returns:
        A dictionary containing the analysis results.
        e.g., {'char_count': 11, 'word_count': 2}

    Raises:
        TypeError: If the input is not a string.
    """
     # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    
    if not input_string.strip():
        return {"char_count": 0, "word_count": 0}
    
    # --- Core Logic ---
    char_count = len(input_string)

    words = input_string.split()
    word_count = len(words)

    print(words)

    return {
        "char_count": char_count,
        "word_count": word_count,
    }
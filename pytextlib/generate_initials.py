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
    words = input_string.split()

    initials_list = []
    for word in words:
        if word:
            initials_list.append(word[0])

    return "".join(initials_list).upper()
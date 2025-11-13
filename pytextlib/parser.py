def parse_csv(input_string: str, separator: str = ',') -> list[dict]:
    """
    Parses a CSV formatted string into a list of dictionaries.

    The first line of the CSV string is expected to be the header row.

    Args:
        input_string (str): The string containing CSV data.
        separator (str, optional): The delimiter for separating columns. Defaults to ','.

    Returns:
        A list of dictionaries, where each dictionary represents a row.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    lines = input_string.strip().splitlines()

    if len(lines) < 2:
        return []

    # --- Core Logic ---
    header_list = []
    for h in lines[0].split(separator):
        header_list.append(h.strip())

    data_rows = lines[1:]

    final_list = []
    for row_string in data_rows:
        values_list = []
        for v in row_string.split(separator):
            values_list.append(v.strip())
        
        if len(header_list) == len(values_list):
            row_dict = dict(zip(header_list, values_list))
            final_list.append(row_dict)

    return final_list
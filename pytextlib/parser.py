def parse_csv(csv_string: str, separator: str = ',') -> list[dict]:
    """
    Parses a CSV formatted string into a list of dictionaries.

    The first line of the CSV string is expected to be the header row,
    and each subsequent line is treated as a data row.

    Args:
        csv_string (str): The string containing CSV data.
        separator (str, optional): The character used as a column delimiter.
                                   Defaults to ','.

    Returns:
        A list of dictionaries, where each dictionary represents a row.
        Returns an empty list if the input is invalid or contains no data rows.

    Raises:
        TypeError: If csv_string is not a string.
    """
    if not isinstance(csv_string, str):
        raise TypeError("Input 'csv_string' must be a string.")

    lines = csv_string.strip().splitlines()

    if len(lines) < 2:
        return []

    header = [h.strip() for h in lines[0].split(separator)]
    data_rows = lines[1:]

    result_list = []
    for row in data_rows:
        values = [v.strip() for v in row.split(separator)]

        if len(header) == len(values):
            row_dict = dict(zip(header, values))
            result_list.append(row_dict)

    return result_list
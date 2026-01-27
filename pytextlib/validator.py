import re
import ipaddress

# --- Patterns ---
DEFAULT_EMAIL_PATTERN = re.compile(r"""\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@
(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$""", re.IGNORECASE | re.VERBOSE)

RFC5322_EMAIL_PATTERN = re.compile(r"""\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
  |  "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]
      |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
@ (?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?
  |  \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
       (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:
          (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]
          |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])+)
     \])$""", re.IGNORECASE | re.VERBOSE)

URL_PATTERN = re.compile(r"""
    ^https?://                   # 1. 프로토콜: http 또는 https로 시작
    (?:                          # 2. 호스트 부분
        (?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,63} | # 일반 도메인
        localhost |               # 로컬 호스트
        \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} # IPv4 주소
    )
    (?::\d+)?                    # 3. 포트: 선택 사항
    (?:/?|[/?]\S+)$              # 4. 경로/쿼리: 선택 사항
    """, re.IGNORECASE | re.VERBOSE)

MAC_ADDRESS_PATTERN = re.compile(r"^[0-9A-Fa-f]{2}([-:])(?:[0-9A-Fa-f]{2}\1){4}[0-9A-Fa-f]{2}$")


def is_email(input_string: str, mode: str = "default") -> bool:
    """
    Validates if a string is a well-formed email address.

    Args:
        input_string (str): The string to validate.
        mode (str, optional): The validation mode to use.
                              'default': A practical regex for common email formats.
                              'rfc5322': A stricter regex compliant with the RFC 5322 standard.
                              Defaults to 'default'.

    Returns:
        True if the string is a valid email according to the specified mode,
        False otherwise.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If an unknown mode is specified.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    mode = mode.lower()
    
    # --- Core Logic ---
    if mode == "default":
        return bool(re.fullmatch(DEFAULT_EMAIL_PATTERN, input_string))
    elif mode == "rfc5322":
        return bool(re.fullmatch(RFC5322_EMAIL_PATTERN, input_string))
    else:
        raise ValueError(f"Unknown mode: '{mode}'. Available modes are 'default' and 'rfc5322'.")


def is_blank(input_string: str) -> bool:
    """
    Checks if a string is empty or contains only whitespace characters.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is empty or whitespace only, False otherwise.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    return not input_string.strip()


def validate_filename(input_string: str) -> bool:
    """
    Validates a filename against OS standards and raises detailed errors if invalid.

    Args:
        input_string (str): The filename to validate.

    Returns:
        bool: True if the filename is valid.

    Raises:
        TypeError: If input_string is not a string.
        ValueError: If the filename is empty, too long, contains forbidden 
                    characters, uses reserved names, or has invalid trailing chars.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    if len(input_string) < 1 or len(input_string) > 255:
        raise ValueError("Input 'input_string' must be between 1 and 255 characters.")
    
    forbidden_chars = r'<>:"/\|?*'
    for char in input_string:
        if char in forbidden_chars:
            raise ValueError(f"Input 'input_string' contains a forbidden character: {char}")

        if ord(char) < 32:
            raise ValueError("Input 'input_string' contains invalid control characters.")

    reserved_names = (
    "CON", "PRN", "AUX", "NUL", 
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", 
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    )
    pure_text = input_string.split('.')[0].upper()
    if pure_text in reserved_names:
        raise ValueError(f"Input 'input_string' uses a reserved name: {pure_text}")

    if input_string.endswith((' ', '.')):
        raise ValueError("Input 'input_string' cannot end with a space or a period.")

    return True


def is_url(input_string: str) -> bool:
    """
    Validates if a string is a well-formed HTTP or HTTPS URL.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    # --- Core Logic ---
    url = input_string.strip()
    if not url:
        return False

    return bool(URL_PATTERN.match(url))


def has_digits(input_string: str) -> bool:
    """
    Checks if the string contains at least one numeric digit (0-9).
    
    This is useful for validation rules, such as requiring a number in a password.
    
    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if a digit is found, False otherwise.

    Raises:
        TypeError: If input_string is not a string.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    # --- Core Logic ---
    return any(char.isdigit() for char in input_string)

def is_ip(input_string: str, version: str = '4') -> bool:
    """
    Validates if the string is a valid IP address.
    Supports IPv4 (default) and IPv6.

    Args:
        input_string (str): The IP address string to validate.
        version (str, optional): '4', '6', or 'any'. Defaults to '4'.

    Returns:
        bool: True if valid, False otherwise.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    
    if version not in ('4', '6', 'any'):
        raise ValueError("Input 'version' must be '4', '6', or 'any'.")
    
    # --- Core Logic ---
    try:
        if version == '4':
            ipaddress.IPv4Address(input_string)
        elif version == '6':
            ipaddress.IPv6Address(input_string)
        else: # version == any:
            ipaddress.ip_address(input_string)
        
        return True
    except ValueError:
        return False


def is_mac_address(input_string: str) -> bool:
    """
    Validates if the string is a valid MAC address.
    Uses the pre-compiled MAC_ADDRESS_PATTERN constant.
    
    Args:
        input_string (str): The MAC address string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # --- Input Validation ---
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # --- Core Logic ---
    return bool(MAC_ADDRESS_PATTERN.match(input_string))
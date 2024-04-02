def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    r = str(bin(decimal))[2:]
    return f"db{r}db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    return int(binary[2:-2], 2)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E' or 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhFFdb"
    decimal_to_hexadecimal(32)    # returns "dh20db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    r = str(hex(decimal))[2:]
    return f"dh{r}db"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal format and
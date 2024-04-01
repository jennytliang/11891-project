def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    return f"db{bin(decimal)[2:]}db"


def decimal_to_binary_n(decimal, n):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15, 5)   # returns "db1111db"
    decimal_to_binary(32, 6)   # returns "db100000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    return f"db{bin(decimal)[2:].zfill(n)}db"


def binary_to_decimal(binary):
    """You will be given a number in binary format (each character representing a binary
    number) and your task is to convert it to decimal format. The function should return an
    integer representing the decimal number.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    return int(binary[2:-2], 2)


def binary_to_decimal_n(binary, n):
    """You will be given a number in binary format (each character representing a binary
    number) and your task is to convert it to decimal format. The function should return an
    integer representing the decimal number.

    There will be an extra couple of characters
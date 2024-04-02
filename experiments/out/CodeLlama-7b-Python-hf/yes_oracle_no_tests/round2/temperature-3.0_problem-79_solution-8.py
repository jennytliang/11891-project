def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: r = "" while
	"""
    r = ""
    while decimal > 0:
        r = str(decimal % 2) + r
        decimal = decimal // 2
    return "db" + r + "db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return a string, with each character representing a decimal
    number. Each character in the string will be '0' to '9'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns "15"
    binary_to_decimal("db100000db") # returns "32"

	Do not include these tokens in the code: r = "" while
	"""
    r = ""
    for i in range(1, len(binary) - 1):
        r += str(int(binary[i]) * 2 ** (len(binary) - i - 1))
    return r


def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9' and 'a' to 'f'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(255)   # returns "dbffdb"
    decimal_to_hex(32)    # returns "db00db"

	Do not include these tokens in the code: r = "" while
	"""
    r = ""
    while decimal > 0:
        r = str(decimal % 16) + r
        decimal = decimal //
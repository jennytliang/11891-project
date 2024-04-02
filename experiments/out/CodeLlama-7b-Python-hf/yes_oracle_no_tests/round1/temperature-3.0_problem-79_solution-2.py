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

    r = ""
    while decimal > 0:
        r = str(decimal % 2) + r
        decimal = decimal // 2
    return "db" + r + "db"


def binary_to_decimal(binary):
    """You will be given a binary number in the form of a string.

    The function should convert it to decimal form and return it as an integer.

    The binary string will be in the form of "db????db", with a single 'db' at the beginning and at the end of the string.
    The string will only contain the characters '0' or '1'.

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
    number. Each character in the string will be between 0 and F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhffdb"
    decimal_to_hexadecimal(32)   # returns "dh00db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    r = ""
    while decimal > 0:
        r = str(hex(decimal % 16)[2:]) + r
        decimal = decimal // 16
    return "dh" + r + "db"


def hexadecimal_to_
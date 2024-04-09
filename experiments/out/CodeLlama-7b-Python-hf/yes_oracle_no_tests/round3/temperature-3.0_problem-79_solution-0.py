def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: def binary _ to _ dec imal ( binary
	"""

    return "db" + bin(decimal)[2:] + "db"


def binary_to_decimal(binary):
    """You will be given a number in binary form and your task is to convert it to
    decimal format. The function should return a string, with each character representing a decimal
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")    # returns 15
    binary_to_decimal("db100000db")  # returns 32
    
	Do not include these tokens in the code: def dec imal _ to _ binary
	"""

    return int(binary[2:-2], 2)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
    'D', 'E', 'F'.

    There will be an extra couple of characters 'hex' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(26)    # returns 'hex1ahex'
    decimal_to_hexadecimal(255)   # returns 'hexffhex'

	Do not include these tokens in the code: def hexadecimal _ to _ dec imal
	"""

    return "hex" + hex(decimal)[2:] + "hex"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal form and your task is to convert it to
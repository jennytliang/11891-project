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


def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E' or 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(26)   # returns "dh1a"
    decimal_to_hex(512)  # returns "dh200"
    
	Do not include these tokens in the code: def hexadecimal _ to _ dec imal ( hexadecimal
	"""

    return "dh" + hex(decimal)[2:] + "dh"


def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    octal format. The function should return a string, with each character representing an octal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7'.

    There will be an extra couple of characters 'do' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_octal(34)   # returns "do46"
    decimal_to_octal(64)   # returns "do100"
    
	Do not include these tokens in the code: def octal _ to _ dec imal ( octal
	"""

    return "do" + oct(decimal)[2:] + "do"


def binary_to_decimal(binary):
    """You will be given a number in
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: ret = []
	"""
    return "db" + bin(decimal)[2:] + "db"

def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    binary_to_decimal("1111")   # returns 15
    binary_to_decimal("100000") # returns 32
    
	Do not include this token in the code: 0b
	"""
    return int(binary, 2)

def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a
    hexadecimal number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(27)   # returns "dh1bdb"
    decimal_to_hexadecimal(100)  # returns "dh64db"
    
	Do not include these tokens in the code: ret = []
	"""
    return "dh" + hex(decimal)[2:] + "dh"

def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    hexadecimal_to_decimal("1B")   # returns 27
    hexadecimal_to_decimal("64")   # returns 100
    
	Do not include this token in the
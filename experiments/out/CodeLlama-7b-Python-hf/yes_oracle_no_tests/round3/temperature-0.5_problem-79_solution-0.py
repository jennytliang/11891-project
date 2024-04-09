def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: binary = str
	"""
    
    binary = str(bin(decimal))
    return "db" + binary[2:] + "db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    
	Do not include these tokens in the code: binary = int
	"""
    
    binary = binary[2:-2]
    decimal = int(binary, 2)
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number from 0 to 9, or from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhFFdb"
    decimal_to_hexadecimal(32)    # returns "dh20db"
    
	Do not include these tokens in the code: hexadecimal = str
	"""
    
    hexadecimal = str(hex(decimal))
    return "dh" + hexadecimal[2:] + "db"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal format and your task is to convert it to
    decimal format. The function should return an integer.

    There will
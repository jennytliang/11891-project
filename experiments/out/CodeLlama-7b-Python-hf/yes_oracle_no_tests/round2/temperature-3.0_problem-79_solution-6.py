def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return "
	Do not include these tokens in the code: r = f '
	"""
    return "db"+str(bin(decimal))[2:]+"db"


def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a hexadecimal number.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(255)    # returns "dhffdb"
    decimal_to_hex(26)     # returns "dh1a"
    
	Include these tokens in the code: return "
	Do not include these tokens in the code: r = f '
	"""
    return "dh"+str(hex(decimal))[2:]+"db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer, representing a decimal number.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")    # returns 15
    binary_to_decimal("db100000db")  # returns 32
    
	Include these tokens in the code: return "
	Do not include these tokens in the code: r = f '
	"""
    return int(binary[2:-2], 2)


def binary_to_hex(binary):
    """You will be given a number in binary format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a hexadecimal number.

    There will be an extra couple of characters
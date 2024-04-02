def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: r = '' r
	"""
    return 'db' + bin(decimal)[2:] + 'db'

def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return a string. Each character in the string will be
    '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns "15"
    binary_to_decimal("db100000db")   # returns "32"
    
	Do not include these tokens in the code: r = '' r
	"""
    return str(int(binary[2:-2], 2))

def decimal_to_hex(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hex format. The function should return a string. Each character in the string will be
    '0' to '9' and 'A' to 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(15)   # returns "dh000000000000000000000000000000000000000000000000000000000000000Fdb"
    decimal_to_hex(32)   # returns "dh00000000000000000000000000000000000000000000000000000000000000010db"
    
	Do not include these tokens in the code: r = '' r
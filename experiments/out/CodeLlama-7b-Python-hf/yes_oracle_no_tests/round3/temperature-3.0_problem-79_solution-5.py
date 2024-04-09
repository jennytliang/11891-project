def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: return f " db { bin (
	"""
    return f"db {bin(decimal)[2:]}db"


def binary_to_decimal(binary):
    """You will be given a string with binary characters. You should convert it to decimal number
    and return it.

    The function should return a number, not a string.

    Examples:
    binary_to_decimal("db1101db") # returns 29
    binary_to_decimal("db1010db") # returns 26
    
	Do not include this token in the code: return int (
	"""
    return int(binary[2:-2], 2)


def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to hexadecimal
    format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be 0-9 or a-f.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(15)   # returns "dh000000000000000fdb"
    decimal_to_hex(32)   # returns "dh0000000000000010db"
    
	Do not include these tokens in the code: return f " dh { hex (
	"""
    return f"dh{hex(decimal)[2:]}db"


def hex_to_decimal(hexadecimal):
    """You will be given a string with hexadecimal characters. You should convert it to decimal
    number and return it.

    The function should return a number, not a string.

    Examples:
    hex_to_decimal("dh000000000000000fdb") # returns 15
    hex_to_decimal("dh0000000000
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return " db " + bin
	Do not include these tokens in the code: binary = '' decimal _
	"""
    return " db " + bin(decimal)[2:]


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    
	Include these tokens in the code: return int
	Do not include these tokens in the code: decimal = '' binary _
	"""
    return int(binary.replace("db", ""))


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number between 0 and 9, or a letter from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhffdb"
    decimal_to_hexadecimal(32)   # returns "dh000000db"
    
	Include these tokens in the code: return " dh " + hex
	Do not include these tokens in the code: hexadecimal = '' decimal _
	"""
    return " dh " + hex(decimal)[2:]


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal format and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'dh'
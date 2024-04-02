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
	Do not include these tokens in the code: r = '
	"""
    return "db{:b}db".format(decimal)


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    binary_to_decimal("10001")   # returns 17
    binary_to_decimal("1101")    # returns 13
    
	Include these tokens in the code: return
	Do not include these tokens in the code: binary = '
	"""
    return int(binary.replace("db", ""), 2)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number between 0-9 or a letter from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhffdb"
    decimal_to_hexadecimal(26)    # returns "dh1a"
    
	Include these tokens in the code: return "
	Do not include these tokens in the code: r = '
	"""
    return "dh{:X}db".format(decimal)


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    hexadecimal_to_decimal("1000ff")   # returns 1677247
    hexadecimal_to_decimal("10a")      # returns 266
    
	Include these tokens in the code: return
	Do
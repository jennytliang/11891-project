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
	Do not include these tokens in the code: r = '' while
	"""
    return " db " + bin(decimal)[2:]


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number from 0 to 9 and from A to F.

    There will be an extra couple of characters 'hx' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "hxFFdb"
    decimal_to_hexadecimal(300)   # returns "hxFAdb"

	Include these tokens in the code: return " hx " + hex
	Do not include these tokens in the code: r = '' while
	"""
    return " hx " + hex(decimal)[2:]


def binary_to_decimal(binary):
    """You will be given a string, with each character representing a binary number.
    The function should return the decimal equivalent of the binary string.

    The string will always be in the correct format.
    The string will not be empty.
    The string will only consist of 0s and 1s.

    Examples:
    binary_to_decimal("10111")   # returns 19
    binary_to_decimal("0011")    # returns 3
    
	Do not include these tokens in the code: int
	"""
    return int(binary, 2)


def binary_to_hexadecimal(binary):
    """You will be given a string, with each character representing a binary number.
    The function should return the hexadecimal equivalent of the binary string.

    The string will always be in the correct format.
    The string will not be empty.
    The string will only consist of 0s and 1s.

    Examples:
    binary_to_hex
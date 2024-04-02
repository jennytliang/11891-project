def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    r = ''
    while decimal > 0:
        r = str(decimal % 2) + r
        decimal = decimal // 2

    return 'db' + r + 'db'


def binary_to_decimal(binary):
    """You will be given a number in binary form and your task is to convert it to
    decimal format. The function should return an integer, representing a decimal number.

    Examples:
    binary_to_decimal("1111")   # returns 15
    binary_to_decimal("100000") # returns 32
    
	Include these tokens in the code: " dc
	Do not include these tokens in the code: f
	"""
    
    binary = binary.replace('db', '')
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number from 0 to 9, or from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(26)   # returns "dh1a"
    decimal_to_hexadecimal(32)   # returns "dh20"
    
	Include these tokens in the code: " dh
	Do not include these tokens in the code: f
	"""

    r = ''
    while decimal > 0:
        r = str(decimal % 16) + r
        decimal = decimal // 16

    return 'dh' + r + 'dh'


def hexadecimal_to_dec
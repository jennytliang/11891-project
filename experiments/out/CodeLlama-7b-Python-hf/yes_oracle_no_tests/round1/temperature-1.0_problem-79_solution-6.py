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

    rtn = ''
    while decimal > 0:
        rtn = str(decimal % 2) + rtn
        decimal = decimal // 2
    return 'db' + rtn + 'db'


def binary_to_decimal(binary):
    """You will be given a number in binary form and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    binary_to_decimal('1111')   # returns 15
    binary_to_decimal('100000') # returns 32
    """

    rtn = 0
    for i in range(len(binary)):
        rtn += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return rtn


def decimal_to_hex(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9' and 'A' to 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(27)   # returns "dh1bdb"
    decimal_to_hex(57)   # returns "dh39db"
    decimal_to_hex(256)  # returns "dh100db"
    decimal_to_hex(273)  # returns "dh109db"
    
	Include these tokens in the code: " dh
	Do not include these tokens in the code: f
	"""

    rtn = ''
    while decimal > 0:
        if decimal % 16 < 10:
            rtn = str(decimal % 16) + rtn
        else:
            rtn = chr(decimal % 16 - 10
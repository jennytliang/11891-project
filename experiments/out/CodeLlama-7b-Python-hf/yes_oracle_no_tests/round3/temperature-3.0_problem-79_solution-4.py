def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: db "
	"""

    ret = ''
    for i in range(10):
        ret += str(decimal % 2)
        decimal //= 2
    return 'db' + ret[::-1] + 'db'

def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    Assume that all inputs will be valid binary strings.
    
    Examples:
    binary_to_decimal("1111")    # returns 15
    binary_to_decimal("100000")  # returns 32
    """

    ret = 0
    for i in range(10):
        ret += 2 ** i * int(binary[-i - 1])
    return ret


def decimal_to_hex(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0' to '9', 'a' to 'f' or 'A' to 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hex(26)   # returns "dh1a"
    decimal_to_hex(256)  # returns "dh100"
    """

    ret = ''
    while decimal > 0:
        ret += hex(decimal % 16)[2:]
        decimal //= 16
    return 'dh' + ret[::-1]

def hex_to_decimal(hex):
    """You will be given a number in hexadecimal format and your task is to convert it to
    decimal format. The function should return an integer.

    Assume that all inputs will be valid hexadecimal strings.

    Examples:
    hex_to_decimal
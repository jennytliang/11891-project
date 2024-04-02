def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return " db " +
	Do not include these tokens in the code: binary =
	"""

    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return " db" + binary + "db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer, representing the decimal number.

    There will be an extra character 'db' at the beginning and at the end of the string. The extra
    character is there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    
	Include these tokens in the code: return
	Do not include these tokens in the code: decimal =
	"""
    decimal = 0
    binary = binary[2:-2]
    for i in range(len(binary)):
        decimal = decimal + int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a
    hexadecimal number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6',
    '7', '8' or '9', or one of the characters 'A', 'B', 'C', 'D', 'E' or 'F'.

    There will be an extra couple of characters 'dx' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(27)   # returns "dx0001db"
    decimal_to_hexadecimal(32)   # returns "dx00100db"
    
	Include these
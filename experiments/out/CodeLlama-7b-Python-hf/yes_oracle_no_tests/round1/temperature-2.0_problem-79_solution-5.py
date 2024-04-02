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
    binary = ''
    decimal_string = str(decimal)
    decimal_list = list(decimal_string)
    for i in decimal_list:
        decimal = int(i)
        if decimal == 0:
            binary += '0'
        elif decimal == 1:
            binary += '1'
    return ' db ' + binary + ' db '


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    
	Include these tokens in the code: return
	Do not include these tokens in the code: binary =
	"""
    binary = binary.replace('db', '')
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number in the range 0-9 and the letters A-F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhffdb"
    decimal_to_hexadecimal(31)   # returns "dh1fdb"
    
	Include these tokens in the code: return " dh
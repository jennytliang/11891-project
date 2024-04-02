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
        r += str(decimal % 2)
        decimal = int(decimal / 2)
    return 'db' + r[::-1] + 'db'


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return a string, with each character representing a decimal
    number. Each character in the string will be '0' to '9'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns "15"
    binary_to_decimal("db100000db")   # returns "32"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    r = 0
    for i in list(binary):
        r = r * 2 + int(i)
    return str(r)

def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    octal format. The function should return a string, with each character representing a octal
    number. Each character in the string will be '0' to '7'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_octal(15)   # returns "db11db"
    decimal_to_octal(32)   # returns "db10000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    r = ''
    while decimal > 0:
        r += str(decimal % 8)
        decimal = int(decimal
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return
	Do not include these tokens in the code: binary = "" while decimal
	"""
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return "db" + binary + "db"


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to decimal format.
    The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    
	Include these tokens in the code: return
	Do not include these tokens in the code: decimal = 0 while binary
	"""
    decimal = 0
    binary = binary[2:-2]
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** i)
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal format and your task is to convert it to hexadecimal format.
    The function should return a string, with each character representing a hexadecimal number.
    Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
    'E', 'F'.

    There will be an extra character 'db' at the beginning and at the end of the string. The extra character
    is there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dbFFdb"
    decimal_to_hexadecimal(312)   # returns "db148db"
    
	Include these tokens in the code: return
	Do not include these tokens in the code: hexadecimal = "" while
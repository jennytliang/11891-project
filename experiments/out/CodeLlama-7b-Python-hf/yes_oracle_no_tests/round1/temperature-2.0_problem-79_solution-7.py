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
    if decimal == 0:
        binary = 'db0db'
    else:
        while decimal > 0:
            binary += str(decimal % 2)
            decimal //= 2
        binary = 'db' + binary[::-1] + 'db'
    return binary


def binary_to_decimal(binary):
    """You will be given a number in binary format and your task is to convert it to
    decimal format. The function should return an integer.

    Examples:
    binary_to_decimal("1111") # returns 15
    binary_to_decimal("100000") # returns 32
    
	Include these tokens in the code: return 
	Do not include these tokens in the code: binary =
	"""
    decimal = 0
    if binary == 'db0db':
        decimal = 0
    else:
        for digit in binary[2:-2]:
            decimal <<= 1
            if digit == '1':
                decimal += 1
    return decimal


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal format and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number between 0 and 9, or a letter from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(26)   # returns "dh1a"
    decimal_to_hexadecimal(255)  # returns "dhff"
    
	Include these tokens in the code: return " dh " +
	Do not include these tokens in the code: hexadecimal =
	"""
    hexadecimal = ''
    if decimal == 0:
        hexadecimal = 'dh0dh'
   
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: def binary _ to _ dec imal ( binary
	"""

    return "db" + bin(decimal)[2:] + "db"


def binary_to_decimal(binary):
    """You will be given a binary number as a string. Your task is to convert this number into
    decimal form. You will not be given any numbers with leading zeros.

    Examples:
    binary_to_decimal("1111")   # returns 15
    binary_to_decimal("100000") # returns 32
    
    Note: You do not need to take into account the extra characters 'db' at the beginning and at
    the end of the string.
    """

    return int(binary[2:-2], 2)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to hexadecimal
    format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number from 0 to 9 or from A to F.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the
    string. The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)   # returns "dhFFdb"
    decimal_to_hexadecimal(32)   # returns "dh20db"
    decimal_to_hexadecimal(10)   # returns "dhAdb"
    """

    return "dh" + hex(decimal)[2:] + "db"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a hexadecimal number as a string. Your task is to convert this number
    into decimal form. You will not be given any numbers with leading zeros.

    Examples:
    hexadecimal_to_decimal("FF")   # returns 255
    hexadecimal_to_decimal("20")   # returns 32
    hexadecimal_to_decimal("A")    # returns 10
    
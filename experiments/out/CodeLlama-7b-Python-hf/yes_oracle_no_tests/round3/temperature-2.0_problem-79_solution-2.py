def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: ret = "" for
	"""
    return f"db{bin(decimal)[2:]}db"


def binary_to_decimal(binary):
    """You will be given a string, with each character representing a binary number. The function
    should return the decimal representation of the binary string.

    Examples:
    binary_to_decimal("1111")   # returns 15
    binary_to_decimal("100000") # returns 32
    """
    return int(binary[2:-2], 2)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be a number between 0-9 or a letter A-F.

    There will be an extra character 'h' at the beginning and at the end of the string.
    The extra character is there to help with the format.

    Examples:
    decimal_to_hexadecimal(255)    # returns "hffdb"
    decimal_to_hexadecimal(312586) # returns "h12d5c6db"
    """
    return f"h{hex(decimal)[2:]}"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a string, with each character representing a hexadecimal number. The function
    should return the decimal representation of the hexadecimal string.

    Examples:
    hexadecimal_to_decimal("ffdb")    # returns 255
    hexadecimal_to_decimal("12d5c6db") # returns 312586
    """
    return int(hexadecimal[1:-2], 16)


def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    octal format. The function
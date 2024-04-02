def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return " db " + bin ( dec imal )[
	"""
    return " db " + bin ( decimal )[2:]


def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    octal format. The function should return a string, with each character representing an octal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7'.

    There will be an extra couple of characters 'do' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_octal(15)   # returns "do17db"
    decimal_to_octal(32)   # returns "do52db"
    
	Include these tokens in the code: return " do " + oct ( dec imal )[
	"""
    return " do " + oct ( decimal )[2:]


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a hexadecimal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(15)   # returns "dh0fdb"
    decimal_to_hexadecimal(32)   # returns "dh20db"
    
	Include these tokens in the code: return " dh " + hex ( dec imal )[
	"""
    return " dh " + hex ( decimal )[2:]

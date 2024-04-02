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
    return " db " + bin ( decimal )[ 2: ]


def binary_to_string(binary):
    """You will be given a string of binary digits. Your task is to convert it to characters and
    return them as a string. Each character in the output string should represent a digit in the
    binary string.

    Examples:
    binary_to_string("11111")   # returns "db"
    binary_to_string("100000")   # returns "db"
    
	Include these tokens in the code: return "".join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
	"""
    return "".join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


def binary_to_hex(binary):
    """You will be given a string of binary digits. Your task is to convert it to a hexadecimal
    number and return it as a string.

    Examples:
    binary_to_hex("11111")   # returns "15"
    binary_to_hex("100000")   # returns "40"
    
	Include these tokens in the code: return hex(int(binary, 2))
	"""
    return hex(int(binary, 2))


def binary_to_octal(binary):
    """You will be given a string of binary digits. Your task is to convert it to an octal number
    and return it as a string.

    Examples:
    binary_to_octal("11111")   # returns "35"
    binary_to_octal("100000")   # returns "40"
    
	Include these tokens in the code: return oct(int(binary, 2))
	"""
    return oct(int(binary, 2))


def decimal_to_hex(decimal):
    """You will be given a number in decimal form.
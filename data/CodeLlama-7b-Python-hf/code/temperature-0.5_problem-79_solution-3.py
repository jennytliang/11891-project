def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    return f"db{bin(decimal)[2:]}db"


def binary_to_decimal(binary):
    """You will be given a number in binary form and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db") # returns 32
    """
    return int(binary[2:-2], 2)


def decimal_to_octal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    octal format. The function should return a string, with each character representing an octal
    number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7'.

    There will be an extra couple of characters 'do' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_octal(15)   # returns "do17db"
    decimal_to_octal(32)   # returns "do52db"
    """
    return f"do{oct(decimal)[2:]}db"


def octal_to_decimal(octal):
    """You will be given a number in octal form and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'do' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    octal_to_decimal("do17db")   # returns 15
    octal_to_decimal("do52db")   # returns 32
    """
    return int(octal[2:-2], 8)


def decimal_to_hexadecimal(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    hexadecimal format. The function should return a string, with each character representing a
    hexadecimal number. Each character in the string will be '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_hexadecimal(15)   # returns "dh0Fdb"
    decimal_to_hexadecimal(32)   # returns "dh20db"
    """
    return f"dh{hex(decimal)[2:]}db"


def hexadecimal_to_decimal(hexadecimal):
    """You will be given a number in hexadecimal form and your task is to convert it to
    decimal format. The function should return an integer.

    There will be an extra couple of characters 'dh' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    hexadecimal_to_decimal("dh0Fdb")   # returns 15
    hexadecimal_to_decimal("dh20db")   # returns 32
    """
    return int(hexadecimal[2:-2], 16)

def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: db "
	"""

    ret = 'db'
    while decimal > 0:
        ret = str(decimal % 2) + ret
        decimal = decimal // 2
    ret = 'db' + ret + 'db'
    return ret


def binary_to_decimal(binary):
    """You will be given a binary string and you will need to convert it to decimal.

    Examples:
    binary_to_decimal("1111") # returns 15
    binary_to_decimal("100000") # returns 32
    """
    ret = 0
    for i in range(len(binary)):
        ret = ret + 2**i * int(binary[i])
    return ret


def decimal_to_hex(decimal):
    """You will be given a decimal number and you will need to convert it to hexadecimal.

    Examples:
    decimal_to_hex(32) # returns "db100000db"
    decimal_to_hex(15) # returns "db1111db"
    """
    ret = 'db'
    while decimal > 0:
        ret = str(hex(decimal % 16)[2]) + ret
        decimal = decimal // 16
    ret = 'db' + ret + 'db'
    return ret


def hex_to_decimal(hexadecimal):
    """You will be given a hexadecimal string and you will need to convert it to decimal.

    Examples:
    hex_to_decimal("100000") # returns 32
    hex_to_decimal("1111") # returns 15
    """
    ret = 0
    for i in range(len(hexadecimal)):
        ret = ret + 16**(len(hexadecimal)-i-1) * int(hexadecimal[i], 16)
    return ret


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f
	"""

    r = 'db'
    if decimal < 0:
        r += '1'
        decimal = -decimal
    else:
        r += '0'
    while decimal > 0:
        r = '1' + r if decimal % 2 else '0' + r
        decimal //= 2
    r += 'db'
    return r


if __name__ == '__main__':
    print("Example:")
    print(decimal_to_binary(15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(123456789) == "db111111100010001000011101101111db"
    assert decimal_to_binary(0) == "dbdb"
    print("Coding complete? Click 'Check' to earn cool rewards!")
